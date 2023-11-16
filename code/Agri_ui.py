# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
 
#     http://www.apache.org/licenses/LICENSE-2.0
 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import lvgl as lv
import utime
from usr import EventMesh
from machine import LCD, Pin
from tp import gt9xx
from usr.screen import Screen


# LCD initialization parameters
init_480X854_local = (
0x11,0,0,
0xFF,120,5,0x77,0x01,0x00,0x00,0x10,
0xC0,0,2,0xE9,0x03,
0xC1,0,2,0x11,0x02,
0xC2,0,2,0x31,0x08,
0xCC,0,1,0x10,
0xB0,0,16,0x00,0x0D,0x14,0x0D,0x10,0x05,0x02,0x08,0x08,0x1E,0x05,0x13,0x11,0xA3,0x29,0x18,
0xB1,0,16,0x00,0x0C,0x14,0x0C,0x10,0x05,0x03,0x08,0x07,0x20,0x05,0x13,0x11,0xA4,0x29,0x18,
0xFF,0,5,0x77,0x01,0x00,0x00,0x11,
0xB0,0,1,0x6C,
0xB1,0,1,0x43,
0xB2,0,1,0x07,
0xB3,0,1,0x80,
0xB5,0,1,0x47,
0xB7,0,1,0x85,
0xB8,0,1,0x20,
0xB9,0,1,0x10,
0xC1,0,1,0x78,
0xC2,0,1,0x78,
0xD0,0,1,0x88,
0xE0,100,3,0x00,0x00,0x02,
0xE1,0,11,0x08,0x00,0x0A,0x00,0x07,0x00,0x09,0x00,0x00,0x33,0x33,
0xE2,0,13,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0xE3,0,4,0x00,0x00,0x33,0x33,
0xE4,0,2,0x44,0x44,
0xE5,0,16,0x0E,0x60,0xA0,0xA0,0x10,0x60,0xA0,0xA0,0x0A,0x60,0xA0,0xA0,0x0C,0x60,0xA0,0xA0,
0xE6,0,4,0x00,0x00,0x33,0x33,
0xE7,0,2,0x44,0x44,
0xE8,0,16,0x0D,0x60,0xA0,0xA0,0x0F,0x60,0xA0,0xA0,0x09,0x60,0xA0,0xA0,0x0B,0x60,0xA0,0xA0,
0xEB,0,7,0x02,0x01,0xE4,0xE4,0x44,0x00,0x40,
0xEC,0,2,0x02,0x01,
0xED,0,16,0xAB,0x89,0x76,0x54,0x01,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x10,0x45,0x67,0x98,0xBA,
0xFF,0,5,0x77,0x01,0x00,0x00,0x00,
0x3A,0,1,0x77,
0x36,0,1,0x00,
0x35,0,1,0x00,
0x29,0,0)


class AgriUi(object):
    def __init__(self):
        self.__disp_buf1 = None
        self.__buf1_1 = None
        self.__disp_drv = None
        self.__indev_drv = None
        self.__tp_gt911 = None

        self.screens = []
        self.__lvgl_init()
        self.mipilcd = None
        print("ui init complete")

    def __lvgl_init(self):
        # Turn on the LCD backlight, and enable SD card.
        gpio1 = Pin(Pin.GPIO27, Pin.OUT, Pin.PULL_PU, 1)
        gpio2 = Pin(Pin.GPIO8, Pin.OUT, Pin.PULL_PU, 1)
        gpio3 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PU, 1)

        self.mipilcd = LCD()
        self.mipilcd.mipi_init(initbuf=bytearray(init_480X854_local), width=480, hight=854, DataLane=2,
                          TransMode=1)  # type=3 indicates mipi interface. Currently, the driver IC only supports vertical screen.
        # Initialize lvgl
        lv.init()
        # Register SDL display driver.
        self.__disp_buf1 = lv.disp_draw_buf_t()
        self.__buf1_1 = bytearray(500 * 1000 * 2)
        self.__disp_buf1.init(self.__buf1_1, None, len(self.__buf1_1))
        self.__disp_drv = lv.disp_drv_t()
        self.__disp_drv.init()
        self.__disp_drv.draw_buf = self.__disp_buf1
        self.__disp_drv.flush_cb = self.mipilcd.lcd_write
        self.__disp_drv.hor_res = 480
        self.__disp_drv.ver_res = 854
        self.__disp_drv.sw_rotate = 1  # Because it is a horizontal screen, it needs to be rotated
        self.__disp_drv.rotated = lv.DISP_ROT._270  # Rotation angle
        self.__disp_drv.register()

        # Initialize GT911
        self.__tp_gt911 = gt9xx(irq=40, reset=20)
        self.__tp_gt911.activate()
        self.__tp_gt911.init()
        print("gt911 init...")

        # Register the touch screen driver into lvgl
        self.__indev_drv = lv.indev_drv_t()
        self.__indev_drv.init()
        self.__indev_drv.type = lv.INDEV_TYPE.POINTER
        self.__indev_drv.read_cb = self.__tp_gt911.read
        self.__indev_drv.register()

        gpio4 = Pin(Pin.GPIO40, Pin.OUT, Pin.PULL_PU, 0)

        # Start lvgl
        lv.tick_inc(5)
        lv.task_handler()

        print("lvgl init complete")

    def add_screen(self, screen):
        """
        Add screen to GUI
        Args:
            screen: screen object
        """
        if isinstance(screen, Screen):
            self.screens.append(screen)
        return self

    def __create(self):
        for screen in self.screens:
            screen.create()

    def start(self):
        """
        Startup of GUI
        """
        self.__create()
        EventMesh.subscribe("load_screen", self.__route)
        EventMesh.publish("load_screen", "WelcomeScreen")
        utime.sleep(2)
        EventMesh.publish("load_screen", "MainScreen")

    def __route(self, topic, meta):
        """Show screen on LCD"""
        for screen in self.screens:
            if screen.name == meta:
                lv.scr_load(screen.screen)