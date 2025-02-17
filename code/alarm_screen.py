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
from usr.screen import Screen
from usr import EventMesh

class AlarmScreen(Screen):
    def __init__(self):
        super().__init__()
        self.home_btn = None
        self.dev_btn = None
        self.monitor_btn = None
        self.setting_btn = None
        self.screen = None
        self.name = "AlarmScreen"
        super().create_style()

    def create(self):
        alarm = lv.obj()
        self.screen = alarm
        # create style style_alarm_main_main_default
        style_alarm_main_main_default = lv.style_t()
        style_alarm_main_main_default.init()
        style_alarm_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_alarm_main_main_default.set_bg_opa(255)

        # add style for alarm
        alarm.add_style(style_alarm_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_cont_menu = lv.obj(alarm)
        alarm_cont_menu.set_pos(0, 0)
        alarm_cont_menu.set_size(100, 480)
        alarm_cont_menu.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_imgbtn_home = lv.imgbtn(alarm)
        alarm_imgbtn_home.set_pos(23, 22)
        alarm_imgbtn_home.set_size(54, 57)

        alarm_imgbtn_home_imgReleased = "U:/img/mp-2145617244.png"
        alarm_imgbtn_home.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_home_imgReleased, None, None)
        alarm_imgbtn_home.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_home_imgReleased, None, None)
        alarm_imgbtn_home.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, alarm_imgbtn_home_imgReleased, None, None)
        alarm_imgbtn_home.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, alarm_imgbtn_home_imgReleased, None, None)

        alarm_imgbtn_home.add_flag(lv.obj.FLAG.CHECKABLE)
        alarm_imgbtn_home.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = alarm_imgbtn_home

        alarm_imgbtn_jiance = lv.imgbtn(alarm)
        alarm_imgbtn_jiance.set_pos(27, 127)
        alarm_imgbtn_jiance.set_size(45, 44)

        alarm_imgbtn_jiance_imgReleased = "U:/img/mp753364720.png"
        alarm_imgbtn_jiance.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_jiance_imgReleased, None, None)
        alarm_imgbtn_jiance.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_jiance_imgReleased, None, None)
        alarm_imgbtn_jiance.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, alarm_imgbtn_jiance_imgReleased, None, None)
        alarm_imgbtn_jiance.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, alarm_imgbtn_jiance_imgReleased, None, None)
        alarm_imgbtn_jiance.add_flag(lv.obj.FLAG.CHECKABLE)
        alarm_imgbtn_jiance.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = alarm_imgbtn_jiance

        alarm_imgbtn_setting = lv.imgbtn(alarm)
        alarm_imgbtn_setting.set_pos(27, 202)
        alarm_imgbtn_setting.set_size(45, 44)

        alarm_imgbtn_setting_imgReleased = "U:/img/mp-370417216.png"
        alarm_imgbtn_setting.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_setting_imgReleased, None, None)
        alarm_imgbtn_setting.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_setting_imgReleased, None, None)
        alarm_imgbtn_setting.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, alarm_imgbtn_setting_imgReleased, None, None)
        alarm_imgbtn_setting.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, alarm_imgbtn_setting_imgReleased, None, None)

        alarm_imgbtn_setting.add_flag(lv.obj.FLAG.CHECKABLE)
        alarm_imgbtn_setting.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = alarm_imgbtn_setting

        alarm_imgbtn_device = lv.imgbtn(alarm)
        alarm_imgbtn_device.set_pos(27, 281)
        alarm_imgbtn_device.set_size(45, 44)

        alarm_imgbtn_device_imgReleased = "U:/img/mp1105200495.png"
        alarm_imgbtn_device.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_device_imgReleased, None, None)
        alarm_imgbtn_device.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_device_imgReleased, None, None)
        alarm_imgbtn_device.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, alarm_imgbtn_device_imgReleased, None, None)
        alarm_imgbtn_device.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, alarm_imgbtn_device_imgReleased, None, None)
        alarm_imgbtn_device.add_flag(lv.obj.FLAG.CHECKABLE)
        alarm_imgbtn_device.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = alarm_imgbtn_device

        alarm_imgbtn_up = lv.imgbtn(alarm)
        alarm_imgbtn_up.set_pos(26, 367)
        alarm_imgbtn_up.set_size(49, 41)

        alarm_imgbtn_up_imgReleased = "U:/img/mp256257620.png"
        alarm_imgbtn_up.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_up_imgReleased, None, None)
        alarm_imgbtn_up.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_up_imgReleased, None, None)
        alarm_imgbtn_up.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, alarm_imgbtn_up_imgReleased, None, None)
        alarm_imgbtn_up.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, alarm_imgbtn_up_imgReleased, None, None)

        alarm_imgbtn_up.add_flag(lv.obj.FLAG.CHECKABLE)
        alarm_imgbtn_up.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_cont_alarm = lv.obj(alarm)
        alarm_cont_alarm.set_pos(100, 28)
        alarm_cont_alarm.set_size(754, 452)
        alarm_cont_alarm.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_imgbtn_down = lv.imgbtn(alarm)
        alarm_imgbtn_down.set_pos(26, 415)
        alarm_imgbtn_down.set_size(49, 41)

        alarm_imgbtn_down_imgReleased = "U:/img/mp-1736843955.png"
        alarm_imgbtn_down.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_down_imgReleased, None, None)
        alarm_imgbtn_down.set_src(lv.imgbtn.STATE.RELEASED, alarm_imgbtn_down_imgReleased, None, None)
        alarm_imgbtn_down.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, alarm_imgbtn_down_imgReleased, None, None)
        alarm_imgbtn_down.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, alarm_imgbtn_down_imgReleased, None, None)
        alarm_imgbtn_down.add_flag(lv.obj.FLAG.CHECKABLE)
        alarm_imgbtn_down.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_img_battery = lv.img(alarm)
        alarm_img_battery.set_pos(798, 8)
        alarm_img_battery.set_size(20, 15)
        alarm_img_battery.add_flag(lv.obj.FLAG.CLICKABLE)

        alarm_img_battery_img = "U:/img/mp2146739423.png"

        alarm_img_battery.set_src(alarm_img_battery_img)
        alarm_img_battery.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_yys = lv.label(alarm)
        alarm_label_yys.set_pos(124, 8)
        alarm_label_yys.set_size(76, 13)
        alarm_label_yys.set_text("Unicom")
        alarm_label_yys.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_yys.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_yys.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_img_sig = lv.img(alarm)
        alarm_img_sig.set_pos(764, 9)
        alarm_img_sig.set_size(18, 12)
        alarm_img_sig.add_flag(lv.obj.FLAG.CLICKABLE)

        alarm_img_sig_img = "U:/img/mp-1849026116.png"

        alarm_img_sig.set_src(alarm_img_sig_img)
        alarm_img_sig.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_time = lv.label(alarm)
        alarm_label_time.set_pos(703, 10)
        alarm_label_time.set_size(50, 13)
        alarm_label_time.set_text("12:00")
        alarm_label_time.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_time.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_time.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_cont_1 = lv.obj(alarm)
        alarm_cont_1.set_pos(168, 122)
        alarm_cont_1.set_size(507, 76)
        alarm_label_3 = lv.label(alarm_cont_1)
        alarm_label_3.set_pos(29, 16)
        alarm_label_3.set_size(189, 22)
        alarm_label_3.set_text("Soil moisture low")
        alarm_label_3.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_3.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_4 = lv.label(alarm_cont_1)
        alarm_label_4.set_pos(27, 45)
        alarm_label_4.set_size(139, 22)
        alarm_label_4.set_text("State: Todo")
        alarm_label_4.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_4.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_4.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_6 = lv.label(alarm_cont_1)
        alarm_label_6.set_pos(314, 28)
        alarm_label_6.set_size(183, 24)
        alarm_label_6.set_text("2022-05-27")
        alarm_label_6.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_6.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_6.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_cont_1.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_5 = lv.label(alarm)
        alarm_label_5.set_pos(168, 70)
        alarm_label_5.set_size(183, 23)
        alarm_label_5.set_text("Alarm record")
        alarm_label_5.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_5.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_5.add_style(self.style_siyuan_22, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_btn_1 = lv.btn(alarm)
        alarm_btn_1.set_pos(713, 135)
        alarm_btn_1.set_size(97, 47)
        alarm_btn_1_label = lv.label(alarm_btn_1)
        alarm_btn_1_label.set_text("Doing")
        alarm_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
        alarm_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
        alarm_btn_1_label.set_style_text_color(lv.color_make(0xfa, 0xfa, 0xfa), lv.STATE.DEFAULT)
        alarm_btn_1_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
        alarm_btn_1.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_cont_2 = lv.obj(alarm)
        alarm_cont_2.set_pos(168, 227)
        alarm_cont_2.set_size(507, 76)
        alarm_label_1_7 = lv.label(alarm_cont_2)
        alarm_label_1_7.set_pos(6, 16)
        alarm_label_1_7.set_size(194, 22)
        alarm_label_1_7.set_text("CO2 too low.")
        alarm_label_1_7.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_1_7.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_1_7.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_2_7 = lv.label(alarm_cont_2)
        alarm_label_2_7.set_pos(27, 45)
        alarm_label_2_7.set_size(214, 22)
        alarm_label_2_7.set_text("State: Processed")
        alarm_label_2_7.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_2_7.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_2_7.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_label_3_7 = lv.label(alarm_cont_2)
        alarm_label_3_7.set_pos(314, 28)
        alarm_label_3_7.set_size(183, 22)
        alarm_label_3_7.set_text("2022-05-26")
        alarm_label_3_7.set_long_mode(lv.label.LONG.WRAP)
        alarm_label_3_7.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarm_label_3_7.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_cont_2.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarm_btn_2 = lv.btn(alarm)
        alarm_btn_2.set_pos(715, 237)
        alarm_btn_2.set_size(97, 47)
        alarm_btn_2_label = lv.label(alarm_btn_2)
        alarm_btn_2_label.set_text("Todo")
        alarm_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
        alarm_btn_2_label.align(lv.ALIGN.CENTER, 0, 0)
        alarm_btn_2_label.set_style_text_color(lv.color_make(0xfa, 0xfa, 0xfa), lv.STATE.DEFAULT)
        alarm_btn_2_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
        alarm_btn_2.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)

    def __home_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "MainScreen")

    def __monitor_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "MonitorScreen")

    def __dev_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "Dev1Screen")

    def __setting_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "SettingScreen")