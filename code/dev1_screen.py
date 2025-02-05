import lvgl as lv
from usr.screen import Screen
from usr import EventMesh

class Dev1Screen(Screen):
    def __init__(self):
        super().__init__()
        self.sw_dev2_btn = None
        self.dev_btn = None
        self.setting_btn = None
        self.monitor_btn = None
        self.home_btn = None
        self.screen = None
        self.name = "Dev1Screen"
        super().create_style()

    def create(self):
        dev_ctrl = lv.obj()
        self.screen = dev_ctrl
        # create style style_dev_ctrl_main_main_default
        style_dev_ctrl_main_main_default = lv.style_t()
        style_dev_ctrl_main_main_default.init()
        style_dev_ctrl_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_dev_ctrl_main_main_default.set_bg_opa(255)

        # add style for dev_ctrl
        dev_ctrl.add_style(style_dev_ctrl_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_1 = lv.obj(dev_ctrl)
        dev_ctrl_cont_1.set_pos(0, 0)
        dev_ctrl_cont_1.set_size(100, 480)
        dev_ctrl_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_imgbtn_1 = lv.imgbtn(dev_ctrl)
        dev_ctrl_imgbtn_1.set_pos(23, 22)
        dev_ctrl_imgbtn_1.set_size(54, 57)

        dev_ctrl_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        dev_ctrl_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl_imgbtn_1_imgReleased, None, None)
        dev_ctrl_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl_imgbtn_1_imgReleased, None, None)
        dev_ctrl_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl_imgbtn_1_imgReleased, None, None)
        dev_ctrl_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl_imgbtn_1_imgReleased, None, None)

        dev_ctrl_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = dev_ctrl_imgbtn_1

        dev_ctrl_imgbtn_2 = lv.imgbtn(dev_ctrl)
        dev_ctrl_imgbtn_2.set_pos(27, 127)
        dev_ctrl_imgbtn_2.set_size(45, 44)

        dev_ctrl_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        dev_ctrl_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl_imgbtn_2_imgReleased, None, None)
        dev_ctrl_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl_imgbtn_2_imgReleased, None, None)
        dev_ctrl_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl_imgbtn_2_imgReleased, None, None)
        dev_ctrl_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl_imgbtn_2_imgReleased, None, None)
        dev_ctrl_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = dev_ctrl_imgbtn_2

        dev_ctrl_imgbtn_3 = lv.imgbtn(dev_ctrl)
        dev_ctrl_imgbtn_3.set_pos(27, 202)
        dev_ctrl_imgbtn_3.set_size(45, 44)

        dev_ctrl_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        dev_ctrl_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl_imgbtn_3_imgReleased, None, None)
        dev_ctrl_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl_imgbtn_3_imgReleased, None, None)
        dev_ctrl_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl_imgbtn_3_imgReleased, None, None)
        dev_ctrl_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl_imgbtn_3_imgReleased, None, None)
        dev_ctrl_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = dev_ctrl_imgbtn_3

        dev_ctrl_imgbtn_4 = lv.imgbtn(dev_ctrl)
        dev_ctrl_imgbtn_4.set_pos(27, 281)
        dev_ctrl_imgbtn_4.set_size(45, 44)

        dev_ctrl_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        dev_ctrl_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl_imgbtn_4_imgReleased, None, None)
        dev_ctrl_imgbtn_4.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl_imgbtn_4_imgReleased, None, None)
        dev_ctrl_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl_imgbtn_4_imgReleased, None, None)
        dev_ctrl_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl_imgbtn_4_imgReleased, None, None)
        dev_ctrl_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = dev_ctrl_imgbtn_4

        dev_ctrl_imgbtn_5 = lv.imgbtn(dev_ctrl)
        dev_ctrl_imgbtn_5.set_pos(26, 367)
        dev_ctrl_imgbtn_5.set_size(49, 41)

        dev_ctrl_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        dev_ctrl_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl_imgbtn_5_imgReleased, None, None)
        dev_ctrl_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl_imgbtn_5_imgReleased, None, None)
        dev_ctrl_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl_imgbtn_5_imgReleased, None, None)
        dev_ctrl_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl_imgbtn_5_imgReleased, None, None)

        dev_ctrl_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_imgbtn_6 = lv.imgbtn(dev_ctrl)
        dev_ctrl_imgbtn_6.set_pos(26, 415)
        dev_ctrl_imgbtn_6.set_size(49, 41)

        dev_ctrl_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        dev_ctrl_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, dev_ctrl_imgbtn_6_imgReleased, None, None)
        dev_ctrl_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dev_ctrl_imgbtn_6_imgReleased, None, None)
        dev_ctrl_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dev_ctrl_imgbtn_6_imgReleased, None, None)
        dev_ctrl_imgbtn_6.set_src(lv.imgbtn.STATE.PRESSED, dev_ctrl_imgbtn_6_imgReleased, None, None)
        dev_ctrl_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        dev_ctrl_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_1 = lv.img(dev_ctrl)
        dev_ctrl_img_1.set_pos(798, 8)
        dev_ctrl_img_1.set_size(20, 15)
        dev_ctrl_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_1_img = "U:/img/mp2146739423.png"

        dev_ctrl_img_1.set_src(dev_ctrl_img_1_img)
        dev_ctrl_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_1 = lv.label(dev_ctrl)
        dev_ctrl_label_1.set_pos(124, 8)
        dev_ctrl_label_1.set_size(76, 13)
        dev_ctrl_label_1.set_text("Union")
        dev_ctrl_label_1.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_2 = lv.img(dev_ctrl)
        dev_ctrl_img_2.set_pos(764, 9)
        dev_ctrl_img_2.set_size(18, 12)
        dev_ctrl_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_2_img = "U:/img/mp-1849026116.png"

        dev_ctrl_img_2.set_src(dev_ctrl_img_2_img)
        dev_ctrl_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_2 = lv.label(dev_ctrl)
        dev_ctrl_label_2.set_pos(703, 10)
        dev_ctrl_label_2.set_size(50, 13)
        dev_ctrl_label_2.set_text("12:00")
        dev_ctrl_label_2.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_tileview_1 = lv.tileview(dev_ctrl)
        dev_ctrl_tileview_1.set_pos(240, 60)
        dev_ctrl_tileview_1.set_size(612, 419)
        dev_ctrl_tileview_1_tileview = dev_ctrl_tileview_1.add_tile(0, 0, lv.DIR.RIGHT)
        dev_ctrl_tileview_1_Title = dev_ctrl_tileview_1.add_tile(1, 0, lv.DIR.LEFT)
        dev_ctrl_tileview_1.add_style(self.style_tileview, lv.PART.MAIN | lv.STATE.DEFAULT)
        dev_ctrl_tileview_1.add_style(self.style_tileview_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        dev_ctrl_cont_9 = lv.obj(dev_ctrl)
        dev_ctrl_cont_9.set_pos(277, 97)
        dev_ctrl_cont_9.set_size(156, 75)
        dev_ctrl_cont_9.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_10 = lv.obj(dev_ctrl)
        dev_ctrl_cont_10.set_pos(468, 98)
        dev_ctrl_cont_10.set_size(156, 75)
        dev_ctrl_cont_10.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_12 = lv.obj(dev_ctrl)
        dev_ctrl_cont_12.set_pos(663, 99)
        dev_ctrl_cont_12.set_size(156, 75)
        dev_ctrl_cont_12.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_13 = lv.obj(dev_ctrl)
        dev_ctrl_cont_13.set_pos(279, 217)
        dev_ctrl_cont_13.set_size(156, 75)
        dev_ctrl_cont_13.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_14 = lv.obj(dev_ctrl)
        dev_ctrl_cont_14.set_pos(472, 216)
        dev_ctrl_cont_14.set_size(156, 75)
        dev_ctrl_cont_14.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_15 = lv.obj(dev_ctrl)
        dev_ctrl_cont_15.set_pos(661, 214)
        dev_ctrl_cont_15.set_size(156, 75)
        dev_ctrl_cont_15.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_16 = lv.obj(dev_ctrl)
        dev_ctrl_cont_16.set_pos(280, 337)
        dev_ctrl_cont_16.set_size(156, 75)
        dev_ctrl_cont_16.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_cont_17 = lv.obj(dev_ctrl)
        dev_ctrl_cont_17.set_pos(477, 338)
        dev_ctrl_cont_17.set_size(156, 75)
        dev_ctrl_cont_17.add_style(self.style_cont_opa_57, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_23 = lv.label(dev_ctrl)
        dev_ctrl_label_23.set_pos(322, 139)
        dev_ctrl_label_23.set_size(93, 25)
        dev_ctrl_label_23.set_text("Status: Normal")
        dev_ctrl_label_23.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_23.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_23.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_24 = lv.label(dev_ctrl)
        dev_ctrl_label_24.set_pos(519, 139)
        dev_ctrl_label_24.set_size(93, 25)
        dev_ctrl_label_24.set_text("Status: Normal")
        dev_ctrl_label_24.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_24.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_24.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_25 = lv.label(dev_ctrl)
        dev_ctrl_label_25.set_pos(715, 139)
        dev_ctrl_label_25.set_size(93, 25)
        dev_ctrl_label_25.set_text("Status: Normal")
        dev_ctrl_label_25.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_25.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_25.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_26 = lv.label(dev_ctrl)
        dev_ctrl_label_26.set_pos(715, 254)
        dev_ctrl_label_26.set_size(93, 25)
        dev_ctrl_label_26.set_text("Status: Normal")
        dev_ctrl_label_26.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_26.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_26.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_27 = lv.label(dev_ctrl)
        dev_ctrl_label_27.set_pos(527, 255)
        dev_ctrl_label_27.set_size(93, 25)
        dev_ctrl_label_27.set_text("Status: Normal")
        dev_ctrl_label_27.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_27.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_27.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_28 = lv.label(dev_ctrl)
        dev_ctrl_label_28.set_pos(331, 255)
        dev_ctrl_label_28.set_size(93, 25)
        dev_ctrl_label_28.set_text("Status: Error")
        dev_ctrl_label_28.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_28.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_28.add_style(self.style_siyuan_14_red, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_29 = lv.label(dev_ctrl)
        dev_ctrl_label_29.set_pos(331, 377)
        dev_ctrl_label_29.set_size(93, 25)
        dev_ctrl_label_29.set_text("Status: Normal")
        dev_ctrl_label_29.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_29.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_29.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_30 = lv.label(dev_ctrl)
        dev_ctrl_label_30.set_pos(528, 377)
        dev_ctrl_label_30.set_size(93, 25)
        dev_ctrl_label_30.set_text("Status: Normal")
        dev_ctrl_label_30.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_30.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_30.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_32 = lv.label(dev_ctrl)
        dev_ctrl_label_32.set_pos(290, 103)
        dev_ctrl_label_32.set_size(131, 18)
        dev_ctrl_label_32.set_text("Temp&Humi Sensor")
        dev_ctrl_label_32.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_32.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_32.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_33 = lv.label(dev_ctrl)
        dev_ctrl_label_33.set_pos(477, 104)
        dev_ctrl_label_33.set_size(134, 23)
        dev_ctrl_label_33.set_text("Light Sensor")
        dev_ctrl_label_33.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_33.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_33.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_34 = lv.label(dev_ctrl)
        dev_ctrl_label_34.set_pos(679, 106)
        dev_ctrl_label_34.set_size(130, 19)
        dev_ctrl_label_34.set_text("PH Sensor")
        dev_ctrl_label_34.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_34.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_34.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_35 = lv.label(dev_ctrl)
        dev_ctrl_label_35.set_pos(290, 224)
        dev_ctrl_label_35.set_size(135, 17)
        dev_ctrl_label_35.set_text("EC Sensor")
        dev_ctrl_label_35.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_35.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_35.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_36 = lv.label(dev_ctrl)
        dev_ctrl_label_36.set_pos(487, 224)
        dev_ctrl_label_36.set_size(128, 17)
        dev_ctrl_label_36.set_text("CO2 Sensor")
        dev_ctrl_label_36.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_36.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_36.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_37 = lv.label(dev_ctrl)
        dev_ctrl_label_37.set_pos(674, 222)
        dev_ctrl_label_37.set_size(134, 17)
        dev_ctrl_label_37.set_text("O2 Sensor")
        dev_ctrl_label_37.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_37.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_37.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_38 = lv.label(dev_ctrl)
        dev_ctrl_label_38.set_pos(289, 346)
        dev_ctrl_label_38.set_size(141, 17)
        dev_ctrl_label_38.set_text("Wind Sensor")
        dev_ctrl_label_38.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_38.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_38.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_label_39 = lv.label(dev_ctrl)
        dev_ctrl_label_39.set_pos(482, 347)
        dev_ctrl_label_39.set_size(150, 17)
        dev_ctrl_label_39.set_text("Soil Temp&Humi Sensor")
        dev_ctrl_label_39.set_long_mode(lv.label.LONG.WRAP)
        dev_ctrl_label_39.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        dev_ctrl_label_39.add_style(self.style_siyuan_16_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_3 = lv.img(dev_ctrl)
        dev_ctrl_img_3.set_pos(282, 127)
        dev_ctrl_img_3.set_size(40, 43)
        dev_ctrl_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_3_img = "U:/img/mp996516799.png"

        dev_ctrl_img_3.set_src(dev_ctrl_img_3_img)
        dev_ctrl_img_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_4 = lv.img(dev_ctrl)
        dev_ctrl_img_4.set_pos(477, 126)
        dev_ctrl_img_4.set_size(37, 37)
        dev_ctrl_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_4_img = "U:/img/mp-888054910.png"

        dev_ctrl_img_4.set_src(dev_ctrl_img_4_img)
        dev_ctrl_img_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_5 = lv.img(dev_ctrl)
        dev_ctrl_img_5.set_pos(672, 127)
        dev_ctrl_img_5.set_size(37, 37)
        dev_ctrl_img_5.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_5_img = "U:/img/mp170626480.png"

        dev_ctrl_img_5.set_src(dev_ctrl_img_5_img)
        dev_ctrl_img_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_6 = lv.img(dev_ctrl)
        dev_ctrl_img_6.set_pos(289, 245)
        dev_ctrl_img_6.set_size(35, 36)
        dev_ctrl_img_6.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_6_img = "U:/img/mp-1166782970.png"

        dev_ctrl_img_6.set_src(dev_ctrl_img_6_img)
        dev_ctrl_img_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_7 = lv.img(dev_ctrl)
        dev_ctrl_img_7.set_pos(483, 244)
        dev_ctrl_img_7.set_size(37, 37)
        dev_ctrl_img_7.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_7_img = "U:/img/mp-856104962.png"

        dev_ctrl_img_7.set_src(dev_ctrl_img_7_img)
        dev_ctrl_img_7.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_8 = lv.img(dev_ctrl)
        dev_ctrl_img_8.set_pos(672, 244)
        dev_ctrl_img_8.set_size(37, 37)
        dev_ctrl_img_8.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_8_img = "U:/img/mp639761499.png"

        dev_ctrl_img_8.set_src(dev_ctrl_img_8_img)
        dev_ctrl_img_8.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_9 = lv.img(dev_ctrl)
        dev_ctrl_img_9.set_pos(286, 366)
        dev_ctrl_img_9.set_size(37, 37)
        dev_ctrl_img_9.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_9_img = "U:/img/mp-120643648.png"

        dev_ctrl_img_9.set_src(dev_ctrl_img_9_img)
        dev_ctrl_img_9.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_10 = lv.img(dev_ctrl)
        dev_ctrl_img_10.set_pos(485, 370)
        dev_ctrl_img_10.set_size(32, 32)
        dev_ctrl_img_10.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_10_img = "U:/img/mp-1969396802.png"

        dev_ctrl_img_10.set_src(dev_ctrl_img_10_img)
        dev_ctrl_img_10.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_img_4 = lv.img(dev_ctrl)
        dev_ctrl_img_4.set_pos(60, 320)
        dev_ctrl_img_4.set_size(16, 14)
        dev_ctrl_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

        dev_ctrl_img_4_img = "U:/img/mp-347592130.png"

        dev_ctrl_img_4.set_src(dev_ctrl_img_4_img)
        dev_ctrl_img_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_btn_3 = lv.btn(dev_ctrl)
        dev_ctrl_btn_3.set_pos(115, 182)
        dev_ctrl_btn_3.set_size(105, 40)
        dev_ctrl_btn_3_label = lv.label(dev_ctrl_btn_3)
        dev_ctrl_btn_3_label.set_text("Status")
        dev_ctrl_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.align(lv.ALIGN.CENTER, 0, 0)
        dev_ctrl_btn_3_label.set_style_text_color(lv.color_make(0xfa, 0xfa, 0xfa), lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
        dev_ctrl_btn_3.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

        dev_ctrl_btn_3 = lv.btn(dev_ctrl)
        dev_ctrl_btn_3.set_pos(115, 268)
        dev_ctrl_btn_3.set_size(105, 40)
        dev_ctrl_btn_3_label = lv.label(dev_ctrl_btn_3)
        dev_ctrl_btn_3_label.set_text("Control")
        dev_ctrl_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.align(lv.ALIGN.CENTER, 0, 0)
        dev_ctrl_btn_3_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
        dev_ctrl_btn_3_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
        dev_ctrl_btn_3.add_style(self.style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.sw_dev2_btn = dev_ctrl_btn_3

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.sw_dev2_btn.add_event_cb(lambda e: self.__sw_dev2_btn_event_cb(e), lv.EVENT.PRESSED, None)

    def __sw_dev2_btn_event_cb(self, e):
        src = e.get_target()
        code = e.get_code()
        print("点击事件发生")
        EventMesh.publish("load_screen", "Dev2Screen")

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