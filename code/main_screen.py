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
from usr import EventMesh
from usr.screen import Screen


class MainScreen(Screen):
    def __init__(self):
        super().__init__()
        self.dev_btn = None
        self.setting_btn = None
        self.monitor_btn_2 = None
        self.alarm_btn = None
        self.monitor_btn = None
        self.weather_btn = None
        self.screen = None
        self.name = "MainScreen"
        super().create_style()
        
    def create(self):
        main = lv.obj()
        self.screen = main

        # add style for main
        main.add_style(self.style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_1 = lv.obj(main)
        main_cont_1.set_pos(0, 0)
        main_cont_1.set_size(100, 480)

        main_cont_1.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_imgbtn_1 = lv.imgbtn(main)
        main_imgbtn_1.set_pos(23, 22)
        main_imgbtn_1.set_size(54, 57)

        main_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        main_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_1_imgReleased, None, None)

        # add style for main_imgbtn_1
        main_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_imgbtn_2 = lv.imgbtn(main)
        main_imgbtn_2.set_pos(27, 127)
        main_imgbtn_2.set_size(45, 44)

        main_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        main_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, main_imgbtn_2_imgReleased, None, None)
        main_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_2_imgReleased, None, None)
        main_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, main_imgbtn_2_imgReleased, None, None)
        main_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, main_imgbtn_2_imgReleased, None, None)
        main_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn_2 = main_imgbtn_2

        main_imgbtn_3 = lv.imgbtn(main)
        main_imgbtn_3.set_pos(27, 202)
        main_imgbtn_3.set_size(45, 44)

        main_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        main_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_3_imgReleased, None, None)
        main_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, main_imgbtn_3_imgReleased, None, None)
        main_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, main_imgbtn_3_imgReleased, None, None)
        main_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, main_imgbtn_3_imgReleased, None, None)
        main_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        main_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = main_imgbtn_3

        main_imgbtn_4 = lv.imgbtn(main)
        main_imgbtn_4.set_pos(27, 281)
        main_imgbtn_4.set_size(45, 44)

        main_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        main_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_4_imgReleased, None, None)
        main_imgbtn_4.set_src(lv.imgbtn.STATE.PRESSED, main_imgbtn_4_imgReleased, None, None)
        main_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, main_imgbtn_4_imgReleased, None, None)
        main_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, main_imgbtn_4_imgReleased, None, None)
        main_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        main_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = main_imgbtn_4

        main_imgbtn_5 = lv.imgbtn(main)
        main_imgbtn_5.set_pos(26, 367)
        main_imgbtn_5.set_size(49, 41)

        main_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        main_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_5_imgReleased, None, None)
        main_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, main_imgbtn_5_imgReleased, None, None)
        main_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, main_imgbtn_5_imgReleased, None, None)
        main_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, main_imgbtn_5_imgReleased, None, None)

        main_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        main_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_2 = lv.obj(main)
        main_cont_2.set_pos(127, 30)
        main_cont_2.set_size(342, 215)
        main_cont_2.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_3 = lv.obj(main)
        main_cont_3.set_pos(488, 30)
        main_cont_3.set_size(342, 215)
        main_cont_3.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_4 = lv.obj(main)
        main_cont_4.set_pos(127, 254)
        main_cont_4.set_size(342, 215)
        main_cont_4.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_5 = lv.obj(main)
        main_cont_5.set_pos(488, 254)
        main_cont_5.set_size(342, 215)
        main_list_1 = lv.list(main_cont_5)
        main_list_1.set_pos(1, 38)
        main_list_1.set_size(334, 135)
        main_list_1_btn_0_img = "U:/img/mp-2033915249.png"
        main_list_1_btn_0 = main_list_1.add_btn(main_list_1_btn_0_img, "Soil moisture is too low !  ----11:30")

        # add style for main_list_1_btn_0
        main_list_1_btn_0.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_list_1_btn_1_img = "U:/img/mp-623834251.png"
        main_list_1_btn_1 = main_list_1.add_btn(main_list_1_btn_1_img, "Lighting 2 low voltage----11:47")

        # add style for main_list_1_btn_1
        main_list_1_btn_1.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_list_1_btn_2_img = "U:/img/mp-2032991728.png"
        main_list_1_btn_2 = main_list_1.add_btn(main_list_1_btn_2_img, "Ambient humidity is too low !  ----11:05")

        # add style for main_list_1_btn_2
        main_list_1_btn_2.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_list_1_btn_3 = main_list_1.add_btn(lv.SYMBOL.SAVE, "")

        # add style for main_list_1_btn_3
        main_list_1_btn_3.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_list_1_btn_4 = main_list_1.add_btn(lv.SYMBOL.MUTE, "")

        # add style for main_list_1_btn_4
        main_list_1_btn_4.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_list_1.add_style(self.style_main_list, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_list_1.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        main_cont_5.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_imgbtn_6 = lv.imgbtn(main)
        main_imgbtn_6.set_pos(26, 415)
        main_imgbtn_6.set_size(49, 41)

        main_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        main_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_6_imgReleased, None, None)
        main_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_6_imgReleased, None, None)
        main_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, main_imgbtn_6_imgReleased, None, None)
        main_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, main_imgbtn_6_imgReleased, None, None)
        main_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        main_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_1 = lv.img(main)
        main_img_1.set_pos(798, 8)
        main_img_1.set_size(20, 15)
        main_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_1_img = "U:/img/mp2146739423.png"

        main_img_1.set_src(main_img_1_img)
        main_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_1 = lv.label(main)
        main_label_1.set_pos(124, 8)
        main_label_1.set_size(76, 13)
        main_label_1.set_text("China Unicom")
        main_label_1.set_long_mode(lv.label.LONG.WRAP)
        main_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_2 = lv.img(main)
        main_img_2.set_pos(764, 9)
        main_img_2.set_size(18, 12)
        main_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_2_img = "U:/img/mp-1849026116.png"

        main_img_2.set_src(main_img_2_img)
        main_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_2 = lv.label(main)
        main_label_2.set_pos(703, 10)
        main_label_2.set_size(50, 13)
        main_label_2.set_text("12:00")
        main_label_2.set_long_mode(lv.label.LONG.WRAP)
        main_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_imgbtn_7 = lv.imgbtn(main)
        main_imgbtn_7.set_pos(133, 349)
        main_imgbtn_7.set_size(23, 31)

        main_imgbtn_7_imgReleased = "U:/img/mp-1881121861.png"
        main_imgbtn_7.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_7_imgReleased, None, None)
        main_imgbtn_7.add_flag(lv.obj.FLAG.CHECKABLE)
        main_imgbtn_7.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_imgbtn_8 = lv.imgbtn(main)
        main_imgbtn_8.set_pos(437, 349)
        main_imgbtn_8.set_size(23, 31)

        main_imgbtn_8_imgReleased = "U:/img/mp-1459476031.png"
        main_imgbtn_8.set_src(lv.imgbtn.STATE.RELEASED, main_imgbtn_8_imgReleased, None, None)
        main_imgbtn_8.add_flag(lv.obj.FLAG.CHECKABLE)
        main_imgbtn_8.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_11 = lv.label(main)
        main_label_11.set_pos(127, 261)
        main_label_11.set_size(76, 17)
        main_label_11.set_text("History curve")
        main_label_11.set_long_mode(lv.label.LONG.WRAP)
        main_label_11.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_11.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_6 = lv.obj(main)
        main_cont_6.set_pos(515, 89)
        main_cont_6.set_size(126, 41)
        main_cont_6.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_8 = lv.obj(main)
        main_cont_8.set_pos(516, 172)
        main_cont_8.set_size(126, 41)
        main_cont_8.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_14 = lv.label(main)
        main_label_14.set_pos(528, 102)
        main_label_14.set_size(100, 32)
        main_label_14.set_text("Soil pH : 7.1")
        main_label_14.set_long_mode(lv.label.LONG.WRAP)
        main_label_14.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_14.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_16 = lv.label(main)
        main_label_16.set_pos(524, 185)
        main_label_16.set_size(109, 24)
        main_label_16.set_text("Soil moisture : 20%")
        main_label_16.set_long_mode(lv.label.LONG.WRAP)
        main_label_16.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_16.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_18 = lv.label(main)
        main_label_18.set_pos(261, 446)
        main_label_18.set_size(76, 17)
        main_label_18.set_text("Temperature")
        main_label_18.set_long_mode(lv.label.LONG.WRAP)
        main_label_18.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_18.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_8 = lv.img(main)
        main_img_8.set_pos(270, 448)
        main_img_8.set_size(10, 10)
        main_img_8.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_8_img = "U:/img/mp-51780172.png"

        main_img_8.set_src(main_img_8_img)
        main_img_8.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_9 = lv.img(main)
        main_img_9.set_pos(353, 52)
        main_img_9.set_size(103, 101)
        main_img_9.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_9_img = "U:/img/mp-1956251486.png"

        main_img_9.set_src(main_img_9_img)
        main_img_9.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_9 = lv.obj(main)
        main_cont_9.set_pos(161, 73)
        main_cont_9.set_size(183, 75)
        main_cont_9.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_10 = lv.obj(main)
        main_cont_10.set_pos(156, 164)
        main_cont_10.set_size(290, 69)
        main_label_25 = lv.label(main_cont_10)
        main_label_25.set_pos(64, 46)
        main_label_25.set_size(48, 17)
        main_label_25.set_text("5/29")
        main_label_25.set_long_mode(lv.label.LONG.WRAP)
        main_label_25.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_25.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_26 = lv.label(main_cont_10)
        main_label_26.set_pos(117, 46)
        main_label_26.set_size(48, 17)
        main_label_26.set_text("5/30")
        main_label_26.set_long_mode(lv.label.LONG.WRAP)
        main_label_26.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_26.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_27 = lv.label(main_cont_10)
        main_label_27.set_pos(177, 46)
        main_label_27.set_size(48, 17)
        main_label_27.set_text("5/31")
        main_label_27.set_long_mode(lv.label.LONG.WRAP)
        main_label_27.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_27.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_28 = lv.label(main_cont_10)
        main_label_28.set_pos(232, 46)
        main_label_28.set_size(48, 17)
        main_label_28.set_text("6/1")
        main_label_28.set_long_mode(lv.label.LONG.WRAP)
        main_label_28.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_28.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_24 = lv.label(main_cont_10)
        main_label_24.set_pos(12, 46)
        main_label_24.set_size(48, 17)
        main_label_24.set_text("5/28")
        main_label_24.set_long_mode(lv.label.LONG.WRAP)
        main_label_24.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_24.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_10 = lv.img(main_cont_10)
        main_img_10.set_pos(16, 8)
        main_img_10.set_size(37, 36)
        main_img_10.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_10_img = "U:/img/mp1501596693.png"

        main_img_10.set_src(main_img_10_img)
        main_img_10.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_11 = lv.img(main_cont_10)
        main_img_11.set_pos(70, 8)
        main_img_11.set_size(37, 36)
        main_img_11.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_11_img = "U:/img/mp399117571.png"

        main_img_11.set_src(main_img_11_img)
        main_img_11.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_12 = lv.img(main_cont_10)
        main_img_12.set_pos(124, 9)
        main_img_12.set_size(37, 36)
        main_img_12.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_12_img = "U:/img/mp399117571.png"

        main_img_12.set_src(main_img_12_img)
        main_img_12.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_13 = lv.img(main_cont_10)
        main_img_13.set_pos(180, 9)
        main_img_13.set_size(37, 36)
        main_img_13.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_13_img = "U:/img/mp1501596693.png"

        main_img_13.set_src(main_img_13_img)
        main_img_13.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_img_14 = lv.img(main_cont_10)
        main_img_14.set_pos(238, 8)
        main_img_14.set_size(37, 36)
        main_img_14.add_flag(lv.obj.FLAG.CLICKABLE)

        main_img_14_img = "U:/img/mp399117571.png"

        main_img_14.set_src(main_img_14_img)
        main_img_14.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_10.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_20 = lv.label(main)
        main_label_20.set_pos(168, 99)
        main_label_20.set_size(62, 19)
        main_label_20.set_text("27°C")
        main_label_20.set_long_mode(lv.label.LONG.WRAP)
        main_label_20.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_20.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_21 = lv.label(main)
        main_label_21.set_pos(166, 80)
        main_label_21.set_size(64, 12)
        main_label_21.set_text("Hefei City")
        main_label_21.set_long_mode(lv.label.LONG.WRAP)
        main_label_21.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_21.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_22 = lv.label(main)
        main_label_22.set_pos(275, 101)
        main_label_22.set_size(64, 12)
        main_label_22.set_text("Cloudy")
        main_label_22.set_long_mode(lv.label.LONG.WRAP)
        main_label_22.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_22.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_23 = lv.label(main)
        main_label_23.set_pos(266, 122)
        main_label_23.set_size(75, 13)
        main_label_23.set_text("21°C-31°C")
        main_label_23.set_long_mode(lv.label.LONG.WRAP)
        main_label_23.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_23.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_chart_1 = lv.chart(main)
        main_chart_1.set_pos(173, 285)
        main_chart_1.set_size(252, 146)
        main_chart_1.set_type(lv.chart.TYPE.LINE)
        main_chart_1.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 100)
        main_chart_1.set_div_line_count(3, 5)
        main_chart_1.set_point_count(5)
        chart_series_0 = lv.chart.add_series(main_chart_1, lv.color_make(0xc9, 0x2c, 0x2c), lv.chart.AXIS.PRIMARY_Y);
        main_chart_1.set_next_value(chart_series_0, 10)
        main_chart_1.set_next_value(chart_series_0, 23)
        main_chart_1.set_next_value(chart_series_0, 25)
        main_chart_1.set_next_value(chart_series_0, 40)
        main_chart_1.set_next_value(chart_series_0, 15)
        # create style style_main_chart_1_main_main_default
        style_main_chart_1_main_main_default = lv.style_t()
        style_main_chart_1_main_main_default.init()
        style_main_chart_1_main_main_default.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_main_chart_1_main_main_default.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_main_chart_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_main_chart_1_main_main_default.set_bg_opa(34)
        style_main_chart_1_main_main_default.set_pad_left(5)
        style_main_chart_1_main_main_default.set_pad_right(5)
        style_main_chart_1_main_main_default.set_pad_top(5)
        style_main_chart_1_main_main_default.set_pad_bottom(5)
        style_main_chart_1_main_main_default.set_line_color(lv.color_make(0xc6, 0xbe, 0xbe))
        style_main_chart_1_main_main_default.set_line_width(2)
        style_main_chart_1_main_main_default.set_line_opa(255)

        # add style for main_chart_1
        main_chart_1.add_style(style_main_chart_1_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_btn_1 = lv.btn(main)
        main_btn_1.set_pos(125, 25)
        main_btn_1.set_size(100, 50)
        self.weather_btn = main_btn_1
        main_btn_1_label = lv.label(main_btn_1)
        main_btn_1_label.set_text("Weather")
        main_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
        main_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
        main_btn_1_label.set_style_text_color(lv.color_make(0xf7, 0xf7, 0xf7), lv.STATE.DEFAULT)
        main_btn_1_label.set_style_text_font(lv.font_siyuan_Regular_14, lv.STATE.DEFAULT)
        main_btn_1.add_style(self.style_opa_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_btn_2 = lv.btn(main)
        main_btn_2.set_pos(492, 27)
        main_btn_2.set_size(100, 50)
        self.monitor_btn = main_btn_2
        main_btn_2_label = lv.label(main_btn_2)
        main_btn_2_label.set_text("Environment parameters")
        main_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
        main_btn_2_label.align(lv.ALIGN.CENTER, 0, 0)
        main_btn_2_label.set_style_text_color(lv.color_make(0xf7, 0xf7, 0xf7), lv.STATE.DEFAULT)
        main_btn_2_label.set_style_text_font(lv.font_siyuan_Regular_14, lv.STATE.DEFAULT)
        main_btn_2.add_style(self.style_opa_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_btn_3 = lv.btn(main)
        main_btn_3.set_pos(486, 246)
        main_btn_3.set_size(100, 50)
        self.alarm_btn = main_btn_3
        main_btn_3_label = lv.label(main_btn_3)
        main_btn_3_label.set_text("Warning message")
        main_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
        main_btn_3_label.align(lv.ALIGN.CENTER, 0, 0)
        main_btn_3_label.set_style_text_color(lv.color_make(0xf7, 0xf7, 0xf7), lv.STATE.DEFAULT)
        main_btn_3_label.set_style_text_font(lv.font_siyuan_Regular_14, lv.STATE.DEFAULT)
        main_btn_3.add_style(self.style_opa_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_11 = lv.obj(main)
        main_cont_11.set_pos(672, 89)
        main_cont_11.set_size(126, 41)
        main_cont_11.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_cont_12 = lv.obj(main)
        main_cont_12.set_pos(672, 172)
        main_cont_12.set_size(126, 41)
        main_cont_12.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_3 = lv.label(main)
        main_label_3.set_pos(672, 186)
        main_label_3.set_size(128, 21)
        main_label_3.set_text("Temperature : 23°C")
        main_label_3.set_long_mode(lv.label.LONG.WRAP)
        main_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_3.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        main_label_6 = lv.label(main)
        main_label_6.set_pos(672, 102)
        main_label_6.set_size(126, 24)
        main_label_6.set_text("Oxygen concentration : 50%")
        main_label_6.set_long_mode(lv.label.LONG.WRAP)
        main_label_6.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        main_label_6.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.weather_btn.add_event_cb(lambda e: self.__weather_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.alarm_btn.add_event_cb(lambda e: self.__alarm_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn_2.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)

    def __weather_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "WeatherScreen")

    def __monitor_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "MonitorScreen")

    def __alarm_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "AlarmScreen")

    def __dev_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "Dev1Screen")

    def __setting_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("Click event occurs")
        EventMesh.publish("load_screen", "SettingScreen")