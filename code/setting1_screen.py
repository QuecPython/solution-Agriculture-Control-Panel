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
import utime

class SettingScreen(Screen):
    def __init__(self):
        super().__init__()
        self.save_btn = None
        self.setting_kb = None
        self.sw_setting2_btn = None
        self.dev_btn = None
        self.setting_btn = None
        self.home_btn = None
        self.monitor_btn = None
        self.screen = None
        # self.__msg_box = None
        # self.__label1 = None
        self.name = "SettingScreen"
        super().create_style()
        # EventMesh.subscribe("save_setting", self.__save_setting_cb)

    def create(self):
        setting = lv.obj()
        self.screen = setting
        # create style style_setting_main_main_default
        style_setting_main_main_default = lv.style_t()
        style_setting_main_main_default.init()
        style_setting_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_setting_main_main_default.set_bg_opa(255)

        # add style for setting
        setting.add_style(style_setting_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_cont_1 = lv.obj(setting)
        setting_cont_1.set_pos(0, 0)
        setting_cont_1.set_size(100, 480)
        setting_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_imgbtn_1 = lv.imgbtn(setting)
        setting_imgbtn_1.set_pos(23, 22)
        setting_imgbtn_1.set_size(54, 57)

        setting_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        setting_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_1_imgReleased, None, None)
        setting_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_1_imgReleased, None, None)
        setting_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting_imgbtn_1_imgReleased, None, None)
        setting_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting_imgbtn_1_imgReleased, None, None)

        setting_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        setting_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = setting_imgbtn_1

        setting_imgbtn_2 = lv.imgbtn(setting)
        setting_imgbtn_2.set_pos(27, 127)
        setting_imgbtn_2.set_size(45, 44)

        setting_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        setting_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_2_imgReleased, None, None)
        setting_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_2_imgReleased, None, None)
        setting_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting_imgbtn_2_imgReleased, None, None)
        setting_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting_imgbtn_2_imgReleased, None, None)
        setting_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        setting_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = setting_imgbtn_2

        setting_imgbtn_3 = lv.imgbtn(setting)
        setting_imgbtn_3.set_pos(27, 202)
        setting_imgbtn_3.set_size(45, 44)

        setting_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        setting_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_3_imgReleased, None, None)
        setting_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_3_imgReleased, None, None)
        setting_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting_imgbtn_3_imgReleased, None, None)
        setting_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting_imgbtn_3_imgReleased, None, None)
        setting_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        setting_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = setting_imgbtn_3

        setting_imgbtn_4 = lv.imgbtn(setting)
        setting_imgbtn_4.set_pos(27, 281)
        setting_imgbtn_4.set_size(45, 44)

        setting_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        setting_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_4_imgReleased, None, None)
        setting_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_4_imgReleased, None, None)
        setting_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting_imgbtn_4_imgReleased, None, None)
        setting_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting_imgbtn_4_imgReleased, None, None)
        setting_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        setting_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = setting_imgbtn_4

        setting_imgbtn_5 = lv.imgbtn(setting)
        setting_imgbtn_5.set_pos(26, 367)
        setting_imgbtn_5.set_size(49, 41)

        setting_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        setting_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_5_imgReleased, None, None)
        setting_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting_imgbtn_5_imgReleased, None, None)
        setting_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting_imgbtn_5_imgReleased, None, None)
        setting_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, setting_imgbtn_5_imgReleased, None, None)

        setting_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        setting_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_imgbtn_6 = lv.imgbtn(setting)
        setting_imgbtn_6.set_pos(26, 415)
        setting_imgbtn_6.set_size(49, 41)

        setting_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        setting_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, setting_imgbtn_6_imgReleased, None, None)
        setting_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, setting_imgbtn_6_imgReleased, None, None)
        setting_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, setting_imgbtn_6_imgReleased, None, None)
        setting_imgbtn_6.set_src(lv.imgbtn.STATE.PRESSED, setting_imgbtn_6_imgReleased, None, None)

        setting_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        setting_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_img_1 = lv.img(setting)
        setting_img_1.set_pos(798, 8)
        setting_img_1.set_size(20, 15)
        setting_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        setting_img_1_img = "U:/img/mp2146739423.png"

        setting_img_1.set_src(setting_img_1_img)
        setting_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_1 = lv.label(setting)
        setting_label_1.set_pos(124, 8)
        setting_label_1.set_size(76, 13)
        setting_label_1.set_text("China Unicom")
        setting_label_1.set_long_mode(lv.label.LONG.WRAP)
        setting_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_img_2 = lv.img(setting)
        setting_img_2.set_pos(764, 9)
        setting_img_2.set_size(18, 12)
        setting_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        setting_img_2_img = "U:/img/mp-1849026116.png"

        setting_img_2.set_src(setting_img_2_img)
        setting_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_2 = lv.label(setting)
        setting_label_2.set_pos(703, 10)
        setting_label_2.set_size(50, 13)
        setting_label_2.set_text("12:00")
        setting_label_2.set_long_mode(lv.label.LONG.WRAP)
        setting_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_tileview_2 = lv.tileview(setting)
        setting_tileview_2.set_pos(242, 61)
        setting_tileview_2.set_size(612, 419)
        setting_tileview_2_tileview = setting_tileview_2.add_tile(0, 0, lv.DIR.RIGHT)
        setting_tileview_2_Title = setting_tileview_2.add_tile(1, 0, lv.DIR.LEFT)
        setting_tileview_2.add_style(self.style_tileview, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_tileview_2.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting_cont_6 = lv.obj(setting)
        setting_cont_6.set_pos(294, 123)
        setting_cont_6.set_size(126, 41)
        setting_cont_6.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_cont_7 = lv.obj(setting)
        setting_cont_7.set_pos(296, 250)
        setting_cont_7.set_size(126, 41)
        setting_cont_7.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_cont_8 = lv.obj(setting)
        setting_cont_8.set_pos(294, 185)
        setting_cont_8.set_size(126, 41)
        setting_cont_8.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_btn_11 = lv.btn(setting)
        setting_btn_11.set_pos(108, 182)
        setting_btn_11.set_size(120, 45)
        setting_btn_11_label = lv.label(setting_btn_11)
        setting_btn_11_label.set_text("Parameter settings")
        setting_btn_11.set_style_pad_all(0, lv.STATE.DEFAULT)
        setting_btn_11_label.center()
        setting_btn_11_label.set_style_text_color(lv.color_make(0xfc, 0xfc, 0xfc), lv.STATE.DEFAULT)
        setting_btn_11_label.set_style_text_font(lv.font_siyuan_Regular_18, lv.STATE.DEFAULT)
        setting_btn_11.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_btn_12 = lv.btn(setting)
        setting_btn_12.set_pos(108, 262)
        setting_btn_12.set_size(120, 45)
        setting_btn_12_label = lv.label(setting_btn_12)
        setting_btn_12_label.set_text("Basic settings")
        setting_btn_12.set_style_pad_all(0, lv.STATE.DEFAULT)
        setting_btn_12_label.align(lv.ALIGN.CENTER, 0, 0)
        setting_btn_12_label.set_style_text_color(lv.color_make(0xfc, 0xfc, 0xfc), lv.STATE.DEFAULT)
        setting_btn_12_label.set_style_text_font(lv.font_siyuan_Regular_18, lv.STATE.DEFAULT)
        setting_btn_12.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.sw_setting2_btn = setting_btn_12

        setting_cont_9 = lv.obj(setting)
        setting_cont_9.set_pos(298, 313)
        setting_cont_9.set_size(126, 41)
        setting_cont_9.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_14 = lv.label(setting)
        setting_label_14.set_pos(307, 136)
        setting_label_14.set_size(100, 32)
        setting_label_14.set_text("Soil pH")
        setting_label_14.set_long_mode(lv.label.LONG.WRAP)
        setting_label_14.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_14.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_16 = lv.label(setting)
        setting_label_16.set_pos(306, 198)
        setting_label_16.set_size(109, 24)
        setting_label_16.set_text("Soil moisture ")
        setting_label_16.set_long_mode(lv.label.LONG.WRAP)
        setting_label_16.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_16.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_ta_1 = lv.textarea(setting)
        setting_ta_1.set_pos(589, 128)
        setting_ta_1.set_size(43, 23)
        setting_ta_1.set_text("5")
        setting_ta_1.set_one_line(True)
        setting_ta_1.set_ext_click_area(10)

        self.setting_kb = lv.keyboard(setting)
        self.setting_kb.add_flag(lv.obj.FLAG.HIDDEN)

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_1.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_1.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_1.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting_ta_2 = lv.textarea(setting)
        setting_ta_2.set_pos(732, 128)
        setting_ta_2.set_size(48, 22)
        setting_ta_2.set_text("8.5")
        setting_ta_2.set_one_line(True)
        setting_ta_2.set_ext_click_area(10)

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_2.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_2.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_2.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting_label_20 = lv.label(setting)
        setting_label_20.set_pos(543, 130)
        setting_label_20.set_size(47, 16)
        setting_label_20.set_text("Min")
        setting_label_20.set_long_mode(lv.label.LONG.WRAP)
        setting_label_20.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_20.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_21 = lv.label(setting)
        setting_label_21.set_pos(681, 130)
        setting_label_21.set_size(47, 16)
        setting_label_21.set_text("Max")
        setting_label_21.set_long_mode(lv.label.LONG.WRAP)
        setting_label_21.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_21.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_22 = lv.label(setting)
        setting_label_22.set_pos(304, 263)
        setting_label_22.set_size(109, 24)
        setting_label_22.set_text("Illuminance")
        setting_label_22.set_long_mode(lv.label.LONG.WRAP)
        setting_label_22.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_22.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_23 = lv.label(setting)
        setting_label_23.set_pos(308, 325)
        setting_label_23.set_size(109, 24)
        setting_label_23.set_text("Oxygen concentration")
        setting_label_23.set_long_mode(lv.label.LONG.WRAP)
        setting_label_23.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_23.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_ta_3 = lv.textarea(setting)
        setting_ta_3.set_pos(732, 190)
        setting_ta_3.set_size(48, 22)
        setting_ta_3.set_one_line(True)
        setting_ta_3.set_text("85")
        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_3.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_3.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_3.set_ext_click_area(10)

        setting_ta_3.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting_ta_4 = lv.textarea(setting)
        setting_ta_4.set_pos(589, 190)
        setting_ta_4.set_size(44, 24)
        setting_ta_4.set_one_line(True)
        setting_ta_4.set_text("45")

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_4.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_4.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_ta_4.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        setting_ta_4.set_ext_click_area(10)

        setting_label_24 = lv.label(setting)
        setting_label_24.set_pos(543, 193)
        setting_label_24.set_size(47, 16)
        setting_label_24.set_text("Min")
        setting_label_24.set_long_mode(lv.label.LONG.WRAP)
        setting_label_24.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_24.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_25 = lv.label(setting)
        setting_label_25.set_pos(681, 193)
        setting_label_25.set_size(47, 16)
        setting_label_25.set_text("Max")
        setting_label_25.set_long_mode(lv.label.LONG.WRAP)
        setting_label_25.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_25.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_ta_5 = lv.textarea(setting)
        setting_ta_5.set_pos(589, 258)
        setting_ta_5.set_size(40, 22)
        setting_ta_5.set_one_line(True)
        setting_ta_5.set_text("500")

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_5.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_5.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_5.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        setting_ta_5.set_ext_click_area(10)

        setting_ta_6 = lv.textarea(setting)
        setting_ta_6.set_pos(732, 258)
        setting_ta_6.set_size(46, 22)
        setting_ta_6.set_one_line(True)
        setting_ta_6.set_text("10")

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_6.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_6.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_6.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        setting_ta_6.set_ext_click_area(10)

        setting_label_28 = lv.label(setting)
        setting_label_28.set_pos(543, 330)
        setting_label_28.set_size(47, 16)
        setting_label_28.set_text("Min")
        setting_label_28.set_long_mode(lv.label.LONG.WRAP)
        setting_label_28.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_28.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_ta_7 = lv.textarea(setting)
        setting_ta_7.set_pos(589, 328)
        setting_ta_7.set_size(42, 22)
        setting_ta_7.set_one_line(True)
        setting_ta_7.set_text("45")
        setting_ta_7.set_ext_click_area(10)

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_7.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_7.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_7.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting_label_29 = lv.label(setting)
        setting_label_29.set_pos(681, 330)
        setting_label_29.set_size(47, 16)
        setting_label_29.set_text("Max")
        setting_label_29.set_long_mode(lv.label.LONG.WRAP)
        setting_label_29.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_29.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_ta_8 = lv.textarea(setting)
        setting_ta_8.set_pos(732, 328)
        setting_ta_8.set_size(44, 22)
        setting_ta_8.set_one_line(True)
        setting_ta_8.set_text("85")
        setting_ta_8.set_ext_click_area(10)

        self.setting_kb.set_textarea(setting_ta_1)
        setting_ta_8.add_event_cb(lambda e: self.ta_event_cb(e, self.setting_kb), lv.EVENT.ALL, None)
        setting_ta_8.add_style(self.style_ta, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_ta_8.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        setting_label_30 = lv.label(setting)
        setting_label_30.set_pos(543, 260)
        setting_label_30.set_size(47, 16)
        setting_label_30.set_text("Min")
        setting_label_30.set_long_mode(lv.label.LONG.WRAP)
        setting_label_30.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_30.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_label_31 = lv.label(setting)
        setting_label_31.set_pos(681, 260)
        setting_label_31.set_size(47, 16)
        setting_label_31.set_text("Max")
        setting_label_31.set_long_mode(lv.label.LONG.WRAP)
        setting_label_31.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        setting_label_31.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        setting_sw_2 = lv.switch(setting)
        setting_sw_2.set_pos(453, 133)
        setting_sw_2.set_size(40, 20)
        setting_sw_2.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_sw_2.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        setting_sw_2.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        setting_sw_2.add_state(lv.STATE.CHECKED)
        setting_sw_2.set_ext_click_area(10)

        setting_sw_5 = lv.switch(setting)
        setting_sw_5.set_pos(453, 258)
        setting_sw_5.set_size(40, 20)
        setting_sw_5.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_sw_5.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        setting_sw_5.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        setting_sw_5.set_ext_click_area(10)

        setting_sw_6 = lv.switch(setting)
        setting_sw_6.set_pos(453, 325)
        setting_sw_6.set_size(40, 20)
        setting_sw_6.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_sw_6.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        setting_sw_6.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        setting_sw_6.set_ext_click_area(10)

        setting_sw_7 = lv.switch(setting)
        setting_sw_7.set_pos(453, 194)
        setting_sw_7.set_size(40, 20)
        setting_sw_7.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        setting_sw_7.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        setting_sw_7.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        setting_sw_7.set_ext_click_area(10)

        setting_btn_1 = lv.btn(setting)
        setting_btn_1.set_pos(628, 407)
        setting_btn_1.set_size(100, 45)
        setting_btn_1_label = lv.label(setting_btn_1)
        setting_btn_1_label.set_text("Save the settings")
        setting_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
        setting_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
        setting_btn_1_label.set_style_text_color(lv.color_make(0xfc, 0xfc, 0xfc), lv.STATE.DEFAULT)
        setting_btn_1_label.set_style_text_font(lv.font_siyuan_Regular_14, lv.STATE.DEFAULT)

        setting_btn_1.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.save_btn = setting_btn_1

        setting_img_3 = lv.img(setting)
        setting_img_3.set_pos(58, 236)
        setting_img_3.set_size(16, 14)
        setting_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

        setting_img_3_img = "U:/img/mp-347592130.png"

        setting_img_3.set_src(setting_img_3_img)
        setting_img_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        # self.__msg_box = lv.msgbox(setting, "", "success to save!", [], False)
        # self.__msg_box.set_size(200, 90)
        # self.__msg_box.center()
        # self.__msg_box.add_flag(lv.obj.FLAG.HIDDEN)

        self.setting_kb = lv.keyboard(setting)
        self.setting_kb.add_flag(lv.obj.FLAG.HIDDEN)

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.sw_setting2_btn.add_event_cb(lambda e: self.__sw_setting2_btn_event_cb(e), lv.EVENT.PRESSED, None)
        # self.save_btn.add_event_cb(lambda e: self.__save_setting_event_cb(e), lv.EVENT.PRESSED, None)

    def ta_event_cb(self, e, kb):
        code = e.get_code()
        ta = e.get_target()
        if code == lv.EVENT.FOCUSED:
            kb.set_textarea(ta)
            kb.clear_flag(lv.obj.FLAG.HIDDEN)

        if code == lv.EVENT.DEFOCUSED:
            kb.set_textarea(None)
            kb.add_flag(lv.obj.FLAG.HIDDEN)

    def __sw_setting2_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "Setting2Screen")

    # def __save_setting_event_cb(self, e):
    #     src = e.get_target()
    #     code = e.get_code()
    #     print("Click event occurs")
    #     EventMesh.publish("save_setting", 1)

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
    
    # def __save_setting_cb(self, topic, meta):
    #     if self.__msg_box:
    #         print("Pop-ups")
    #         self.__msg_box.clear_flag(lv.obj.FLAG.HIDDEN)
    #         utime.sleep(1)
    #         self.__msg_box.add_flag(lv.obj.FLAG.HIDDEN)
    #         print("The pop-up window ends")