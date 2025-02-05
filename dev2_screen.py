import lvgl as lv
from usr.screen import Screen
from usr import EventMesh

class Dev2Screen(Screen):
    def __init__(self):
        super().__init__()
        self.dev_btn = None
        self.setting_btn = None
        self.monitor_btn = None
        self.home_btn = None
        self.screen = None
        self.name = "Dev2Screen"
        super().create_style()

    def create(self):
        dev_ctrl2 = lv.obj()
        self.screen = dev_ctrl2
        # create style style_dev_ctrl2_main_main_default
        style_dev_ctrl2_main_main_default = lv.style_t()
        style_dev_ctrl2_main_main_default.init()
        style_dev_ctrl2_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_dev_ctrl2_main_main_default.set_bg_opa(255)

        # add style for dev_ctrl2
        dev_ctrl2.add_style(style_dev_ctrl2_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_cont_1 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_1.set_pos(0, 0)
        dev_ctrl2_cont_1.set_size(100, 480)
        dev_ctrl2_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_imgbtn_1 = lv.imgbtn(dev_ctrl2)
        dev_ctrl2_imgbtn_1.set_pos(23, 22)
        dev_ctrl2_imgbtn_1.set_size(54, 57)

        dev_ctrl2_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        dev_ctrl2_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl2_imgbtn_1_imgReleased, None, None)
        dev_ctrl2_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl2_imgbtn_1_imgReleased, None, None)
        dev_ctrl2_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl2_imgbtn_1_imgReleased, None, None)
        dev_ctrl2_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl2_imgbtn_1_imgReleased, None, None)
        dev_ctrl2_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl2_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = dev_ctrl2_imgbtn_1

        dev_ctrl2_imgbtn_2 = lv.imgbtn(dev_ctrl2)
        dev_ctrl2_imgbtn_2.set_pos(27, 127)
        dev_ctrl2_imgbtn_2.set_size(45, 44)

        dev_ctrl2_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        dev_ctrl2_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl2_imgbtn_2_imgReleased, None, None)
        dev_ctrl2_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl2_imgbtn_2_imgReleased, None, None)
        dev_ctrl2_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl2_imgbtn_2_imgReleased, None, None)
        dev_ctrl2_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl2_imgbtn_2_imgReleased, None, None)
        dev_ctrl2_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl2_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = dev_ctrl2_imgbtn_2

        dev_ctrl2_imgbtn_3 = lv.imgbtn(dev_ctrl2)
        dev_ctrl2_imgbtn_3.set_pos(27, 202)
        dev_ctrl2_imgbtn_3.set_size(45, 44)

        dev_ctrl2_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        dev_ctrl2_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl2_imgbtn_3_imgReleased, None, None)
        dev_ctrl2_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl2_imgbtn_3_imgReleased, None, None)
        dev_ctrl2_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl2_imgbtn_3_imgReleased, None, None)
        dev_ctrl2_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl2_imgbtn_3_imgReleased, None, None)
        dev_ctrl2_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl2_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = dev_ctrl2_imgbtn_3

        dev_ctrl2_imgbtn_4 = lv.imgbtn(dev_ctrl2)
        dev_ctrl2_imgbtn_4.set_pos(27, 281)
        dev_ctrl2_imgbtn_4.set_size(45, 44)

        dev_ctrl2_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        dev_ctrl2_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl2_imgbtn_4_imgReleased, None, None)
        dev_ctrl2_imgbtn_4.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl2_imgbtn_4_imgReleased, None, None)
        dev_ctrl2_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl2_imgbtn_4_imgReleased, None, None)
        dev_ctrl2_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl2_imgbtn_4_imgReleased, None, None)

        dev_ctrl2_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl2_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = dev_ctrl2_imgbtn_4

        dev_ctrl2_imgbtn_5 = lv.imgbtn(dev_ctrl2)
        dev_ctrl2_imgbtn_5.set_pos(26, 367)
        dev_ctrl2_imgbtn_5.set_size(49, 41)

        dev_ctrl2_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        dev_ctrl2_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl2_imgbtn_5_imgReleased, None, None)
        dev_ctrl2_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl2_imgbtn_5_imgReleased, None, None)
        dev_ctrl2_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl2_imgbtn_5_imgReleased, None, None)
        dev_ctrl2_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl2_imgbtn_5_imgReleased, None, None)

        dev_ctrl2_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl2_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_imgbtn_6 = lv.imgbtn(dev_ctrl2)
        dev_ctrl2_imgbtn_6.set_pos(26, 415)
        dev_ctrl2_imgbtn_6.set_size(49, 41)

        dev_ctrl2_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        dev_ctrl2_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl2_imgbtn_6_imgReleased, None, None)
        dev_ctrl2_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl2_imgbtn_6_imgReleased, None, None)
        dev_ctrl2_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl2_imgbtn_6_imgReleased, None, None)
        dev_ctrl2_imgbtn_6.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl2_imgbtn_6_imgReleased, None, None)
        dev_ctrl2_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl2_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_1 = lv.img(dev_ctrl2)
        dev_ctrl2_img_1.set_pos(798, 8)
        dev_ctrl2_img_1.set_size(20, 15)
        dev_ctrl2_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_1_img = "U:/img/mp2146739423.png"

        dev_ctrl2_img_1.set_src(dev_ctrl2_img_1_img)
        dev_ctrl2_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_1 = lv.label(dev_ctrl2)
        dev_ctrl2_label_1.set_pos(124, 8)
        dev_ctrl2_label_1.set_size(76, 13)
        dev_ctrl2_label_1.set_text("Union")
        dev_ctrl2_label_1.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_2 = lv.img(dev_ctrl2)
        dev_ctrl2_img_2.set_pos(764, 9)
        dev_ctrl2_img_2.set_size(18, 12)
        dev_ctrl2_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_2_img = "U:/img/mp-1849026116.png"

        dev_ctrl2_img_2.set_src(dev_ctrl2_img_2_img)
        dev_ctrl2_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_2 = lv.label(dev_ctrl2)
        dev_ctrl2_label_2.set_pos(703, 10)
        dev_ctrl2_label_2.set_size(50, 13)
        dev_ctrl2_label_2.set_text("12:00")
        dev_ctrl2_label_2.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_tileview_1 = lv.tileview(dev_ctrl2)
        dev_ctrl2_tileview_1.set_pos(234, 60)
        dev_ctrl2_tileview_1.set_size(620, 419)
        dev_ctrl2_tileview_1_tileview = dev_ctrl2_tileview_1.add_tile(0, 0, lv.DIR.RIGHT)
        dev_ctrl2_tileview_1_Title = dev_ctrl2_tileview_1.add_tile(1, 0, lv.DIR.LEFT)
        dev_ctrl2_tileview_1.add_style(self.style_tileview, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl2_tileview_1.add_style(self.style_tileview_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        dev_ctrl2_cont_13 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_13.set_pos(294, 90)
        dev_ctrl2_cont_13.set_size(212, 101)
        dev_ctrl2_cont_13.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_cont_11 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_11.set_pos(577, 223)
        dev_ctrl2_cont_11.set_size(215, 101)
        dev_ctrl2_cont_11.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_cont_12 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_12.set_pos(582, 352)
        dev_ctrl2_cont_12.set_size(210, 101)
        dev_ctrl2_cont_12.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_cont_14 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_14.set_pos(294, 224)
        dev_ctrl2_cont_14.set_size(212, 101)
        dev_ctrl2_cont_14.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_cont_15 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_15.set_pos(294, 352)
        dev_ctrl2_cont_15.set_size(212, 101)
        dev_ctrl2_cont_15.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_cont_10 = lv.obj(dev_ctrl2)
        dev_ctrl2_cont_10.set_pos(575, 90)
        dev_ctrl2_cont_10.set_size(212, 101)
        dev_ctrl2_cont_10.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_32 = lv.label(dev_ctrl2)
        dev_ctrl2_label_32.set_pos(384, 100)
        dev_ctrl2_label_32.set_size(89, 17)
        dev_ctrl2_label_32.set_text("Ventilation")
        dev_ctrl2_label_32.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_32.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_32.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_33 = lv.label(dev_ctrl2)
        dev_ctrl2_label_33.set_pos(660, 101)
        dev_ctrl2_label_33.set_size(89, 17)
        dev_ctrl2_label_33.set_text("Irrigator")
        dev_ctrl2_label_33.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_33.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_33.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_35 = lv.label(dev_ctrl2)
        dev_ctrl2_label_35.set_pos(378, 235)
        dev_ctrl2_label_35.set_size(101, 17)
        dev_ctrl2_label_35.set_text("Humidifying")
        dev_ctrl2_label_35.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_35.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_35.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_36 = lv.label(dev_ctrl2)
        dev_ctrl2_label_36.set_pos(655, 235)
        dev_ctrl2_label_36.set_size(101, 17)
        dev_ctrl2_label_36.set_text("Insect repellent")
        dev_ctrl2_label_36.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_36.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_36.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_38 = lv.label(dev_ctrl2)
        dev_ctrl2_label_38.set_pos(384, 365)
        dev_ctrl2_label_38.set_size(85, 17)
        dev_ctrl2_label_38.set_text("Heating")
        dev_ctrl2_label_38.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_38.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_38.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_39 = lv.label(dev_ctrl2)
        dev_ctrl2_label_39.set_pos(661, 365)
        dev_ctrl2_label_39.set_size(94, 17)
        dev_ctrl2_label_39.set_text("Alarm")
        dev_ctrl2_label_39.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_39.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl2_label_39.add_style(self.style_siyuan_16, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_3 = lv.img(dev_ctrl2)
        dev_ctrl2_img_3.set_pos(317, 125)
        dev_ctrl2_img_3.set_size(32, 32)
        dev_ctrl2_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_3_img = "U:/img/mp-1466630811.png"

        dev_ctrl2_img_3.set_src(dev_ctrl2_img_3_img)
        dev_ctrl2_img_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_4 = lv.img(dev_ctrl2)
        dev_ctrl2_img_4.set_pos(598, 122)
        dev_ctrl2_img_4.set_size(37, 37)
        dev_ctrl2_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_4_img = "U:/img/mp1849614543.png"

        dev_ctrl2_img_4.set_src(dev_ctrl2_img_4_img)
        dev_ctrl2_img_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_6 = lv.img(dev_ctrl2)
        dev_ctrl2_img_6.set_pos(315, 256)
        dev_ctrl2_img_6.set_size(35, 36)
        dev_ctrl2_img_6.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_6_img = "U:/img/mp910426373.png"

        dev_ctrl2_img_6.set_src(dev_ctrl2_img_6_img)
        dev_ctrl2_img_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_7 = lv.img(dev_ctrl2)
        dev_ctrl2_img_7.set_pos(599, 257)
        dev_ctrl2_img_7.set_size(37, 37)
        dev_ctrl2_img_7.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_7_img = "U:/img/mp-36862517.png"

        dev_ctrl2_img_7.set_src(dev_ctrl2_img_7_img)
        dev_ctrl2_img_7.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_9 = lv.img(dev_ctrl2)
        dev_ctrl2_img_9.set_pos(316, 382)
        dev_ctrl2_img_9.set_size(37, 37)
        dev_ctrl2_img_9.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_9_img = "U:/img/mp575079848.png"

        dev_ctrl2_img_9.set_src(dev_ctrl2_img_9_img)
        dev_ctrl2_img_9.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_10 = lv.img(dev_ctrl2)
        dev_ctrl2_img_10.set_pos(608, 391)
        dev_ctrl2_img_10.set_size(30, 30)
        dev_ctrl2_img_10.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_10_img = "U:/img/mp-1474147909.png"

        dev_ctrl2_img_10.set_src(dev_ctrl2_img_10_img)
        dev_ctrl2_img_10.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_img_4 = lv.img(dev_ctrl2)
        dev_ctrl2_img_4.set_pos(60, 320)
        dev_ctrl2_img_4.set_size(16, 14)
        dev_ctrl2_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl2_img_4_img = "U:/img/mp-347592130.png"

        dev_ctrl2_img_4.set_src(dev_ctrl2_img_4_img)
        dev_ctrl2_img_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_slider_1 = lv.slider(dev_ctrl2)
        dev_ctrl2_slider_1.set_pos(379, 165)
        dev_ctrl2_slider_1.set_size(101, 10)
        dev_ctrl2_slider_1.set_range(0, 100)
        dev_ctrl2_slider_1.set_value(50, False)

        dev_ctrl2_slider_1.add_style(self.style_slider, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl2_slider_1.add_style(self.style_slider_indicator, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        dev_ctrl2_slider_1.add_style(self.style_slider_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        dev_ctrl2_slider_1.set_ext_click_area(10)

        self.dev_ctrl2_sw_1 = lv.switch(dev_ctrl2)
        self.dev_ctrl2_sw_1.set_pos(429, 130)
        self.dev_ctrl2_sw_1.set_size(39, 16)
        self.dev_ctrl2_sw_1.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_1.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        self.dev_ctrl2_sw_1.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_1.add_state(lv.STATE.CHECKED)
        self.dev_ctrl2_sw_1.set_ext_click_area(10)

        dev_ctrl2_label_40 = lv.label(dev_ctrl2)
        dev_ctrl2_label_40.set_pos(369, 132)
        dev_ctrl2_label_40.set_size(50, 16)
        dev_ctrl2_label_40.set_text("on-off")
        dev_ctrl2_label_40.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_40.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        # dev_ctrl2_label_40.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)


        dev_ctrl2_label_41 = lv.label(dev_ctrl2)
        dev_ctrl2_label_41.set_pos(652, 131)
        dev_ctrl2_label_41.set_size(50, 16)
        dev_ctrl2_label_41.set_text("on-off")
        dev_ctrl2_label_41.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_41.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        # dev_ctrl2_label_41.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_42 = lv.label(dev_ctrl2)
        dev_ctrl2_label_42.set_pos(371, 268)
        dev_ctrl2_label_42.set_size(50, 16)
        dev_ctrl2_label_42.set_text("on-off")
        dev_ctrl2_label_42.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_42.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        # dev_ctrl2_label_42.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_43 = lv.label(dev_ctrl2)
        dev_ctrl2_label_43.set_pos(653, 266)
        dev_ctrl2_label_43.set_size(50, 16)
        dev_ctrl2_label_43.set_text("on-off")
        dev_ctrl2_label_43.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_43.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        # dev_ctrl2_label_43.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_44 = lv.label(dev_ctrl2)
        dev_ctrl2_label_44.set_pos(374, 393)
        dev_ctrl2_label_44.set_size(50, 16)
        dev_ctrl2_label_44.set_text("on-off")
        dev_ctrl2_label_44.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_44.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        # dev_ctrl2_label_44.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl2_label_45 = lv.label(dev_ctrl2)
        dev_ctrl2_label_45.set_pos(657, 403)
        dev_ctrl2_label_45.set_size(50, 16)
        dev_ctrl2_label_45.set_text("on-off")
        dev_ctrl2_label_45.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl2_label_45.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        # dev_ctrl2_label_45.add_style(self.style_siyuan_12, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.dev_ctrl2_sw_2 = lv.switch(dev_ctrl2)
        self.dev_ctrl2_sw_2.set_pos(714, 129)
        self.dev_ctrl2_sw_2.set_size(39, 16)
        self.dev_ctrl2_sw_2.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_2.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        self.dev_ctrl2_sw_2.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_2.add_state(lv.STATE.CHECKED)
        self.dev_ctrl2_sw_2.set_ext_click_area(10)

        self.dev_ctrl2_sw_3 = lv.switch(dev_ctrl2)
        self.dev_ctrl2_sw_3.set_pos(430, 266)
        self.dev_ctrl2_sw_3.set_size(39, 16)
        self.dev_ctrl2_sw_3.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_3.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        self.dev_ctrl2_sw_3.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_3.set_ext_click_area(10)

        self.dev_ctrl2_sw_4 = lv.switch(dev_ctrl2)
        self.dev_ctrl2_sw_4.set_pos(714, 265)
        self.dev_ctrl2_sw_4.set_size(39, 16)
        self.dev_ctrl2_sw_4.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_4.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        self.dev_ctrl2_sw_4.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_4.set_ext_click_area(10)

        self.dev_ctrl2_sw_5 = lv.switch(dev_ctrl2)
        self.dev_ctrl2_sw_5.set_pos(431, 391)
        self.dev_ctrl2_sw_5.set_size(39, 16)
        self.dev_ctrl2_sw_5.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_5.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        self.dev_ctrl2_sw_5.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_5.set_ext_click_area(10)

        self.dev_ctrl2_sw_6 = lv.switch(dev_ctrl2)
        self.dev_ctrl2_sw_6.set_pos(716, 401)
        self.dev_ctrl2_sw_6.set_size(39, 16)
        self.dev_ctrl2_sw_6.add_style(self.style_sw, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_6.add_style(self.style_sw_checked, lv.PART.INDICATOR | lv.STATE.CHECKED)
        self.dev_ctrl2_sw_6.add_style(self.style_sw_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.dev_ctrl2_sw_6.set_ext_click_area(10)

        dev_ctrl2_slider_2 = lv.slider(dev_ctrl2)
        dev_ctrl2_slider_2.set_pos(661, 160)
        dev_ctrl2_slider_2.set_size(101, 10)
        dev_ctrl2_slider_2.set_range(0, 100)
        dev_ctrl2_slider_2.set_value(50, False)
        dev_ctrl2_slider_2.add_style(self.style_slider, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl2_slider_2.add_style(self.style_slider_indicator, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        dev_ctrl2_slider_2.add_style(self.style_slider_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        dev_ctrl2_slider_2.set_ext_click_area(10)

        dev_ctrl2_slider_3 = lv.slider(dev_ctrl2)
        dev_ctrl2_slider_3.set_pos(379, 298)
        dev_ctrl2_slider_3.set_size(101, 10)
        dev_ctrl2_slider_3.set_range(0, 100)
        dev_ctrl2_slider_3.set_value(50, False)
        dev_ctrl2_slider_3.add_style(self.style_slider, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl2_slider_3.add_style(self.style_slider_indicator, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        dev_ctrl2_slider_3.add_style(self.style_slider_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        dev_ctrl2_slider_3.set_ext_click_area(10)

        dev_ctrl2_slider_4 = lv.slider(dev_ctrl2)
        dev_ctrl2_slider_4.set_pos(660, 297)
        dev_ctrl2_slider_4.set_size(101, 10)
        dev_ctrl2_slider_4.set_range(0, 100)
        dev_ctrl2_slider_4.set_value(50, False)
        dev_ctrl2_slider_4.add_style(self.style_slider, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl2_slider_4.add_style(self.style_slider_indicator, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        dev_ctrl2_slider_4.add_style(self.style_slider_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        dev_ctrl2_slider_4.set_ext_click_area(10)

        dev_ctrl2_slider_5 = lv.slider(dev_ctrl2)
        dev_ctrl2_slider_5.set_pos(378, 424)
        dev_ctrl2_slider_5.set_size(101, 10)
        dev_ctrl2_slider_5.set_range(0, 100)
        dev_ctrl2_slider_5.set_value(50, False)
        dev_ctrl2_slider_5.add_style(self.style_slider, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl2_slider_5.add_style(self.style_slider_indicator, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        dev_ctrl2_slider_5.add_style(self.style_slider_knob, lv.PART.KNOB | lv.STATE.DEFAULT)
        dev_ctrl2_slider_5.set_ext_click_area(10)

        dev_ctrl_btn_3 = lv.btn(dev_ctrl2)
        dev_ctrl_btn_3.set_pos(115, 182)
        dev_ctrl_btn_3.set_size(105, 40)
        dev_ctrl_btn_3_label = lv.label(dev_ctrl_btn_3)
        dev_ctrl_btn_3_label.set_text("Status")
        dev_ctrl_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.align(lv.ALIGN.CENTER, 0, 0)
        dev_ctrl_btn_3_label.set_style_text_color(lv.color_make(0xfa, 0xfa, 0xfa), lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
        dev_ctrl_btn_3.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.sw_dev1_btn = dev_ctrl_btn_3

        dev_ctrl_btn_3 = lv.btn(dev_ctrl2)
        dev_ctrl_btn_3.set_pos(115, 268)
        dev_ctrl_btn_3.set_size(105, 40)
        dev_ctrl_btn_3_label = lv.label(dev_ctrl_btn_3)
        dev_ctrl_btn_3_label.set_text("Control")
        dev_ctrl_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.align(lv.ALIGN.CENTER, 0, 0)
        dev_ctrl_btn_3_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
        dev_ctrl_btn_3.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.sw_dev1_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
    def getSwitchStatus(self):
        return (
            self.dev_ctrl2_sw_1.has_state(lv.STATE.CHECKED),
            self.dev_ctrl2_sw_2.has_state(lv.STATE.CHECKED),
            self.dev_ctrl2_sw_3.has_state(lv.STATE.CHECKED),
            self.dev_ctrl2_sw_4.has_state(lv.STATE.CHECKED),
            self.dev_ctrl2_sw_5.has_state(lv.STATE.CHECKED),
            self.dev_ctrl2_sw_6.has_state(lv.STATE.CHECKED)
        )

    def __home_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "MainScreen")

    def __monitor_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "MonitorScreen")

    def __dev_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "Dev1Screen")

    def __setting_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "SettingScreen")