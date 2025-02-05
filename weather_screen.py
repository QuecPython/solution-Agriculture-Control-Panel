import lvgl as lv
from usr.screen import Screen
from usr import EventMesh


class WeatherScreen(Screen):
    def __init__(self):
        super().__init__()
        self.dev_btn = None
        self.setting_btn = None
        self.monitor_btn = None
        self.home_btn = None
        self.screen = None
        self.name = "WeatherScreen"
        super().create_style()

    def create(self):
        weather = lv.obj()
        self.screen = weather
        # create style style_weather_main_main_default
        style_weather_main_main_default = lv.style_t()
        style_weather_main_main_default.init()
        style_weather_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_weather_main_main_default.set_bg_opa(255)

        # add style for weather
        weather.add_style(style_weather_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_cont_1 = lv.obj(weather)
        weather_cont_1.set_pos(0, 0)
        weather_cont_1.set_size(100, 480)
        weather_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_imgbtn_1 = lv.imgbtn(weather)
        weather_imgbtn_1.set_pos(23, 22)
        weather_imgbtn_1.set_size(54, 57)

        weather_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        weather_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_1_imgReleased, None, None)
        weather_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_1_imgReleased, None, None)
        weather_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, weather_imgbtn_1_imgReleased, None, None)
        weather_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, weather_imgbtn_1_imgReleased, None, None)

        weather_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        weather_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = weather_imgbtn_1

        weather_imgbtn_2 = lv.imgbtn(weather)
        weather_imgbtn_2.set_pos(27, 127)
        weather_imgbtn_2.set_size(45, 44)

        weather_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        weather_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_2_imgReleased, None, None)
        weather_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_2_imgReleased, None, None)
        weather_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, weather_imgbtn_2_imgReleased, None, None)
        weather_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, weather_imgbtn_2_imgReleased, None, None)
        weather_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        weather_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = weather_imgbtn_2

        weather_imgbtn_3 = lv.imgbtn(weather)
        weather_imgbtn_3.set_pos(27, 202)
        weather_imgbtn_3.set_size(45, 44)

        weather_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        weather_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_3_imgReleased, None, None)
        weather_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_3_imgReleased, None, None)
        weather_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, weather_imgbtn_3_imgReleased, None, None)
        weather_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, weather_imgbtn_3_imgReleased, None, None)
        weather_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        weather_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = weather_imgbtn_3

        weather_imgbtn_4 = lv.imgbtn(weather)
        weather_imgbtn_4.set_pos(27, 281)
        weather_imgbtn_4.set_size(45, 44)

        weather_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        weather_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_4_imgReleased, None, None)
        weather_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_4_imgReleased, None, None)
        weather_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, weather_imgbtn_4_imgReleased, None, None)
        weather_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, weather_imgbtn_4_imgReleased, None, None)
        weather_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        weather_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = weather_imgbtn_4

        weather_imgbtn_5 = lv.imgbtn(weather)
        weather_imgbtn_5.set_pos(26, 367)
        weather_imgbtn_5.set_size(49, 41)

        weather_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        weather_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_5_imgReleased, None, None)
        weather_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, weather_imgbtn_5_imgReleased, None, None)
        weather_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, weather_imgbtn_5_imgReleased, None, None)
        weather_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, weather_imgbtn_5_imgReleased, None, None)

        weather_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        weather_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_imgbtn_6 = lv.imgbtn(weather)
        weather_imgbtn_6.set_pos(26, 415)
        weather_imgbtn_6.set_size(49, 41)

        weather_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        weather_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, weather_imgbtn_6_imgReleased, None, None)
        weather_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, weather_imgbtn_6_imgReleased, None, None)
        weather_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, weather_imgbtn_6_imgReleased, None, None)
        weather_imgbtn_6.set_src(lv.imgbtn.STATE.PRESSED, weather_imgbtn_6_imgReleased, None, None)

        weather_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        weather_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_1 = lv.img(weather)
        weather_img_1.set_pos(798, 8)
        weather_img_1.set_size(20, 15)
        weather_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_1_img = "U:/img/mp2146739423.png"

        weather_img_1.set_src(weather_img_1_img)
        weather_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_1 = lv.label(weather)
        weather_label_1.set_pos(124, 8)
        weather_label_1.set_size(76, 13)
        weather_label_1.set_text("Union")
        weather_label_1.set_long_mode(lv.label.LONG.WRAP)
        weather_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_2 = lv.img(weather)
        weather_img_2.set_pos(764, 9)
        weather_img_2.set_size(18, 12)
        weather_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_2_img = "U:/img/mp-1849026116.png"

        weather_img_2.set_src(weather_img_2_img)
        weather_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_2 = lv.label(weather)
        weather_label_2.set_pos(703, 10)
        weather_label_2.set_size(50, 13)
        weather_label_2.set_text("12:00")
        weather_label_2.set_long_mode(lv.label.LONG.WRAP)
        weather_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_tileview_2 = lv.tileview(weather)
        weather_tileview_2.set_pos(100, 28)
        weather_tileview_2.set_size(754, 452)
        weather_tileview_2_tileview = weather_tileview_2.add_tile(0, 0, lv.DIR.RIGHT)
        weather_tileview_2_Title = weather_tileview_2.add_tile(1, 0, lv.DIR.LEFT)
        weather_tileview_2.add_style(self.style_tileview, lv.PART.MAIN | lv.STATE.DEFAULT)
        weather_tileview_2.add_style(self.style_tileview_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        weather_img_3 = lv.img(weather)
        weather_img_3.set_pos(60, 166)
        weather_img_3.set_size(16, 14)
        weather_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_3_img = "U:/img/mp-347592130.png"

        weather_img_3.set_src(weather_img_3_img)
        weather_img_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_cont_2 = lv.obj(weather)
        weather_cont_2.set_pos(167, 113)
        weather_cont_2.set_size(221, 163)
        weather_cont_2.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_cont_3 = lv.obj(weather)
        weather_cont_3.set_pos(415, 113)
        weather_cont_3.set_size(401, 328)
        weather_cont_3.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_7 = lv.label(weather)
        weather_label_7.set_pos(443, 218)
        weather_label_7.set_size(95, 17)
        weather_label_7.set_text("05/29")
        weather_label_7.set_long_mode(lv.label.LONG.WRAP)
        weather_label_7.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_7.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_line_5 = lv.line(weather)
        weather_line_5.set_pos(0, 0)
        weather_line_5.set_size(830, 460)
        line_points = [
            {"x": 455, "y": 400},
            {"x": 760, "y": 400},
        ]
        weather_line_5.set_points(line_points, 2)
        # create style style_weather_line_5_main_main_default
        style_weather_line_5_main_main_default = lv.style_t()
        style_weather_line_5_main_main_default.init()
        style_weather_line_5_main_main_default.set_line_color(lv.color_make(0xf2, 0xf2, 0xf2))
        style_weather_line_5_main_main_default.set_line_width(1)
        style_weather_line_5_main_main_default.set_line_rounded(255)

        # add style for weather_line_5
        weather_line_5.add_style(style_weather_line_5_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_8 = lv.label(weather)
        weather_label_8.set_pos(457, 168)
        weather_label_8.set_size(67, 17)
        weather_label_8.set_text("05/28")
        weather_label_8.set_long_mode(lv.label.LONG.WRAP)
        weather_label_8.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_8.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_line_2 = lv.line(weather)
        weather_line_2.set_pos(0, 0)
        weather_line_2.set_size(830, 460)
        line_points = [
            {"x": 455, "y": 250},
            {"x": 760, "y": 250},
        ]
        weather_line_2.set_points(line_points, 2)
        # create style style_weather_line_2_main_main_default
        style_weather_line_2_main_main_default = lv.style_t()
        style_weather_line_2_main_main_default.init()
        style_weather_line_2_main_main_default.set_line_color(lv.color_make(0xf2, 0xf2, 0xf2))
        style_weather_line_2_main_main_default.set_line_width(1)
        style_weather_line_2_main_main_default.set_line_rounded(255)

        # add style for weather_line_2
        weather_line_2.add_style(style_weather_line_2_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_line_3 = lv.line(weather)
        weather_line_3.set_pos(0, 0)
        weather_line_3.set_size(830, 460)
        line_points = [
            {"x": 455, "y": 300},
            {"x": 760, "y": 300},
        ]
        weather_line_3.set_points(line_points, 2)
        # create style style_weather_line_3_main_main_default
        style_weather_line_3_main_main_default = lv.style_t()
        style_weather_line_3_main_main_default.init()
        style_weather_line_3_main_main_default.set_line_color(lv.color_make(0xf2, 0xf2, 0xf2))
        style_weather_line_3_main_main_default.set_line_width(1)
        style_weather_line_3_main_main_default.set_line_rounded(255)

        # add style for weather_line_3
        weather_line_3.add_style(style_weather_line_3_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_9 = lv.label(weather)
        weather_label_9.set_pos(288, 98)
        weather_label_9.set_size(100, 32)
        weather_label_9.set_text("27°C")
        weather_label_9.set_long_mode(lv.label.LONG.WRAP)
        weather_label_9.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_9.add_style(self.style_siyuan_26, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_cont_4 = lv.obj(weather)
        weather_cont_4.set_pos(166, 300)
        weather_cont_4.set_size(221, 141)
        weather_label_1_9 = lv.label(weather_cont_4)
        weather_label_1_9.set_pos(105, 42)
        weather_label_1_9.set_size(98, 18)
        weather_label_1_9.set_text("Northeast")#东北风
        weather_label_1_9.set_long_mode(lv.label.LONG.WRAP)
        weather_label_1_9.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_1_9.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_2_9 = lv.label(weather_cont_4)
        weather_label_2_9.set_pos(105, 82)
        weather_label_2_9.set_size(98, 18)
        weather_label_2_9.set_text("3 level")
        weather_label_2_9.set_long_mode(lv.label.LONG.WRAP)
        weather_label_2_9.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_2_9.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_cont_4.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_4 = lv.img(weather)
        weather_img_4.set_pos(182, 58)
        weather_img_4.set_size(100, 100)
        weather_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_4_img = "U:/img/mp404464238.png"

        weather_img_4.set_src(weather_img_4_img)
        weather_img_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_10 = lv.label(weather)
        weather_label_10.set_pos(230, 193)
        weather_label_10.set_size(100, 22)
        weather_label_10.set_text("Cloudy")
        weather_label_10.set_long_mode(lv.label.LONG.WRAP)
        weather_label_10.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_10.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_11 = lv.label(weather)
        weather_label_11.set_pos(231, 160)
        weather_label_11.set_size(100, 22)
        weather_label_11.set_text("HeFei")
        weather_label_11.set_long_mode(lv.label.LONG.WRAP)
        weather_label_11.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_11.add_style(self.style_siyuan_20, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_line_4 = lv.line(weather)
        weather_line_4.set_pos(0, 0)
        weather_line_4.set_size(830, 460)
        line_points = [
            {"x": 455, "y": 350},
            {"x": 760, "y": 350},
        ]
        weather_line_4.set_points(line_points, 2)
        # create style style_weather_line_4_main_main_default
        style_weather_line_4_main_main_default = lv.style_t()
        style_weather_line_4_main_main_default.init()
        style_weather_line_4_main_main_default.set_line_color(lv.color_make(0xf2, 0xf2, 0xf2))
        style_weather_line_4_main_main_default.set_line_width(1)
        style_weather_line_4_main_main_default.set_line_rounded(255)

        # add style for weather_line_4
        weather_line_4.add_style(style_weather_line_4_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_12 = lv.label(weather)
        weather_label_12.set_pos(176, 226)
        weather_label_12.set_size(207, 22)
        weather_label_12.set_text("Max32°C  Min22°C")
        weather_label_12.set_long_mode(lv.label.LONG.WRAP)
        weather_label_12.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_12.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_line_1 = lv.line(weather)
        weather_line_1.set_pos(0, 0)
        weather_line_1.set_size(830, 460)
        line_points = [
            {"x": 455, "y": 200},
            {"x": 760, "y": 200},
        ]
        weather_line_1.set_points(line_points, 2)
        # create style style_weather_line_1_main_main_default
        style_weather_line_1_main_main_default = lv.style_t()
        style_weather_line_1_main_main_default.init()
        style_weather_line_1_main_main_default.set_line_color(lv.color_make(0xf2, 0xf2, 0xf2))
        style_weather_line_1_main_main_default.set_line_width(1)
        style_weather_line_1_main_main_default.set_line_rounded(255)

        # add style for weather_line_1
        weather_line_1.add_style(style_weather_line_1_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_5 = lv.img(weather)
        weather_img_5.set_pos(207, 341)
        weather_img_5.set_size(50, 50)
        weather_img_5.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_5_img = "U:/img/mp319674000.png"

        weather_img_5.set_src(weather_img_5_img)
        weather_img_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_13 = lv.label(weather)
        weather_label_13.set_pos(444, 268)
        weather_label_13.set_size(95, 17)
        weather_label_13.set_text("05/30")
        weather_label_13.set_long_mode(lv.label.LONG.WRAP)
        weather_label_13.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_13.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_14 = lv.label(weather)
        weather_label_14.set_pos(445, 318)
        weather_label_14.set_size(95, 17)
        weather_label_14.set_text("05/31")
        weather_label_14.set_long_mode(lv.label.LONG.WRAP)
        weather_label_14.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_14.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_15 = lv.label(weather)
        weather_label_15.set_pos(446, 368)
        weather_label_15.set_size(95, 17)
        weather_label_15.set_text("05/31")
        weather_label_15.set_long_mode(lv.label.LONG.WRAP)
        weather_label_15.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_15.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_6 = lv.img(weather)
        weather_img_6.set_pos(545, 159)
        weather_img_6.set_size(30, 29)
        weather_img_6.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_6_img = "U:/img/mp-415000654.png"

        weather_img_6.set_src(weather_img_6_img)
        weather_img_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_7 = lv.img(weather)
        weather_img_7.set_pos(546, 208)
        weather_img_7.set_size(30, 29)
        weather_img_7.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_7_img = "U:/img/mp-672201496.png"

        weather_img_7.set_src(weather_img_7_img)
        weather_img_7.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_8 = lv.img(weather)
        weather_img_8.set_pos(548, 261)
        weather_img_8.set_size(30, 29)
        weather_img_8.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_8_img = "U:/img/mp-672201496.png"

        weather_img_8.set_src(weather_img_8_img)
        weather_img_8.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_9 = lv.img(weather)
        weather_img_9.set_pos(549, 310)
        weather_img_9.set_size(30, 28)
        weather_img_9.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_9_img = "U:/img/mp1424177823.png"

        weather_img_9.set_src(weather_img_9_img)
        weather_img_9.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_img_10 = lv.img(weather)
        weather_img_10.set_pos(550, 362)
        weather_img_10.set_size(30, 28)
        weather_img_10.add_flag(lv.obj.FLAG.CLICKABLE)

        weather_img_10_img = "U:/img/mp-1113916345.png"

        weather_img_10.set_src(weather_img_10_img)
        weather_img_10.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_16 = lv.label(weather)
        weather_label_16.set_pos(591, 169)
        weather_label_16.set_size(79, 17)
        weather_label_16.set_text("cloudy")#阴天
        weather_label_16.set_long_mode(lv.label.LONG.WRAP)
        weather_label_16.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_16.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_17 = lv.label(weather)
        weather_label_17.set_pos(671, 169)
        weather_label_17.set_size(93, 17)
        weather_label_17.set_text("22°C~30°C")
        weather_label_17.set_long_mode(lv.label.LONG.WRAP)
        weather_label_17.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_17.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_18 = lv.label(weather)
        weather_label_18.set_pos(672, 219)
        weather_label_18.set_size(93, 17)
        weather_label_18.set_text("22°C~30°C")
        weather_label_18.set_long_mode(lv.label.LONG.WRAP)
        weather_label_18.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_18.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_19 = lv.label(weather)
        weather_label_19.set_pos(674, 270)
        weather_label_19.set_size(93, 17)
        weather_label_19.set_text("22°C~30°C")
        weather_label_19.set_long_mode(lv.label.LONG.WRAP)
        weather_label_19.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_19.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_20 = lv.label(weather)
        weather_label_20.set_pos(674, 318)
        weather_label_20.set_size(93, 17)
        weather_label_20.set_text("22°C~30°C")
        weather_label_20.set_long_mode(lv.label.LONG.WRAP)
        weather_label_20.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_20.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_21 = lv.label(weather)
        weather_label_21.set_pos(676, 367)
        weather_label_21.set_size(93, 17)
        weather_label_21.set_text("22°C~30°C")
        weather_label_21.set_long_mode(lv.label.LONG.WRAP)
        weather_label_21.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_21.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_22 = lv.label(weather)
        weather_label_22.set_pos(592, 218)
        weather_label_22.set_size(79, 17)
        weather_label_22.set_text("rain")#雨
        weather_label_22.set_long_mode(lv.label.LONG.WRAP)
        weather_label_22.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_22.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_23 = lv.label(weather)
        weather_label_23.set_pos(592, 269)
        weather_label_23.set_size(79, 17)
        weather_label_23.set_text("rain")#雨
        weather_label_23.set_long_mode(lv.label.LONG.WRAP)
        weather_label_23.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_23.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_24 = lv.label(weather)
        weather_label_24.set_pos(594, 317)
        weather_label_24.set_size(79, 17)
        weather_label_24.set_text("sunny")#晴天
        weather_label_24.set_long_mode(lv.label.LONG.WRAP)
        weather_label_24.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_24.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        weather_label_25 = lv.label(weather)
        weather_label_25.set_pos(594, 369)
        weather_label_25.set_size(79, 17)
        weather_label_25.set_text("cloudy")#多云
        weather_label_25.set_long_mode(lv.label.LONG.WRAP)
        weather_label_25.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        weather_label_25.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)

    def __home_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "MainScreen")

    def __monitor_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "MonitorScreen")

    def __dev_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "Dev1Screen")

    def __setting_btn_event_cb(self,e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "SettingScreen")