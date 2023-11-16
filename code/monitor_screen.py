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

class MonitorScreen(Screen):
    def __init__(self):
        super().__init__()
        self.home_btn = None
        self.monitor_btn = None
        self.setting_btn = None
        self.dev_btn = None
        self.name = "MonitorScreen"
        self.screen = None
        super().create_style()

    def create(self):
        jiance = lv.obj()
        self.screen = jiance
        # create style style_jiance_main_main_default
        style_jiance_main_main_default = lv.style_t()
        style_jiance_main_main_default.init()
        style_jiance_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_jiance_main_main_default.set_bg_opa(255)

        # add style for jiance
        jiance.add_style(style_jiance_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_1 = lv.obj(jiance)
        jiance_cont_1.set_pos(0, 0)
        jiance_cont_1.set_size(100, 480)
        jiance_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_imgbtn_1 = lv.imgbtn(jiance)
        jiance_imgbtn_1.set_pos(23, 22)
        jiance_imgbtn_1.set_size(54, 57)

        jiance_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        jiance_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, jiance_imgbtn_1_imgReleased, None, None)
        jiance_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, jiance_imgbtn_1_imgReleased, None, None)
        jiance_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, jiance_imgbtn_1_imgReleased, None, None)
        jiance_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, jiance_imgbtn_1_imgReleased, None, None)

        jiance_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        jiance_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = jiance_imgbtn_1

        jiance_imgbtn_2 = lv.imgbtn(jiance)
        jiance_imgbtn_2.set_pos(27, 127)
        jiance_imgbtn_2.set_size(45, 44)

        jiance_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        jiance_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, jiance_imgbtn_2_imgReleased, None, None)
        jiance_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, jiance_imgbtn_2_imgReleased, None, None)
        jiance_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, jiance_imgbtn_2_imgReleased, None, None)
        jiance_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, jiance_imgbtn_2_imgReleased, None, None)
        jiance_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        jiance_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = jiance_imgbtn_2

        jiance_imgbtn_3 = lv.imgbtn(jiance)
        jiance_imgbtn_3.set_pos(27, 202)
        jiance_imgbtn_3.set_size(45, 44)

        jiance_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        jiance_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, jiance_imgbtn_3_imgReleased, None, None)
        jiance_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, jiance_imgbtn_3_imgReleased, None, None)
        jiance_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, jiance_imgbtn_3_imgReleased, None, None)
        jiance_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, jiance_imgbtn_3_imgReleased, None, None)
        jiance_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        jiance_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = jiance_imgbtn_3

        jiance_imgbtn_4 = lv.imgbtn(jiance)
        jiance_imgbtn_4.set_pos(27, 281)
        jiance_imgbtn_4.set_size(45, 44)

        jiance_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        jiance_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, jiance_imgbtn_4_imgReleased, None, None)
        jiance_imgbtn_4.set_src(lv.imgbtn.STATE.PRESSED, jiance_imgbtn_4_imgReleased, None, None)
        jiance_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, jiance_imgbtn_4_imgReleased, None, None)
        jiance_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, jiance_imgbtn_4_imgReleased, None, None)
        jiance_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        jiance_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = jiance_imgbtn_4

        jiance_imgbtn_5 = lv.imgbtn(jiance)
        jiance_imgbtn_5.set_pos(26, 367)
        jiance_imgbtn_5.set_size(49, 41)

        jiance_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        jiance_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, jiance_imgbtn_5_imgReleased, None, None)
        jiance_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, jiance_imgbtn_5_imgReleased, None, None)
        jiance_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, jiance_imgbtn_5_imgReleased, None, None)
        jiance_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, jiance_imgbtn_5_imgReleased, None, None)

        jiance_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        jiance_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_imgbtn_6 = lv.imgbtn(jiance)
        jiance_imgbtn_6.set_pos(26, 415)
        jiance_imgbtn_6.set_size(49, 41)

        jiance_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        jiance_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, jiance_imgbtn_6_imgReleased, None, None)
        jiance_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, jiance_imgbtn_6_imgReleased, None, None)
        jiance_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, jiance_imgbtn_6_imgReleased, None, None)
        jiance_imgbtn_6.set_src(lv.imgbtn.STATE.PRESSED, jiance_imgbtn_6_imgReleased, None, None)
        jiance_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        jiance_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_img_1 = lv.img(jiance)
        jiance_img_1.set_pos(798, 8)
        jiance_img_1.set_size(20, 15)
        jiance_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        jiance_img_1_img = "U:/img/mp2146739423.png"

        jiance_img_1.set_src(jiance_img_1_img)
        jiance_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_1 = lv.label(jiance)
        jiance_label_1.set_pos(124, 8)
        jiance_label_1.set_size(76, 13)
        jiance_label_1.set_text("China Unicom")
        jiance_label_1.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_img_2 = lv.img(jiance)
        jiance_img_2.set_pos(764, 9)
        jiance_img_2.set_size(18, 12)
        jiance_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        jiance_img_2_img = "U:/img/mp-1849026116.png"

        jiance_img_2.set_src(jiance_img_2_img)
        jiance_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_2 = lv.label(jiance)
        jiance_label_2.set_pos(703, 10)
        jiance_label_2.set_size(50, 13)
        jiance_label_2.set_text("12:00")
        jiance_label_2.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_tileview_2 = lv.tileview(jiance)
        jiance_tileview_2.set_pos(100, 28)
        jiance_tileview_2.set_size(754, 452)
        jiance_tileview_2_tileview = jiance_tileview_2.add_tile(0, 0, lv.DIR.RIGHT)
        jiance_tileview_2_Title = jiance_tileview_2.add_tile(1, 0, lv.DIR.LEFT)
        jiance_tileview_2.add_style(self.style_tileview, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_tileview_2.add_style(self.style_tileview_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        jiance_img_3 = lv.img(jiance)
        jiance_img_3.set_pos(60, 166)
        jiance_img_3.set_size(16, 14)
        jiance_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

        jiance_img_3_img = "U:/img/mp-347592130.png"

        jiance_img_3.set_src(jiance_img_3_img)
        jiance_img_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_2 = lv.obj(jiance)
        jiance_cont_2.set_pos(173, 76)
        jiance_cont_2.set_size(261, 75)
        jiance_label_3 = lv.label(jiance_cont_2)
        jiance_label_3.set_pos(41, 16)
        jiance_label_3.set_size(98, 18)
        jiance_label_3.set_text("Temperature")
        jiance_label_3.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_3.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_4 = lv.label(jiance_cont_2)
        jiance_label_4.set_pos(42, 41)
        jiance_label_4.set_size(98, 18)
        jiance_label_4.set_text("27°C")
        jiance_label_4.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_4.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_4.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_2.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_3 = lv.obj(jiance)
        jiance_cont_3.set_pos(172, 174)
        jiance_cont_3.set_size(261, 75)
        jiance_cont_3.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_4 = lv.obj(jiance)
        jiance_cont_4.set_pos(171, 271)
        jiance_cont_4.set_size(261, 75)
        jiance_cont_4.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_5 = lv.obj(jiance)
        jiance_cont_5.set_pos(170, 369)
        jiance_cont_5.set_size(261, 75)
        jiance_cont_5.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_6 = lv.obj(jiance)
        jiance_cont_6.set_pos(516, 77)
        jiance_cont_6.set_size(261, 75)
        jiance_cont_6.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_7 = lv.obj(jiance)
        jiance_cont_7.set_pos(517, 176)
        jiance_cont_7.set_size(261, 75)
        jiance_cont_7.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_8 = lv.obj(jiance)
        jiance_cont_8.set_pos(518, 274)
        jiance_cont_8.set_size(261, 75)
        jiance_cont_8.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_cont_9 = lv.obj(jiance)
        jiance_cont_9.set_pos(518, 370)
        jiance_cont_9.set_size(261, 75)
        jiance_cont_9.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_1 = lv.arc(jiance)
        jiance_arc_1.set_pos(307, 66)
        jiance_arc_1.set_size(117, 93)
        jiance_arc_1.set_bg_angles(0, 360)
        jiance_arc_1.set_angles(90, 290)
        jiance_arc_1.set_rotation(0)
        jiance_arc_1.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_1.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_1.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_1.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_1.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_1.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_1.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_1.add_style(self.style_arc_indicator_green, lv.PART.INDICATOR | lv.STATE.DEFAULT)

        jiance_arc_1.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_5 = lv.label(jiance)
        jiance_label_5.set_pos(561, 92)
        jiance_label_5.set_size(92, 19)
        jiance_label_5.set_text("Humidity")
        jiance_label_5.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_5.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_5.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_6 = lv.label(jiance)
        jiance_label_6.set_pos(562, 116)
        jiance_label_6.set_size(92, 19)
        jiance_label_6.set_text("20%")
        jiance_label_6.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_6.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_6.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_2 = lv.arc(jiance)
        jiance_arc_2.set_pos(658, 66)
        jiance_arc_2.set_size(117, 93)
        jiance_arc_2.set_bg_angles(0, 360)
        jiance_arc_2.set_angles(90, 150)
        jiance_arc_2.set_rotation(0)
        jiance_arc_2.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_2.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_2.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_2.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_2.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_2.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_2.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_2.add_style(self.style_arc_indicator_red, lv.PART.INDICATOR | lv.STATE.DEFAULT)

        jiance_arc_2.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_7 = lv.label(jiance)
        jiance_label_7.set_pos(215, 189)
        jiance_label_7.set_size(95, 17)
        jiance_label_7.set_text("Illuminance")
        jiance_label_7.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_7.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_7.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_8 = lv.label(jiance)
        jiance_label_8.set_pos(215, 215)
        jiance_label_8.set_size(95, 17)
        jiance_label_8.set_text("50000Lux")
        jiance_label_8.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_8.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_8.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_3 = lv.arc(jiance)
        jiance_arc_3.set_pos(309, 165)
        jiance_arc_3.set_size(117, 93)
        jiance_arc_3.set_bg_angles(0, 360)
        jiance_arc_3.set_angles(90, 320)
        jiance_arc_3.set_rotation(0)
        jiance_arc_3.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_3.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_3.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_3.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_3.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_3.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_3.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_3.add_style(self.style_arc_indicator_green, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_3.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_9 = lv.label(jiance)
        jiance_label_9.set_pos(560, 190)
        jiance_label_9.set_size(95, 17)
        jiance_label_9.set_text("Soil temperature")
        jiance_label_9.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_9.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_9.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_10 = lv.label(jiance)
        jiance_label_10.set_pos(561, 217)
        jiance_label_10.set_size(95, 17)
        jiance_label_10.set_text("25°C")
        jiance_label_10.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_10.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_10.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_4 = lv.arc(jiance)
        jiance_arc_4.set_pos(660, 169)
        jiance_arc_4.set_size(117, 93)
        jiance_arc_4.set_bg_angles(0, 360)
        jiance_arc_4.set_angles(90, 220)
        jiance_arc_4.set_rotation(0)
        jiance_arc_4.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_4.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_4.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_4.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_4.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_4.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_4.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_4.add_style(self.style_arc_indicator_yellow, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_4.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_11 = lv.label(jiance)
        jiance_label_11.set_pos(216, 286)
        jiance_label_11.set_size(95, 17)
        jiance_label_11.set_text("Oxygen concentration")
        jiance_label_11.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_11.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_11.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_12 = lv.label(jiance)
        jiance_label_12.set_pos(217, 312)
        jiance_label_12.set_size(95, 17)
        jiance_label_12.set_text("30%")
        jiance_label_12.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_12.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_12.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_5 = lv.arc(jiance)
        jiance_arc_5.set_pos(312, 262)
        jiance_arc_5.set_size(117, 93)
        jiance_arc_5.set_bg_angles(0, 360)
        jiance_arc_5.set_angles(90, 270)
        jiance_arc_5.set_rotation(0)
        jiance_arc_5.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_5.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_5.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_5.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_5.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_5.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_5.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_5.add_style(self.style_arc_indicator_green, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_5.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_13 = lv.label(jiance)
        jiance_label_13.set_pos(560, 290)
        jiance_label_13.set_size(115, 17)
        jiance_label_13.set_text("Carbon dioxide concentration")
        jiance_label_13.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_13.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_13.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_14 = lv.label(jiance)
        jiance_label_14.set_pos(564, 316)
        jiance_label_14.set_size(95, 17)
        jiance_label_14.set_text("0.02%")
        jiance_label_14.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_14.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_14.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_6 = lv.arc(jiance)
        jiance_arc_6.set_pos(663, 268)
        jiance_arc_6.set_size(117, 93)
        jiance_arc_6.set_bg_angles(0, 360)
        jiance_arc_6.set_angles(90, 120)
        jiance_arc_6.set_rotation(0)
        jiance_arc_6.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_6.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_6.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_6.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_6.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_6.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_6.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_6.add_style(self.style_arc_indicator_red, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_6.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_15 = lv.label(jiance)
        jiance_label_15.set_pos(215, 383)
        jiance_label_15.set_size(95, 17)
        jiance_label_15.set_text("Soil pH")
        jiance_label_15.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_15.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_15.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_16 = lv.label(jiance)
        jiance_label_16.set_pos(215, 410)
        jiance_label_16.set_size(95, 17)
        jiance_label_16.set_text("6.6")
        jiance_label_16.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_16.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_16.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_7 = lv.arc(jiance)
        jiance_arc_7.set_pos(312, 359)
        jiance_arc_7.set_size(117, 93)
        jiance_arc_7.set_bg_angles(0, 360)
        jiance_arc_7.set_angles(90, 220)
        jiance_arc_7.set_rotation(0)
        jiance_arc_7.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_7.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_7.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_7.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_7.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_7.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_7.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_7.add_style(self.style_arc_indicator_yellow, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_7.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

        jiance_label_17 = lv.label(jiance)
        jiance_label_17.set_pos(562, 384)
        jiance_label_17.set_size(95, 17)
        jiance_label_17.set_text("Soil EC")
        jiance_label_17.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_17.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_17.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_label_18 = lv.label(jiance)
        jiance_label_18.set_pos(563, 411)
        jiance_label_18.set_size(95, 17)
        jiance_label_18.set_text("6.6")
        jiance_label_18.set_long_mode(lv.label.LONG.WRAP)
        jiance_label_18.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        jiance_label_18.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        jiance_arc_8 = lv.arc(jiance)
        jiance_arc_8.set_pos(663, 363)
        jiance_arc_8.set_size(117, 93)
        jiance_arc_8.set_bg_angles(0, 360)
        jiance_arc_8.set_angles(90, 270)
        jiance_arc_8.set_rotation(0)
        jiance_arc_8.set_style_pad_top(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_8.set_style_pad_bottom(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_8.set_style_pad_left(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_8.set_style_pad_right(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_8.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_8.set_style_arc_rounded(True, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_8.add_style(self.style_arc, lv.PART.MAIN | lv.STATE.DEFAULT)
        jiance_arc_8.add_style(self.style_arc_indicator_green, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        jiance_arc_8.add_style(self.style_arc_knob, lv.PART.KNOB | lv.STATE.DEFAULT)

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