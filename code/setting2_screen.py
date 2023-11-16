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

class Setting2Screen(Screen):
    def __init__(self):
        super().__init__()
        self.about_item = None
        self.dev_btn = None
        self.setting_btn = None
        self.monitor_btn = None
        self.home_btn = None
        self.screen = None
        self.name = "Setting2Screen"
        super().create_style()

    def create(self):
        setting2 = lv.obj()
        self.screen = setting2
        # create style style_setting2_main_main_default
        style_setting2_main_main_default = lv.style_t()
        style_setting2_main_main_default.init()
        style_setting2_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_setting2_main_main_default.set_bg_opa(255)

        # add style for setting2
        setting2.add_style(style_setting2_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_cont_1 = lv.obj(setting2)
        setting2_cont_1.set_pos(0, 0)
        setting2_cont_1.set_size(100, 480)
        setting2_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_imgbtn_1 = lv.imgbtn(setting2)
        setting2_imgbtn_1.set_pos(23, 22)
        setting2_imgbtn_1.set_size(54, 57)

        setting2_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        setting2_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_1_imgReleased, None, None)
        setting2_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_1_imgReleased, None, None)
        setting2_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting2_imgbtn_1_imgReleased, None, None)
        setting2_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting2_imgbtn_1_imgReleased, None, None)
        setting2_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        setting2_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = setting2_imgbtn_1

        setting2_imgbtn_2 = lv.imgbtn(setting2)
        setting2_imgbtn_2.set_pos(27, 127)
        setting2_imgbtn_2.set_size(45, 44)

        setting2_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        setting2_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_2_imgReleased, None, None)
        setting2_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_2_imgReleased, None, None)
        setting2_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting2_imgbtn_2_imgReleased, None, None)
        setting2_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting2_imgbtn_2_imgReleased, None, None)
        setting2_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        setting2_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = setting2_imgbtn_2

        setting2_imgbtn_3 = lv.imgbtn(setting2)
        setting2_imgbtn_3.set_pos(27, 202)
        setting2_imgbtn_3.set_size(45, 44)

        setting2_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        setting2_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_3_imgReleased, None, None)
        setting2_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_3_imgReleased, None, None)
        setting2_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting2_imgbtn_3_imgReleased, None, None)
        setting2_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting2_imgbtn_3_imgReleased, None, None)
        setting2_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        setting2_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = setting2_imgbtn_3

        setting2_imgbtn_4 = lv.imgbtn(setting2)
        setting2_imgbtn_4.set_pos(27, 281)
        setting2_imgbtn_4.set_size(45, 44)

        setting2_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        setting2_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_4_imgReleased, None, None)
        setting2_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_4_imgReleased, None, None)
        setting2_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting2_imgbtn_4_imgReleased, None, None)
        setting2_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting2_imgbtn_4_imgReleased, None, None)
        setting2_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        setting2_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = setting2_imgbtn_4

        setting2_imgbtn_5 = lv.imgbtn(setting2)
        setting2_imgbtn_5.set_pos(26, 367)
        setting2_imgbtn_5.set_size(49, 41)

        setting2_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        setting2_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_5_imgReleased, None, None)
        setting2_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting2_imgbtn_5_imgReleased, None, None)
        setting2_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting2_imgbtn_5_imgReleased, None, None)
        setting2_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, setting2_imgbtn_5_imgReleased, None, None)
        setting2_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        setting2_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_cont_5 = lv.obj(setting2)
        setting2_cont_5.set_pos(100, 28)
        setting2_cont_5.set_size(754, 452)
        setting2_list_1 = lv.list(setting2_cont_5)
        setting2_list_1.set_pos(84, 83)
        setting2_list_1.set_size(596, 305)

        setting2_list_1_btn_0_img = "U:/img/mp1709126206.png"
        setting2_list_1_btn_0 = setting2_list_1.add_btn(setting2_list_1_btn_0_img, "About")

        # add style for setting2_list_1_btn_0
        setting2_list_1_btn_0.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.about_item = setting2_list_1_btn_0

        setting2_list_1_btn_1_img = "U:/img/mp-612897245.png"
        setting2_list_1_btn_1 = setting2_list_1.add_btn(setting2_list_1_btn_1_img, "Volume settings")

        # add style for setting2_list_1_btn_1
        setting2_list_1_btn_1.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_list_1_btn_2_img = "U:/img/mp1344530085.png"
        setting2_list_1_btn_2 = setting2_list_1.add_btn(setting2_list_1_btn_2_img, "Check for updates")

        # add style for setting2_list_1_btn_2
        setting2_list_1_btn_2.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_list_1_btn_3_img = "U:/img/mp-1120889833.png"
        setting2_list_1_btn_3 = setting2_list_1.add_btn(setting2_list_1_btn_3_img, "Low power settings")

        # add style for setting2_list_1_btn_3
        setting2_list_1_btn_3.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_list_1_btn_4_img = "U:/img/mp2028397566.png"
        setting2_list_1_btn_4 = setting2_list_1.add_btn(setting2_list_1_btn_4_img, "Screen time settings")

        # add style for setting2_list_1_btn_4
        setting2_list_1_btn_4.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting2_list_1_btn_5_img = "U:/img/mp1359371871.png"
        setting2_list_1_btn_5 = setting2_list_1.add_btn(setting2_list_1_btn_5_img, "Mode settings")

        # add style for setting2_list_1_btn_5
        setting2_list_1_btn_5.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_list_1.add_style(self.style_main_list, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_list_1.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting2_cont_5.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_imgbtn_6 = lv.imgbtn(setting2)
        setting2_imgbtn_6.set_pos(26, 415)
        setting2_imgbtn_6.set_size(49, 41)

        setting2_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        setting2_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, setting2_imgbtn_6_imgReleased, None, None)
        setting2_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting2_imgbtn_6_imgReleased, None, None)
        setting2_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting2_imgbtn_6_imgReleased, None, None)
        setting2_imgbtn_6.set_src(lv.imgbtn.STATE.PRESSED, setting2_imgbtn_6_imgReleased, None, None)
        setting2_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        setting2_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_img_1 = lv.img(setting2)
        setting2_img_1.set_pos(798, 8)
        setting2_img_1.set_size(20, 15)
        setting2_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        setting2_img_1_img = "U:/img/mp2146739423.png"

        setting2_img_1.set_src(setting2_img_1_img)
        setting2_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_label_1 = lv.label(setting2)
        setting2_label_1.set_pos(124, 8)
        setting2_label_1.set_size(76, 13)
        setting2_label_1.set_text("China Unicom")
        setting2_label_1.set_long_mode(lv.label.LONG.WRAP)
        setting2_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting2_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_img_2 = lv.img(setting2)
        setting2_img_2.set_pos(764, 9)
        setting2_img_2.set_size(18, 12)
        setting2_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        setting2_img_2_img = "U:/img/mp-1849026116.png"

        setting2_img_2.set_src(setting2_img_2_img)
        setting2_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_label_2 = lv.label(setting2)
        setting2_label_2.set_pos(703, 10)
        setting2_label_2.set_size(50, 13)
        setting2_label_2.set_text("12:00")
        setting2_label_2.set_long_mode(lv.label.LONG.WRAP)
        setting2_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting2_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting2_label_19 = lv.label(setting2)
        setting2_label_19.set_pos(414, 78)
        setting2_label_19.set_size(102, 21)
        setting2_label_19.set_text("Basic settings")
        setting2_label_19.set_long_mode(lv.label.LONG.WRAP)
        setting2_label_19.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting2_label_19.add_style(self.style_siyuan_20, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.about_item.add_event_cb(lambda e: self.__about_item_event_cb(e), lv.EVENT.CLICKED, None)

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

    def __about_item_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "AboutScreen")