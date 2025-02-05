import lvgl as lv
from usr.screen import Screen
from usr import EventMesh

class AboutScreen(Screen):
    def __init__(self):
        super().__init__()
        self.setting_btn = None
        self.monitor_btn = None
        self.home_btn = None
        self.dev_btn = None
        self.screen = None
        self.name = "AboutScreen"
        super().create_style()

    def create(self):
        about = lv.obj()
        self.screen = about
        # create style style_about_main_main_default
        style_about_main_main_default = lv.style_t()
        style_about_main_main_default.init()
        style_about_main_main_default.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_about_main_main_default.set_bg_opa(255)

        # add style for about
        about.add_style(style_about_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_cont_1 = lv.obj(about)
        about_cont_1.set_pos(0, 0)
        about_cont_1.set_size(100, 480)

        # add style for about_cont_1
        about_cont_1.add_style(self.style_cont_menu, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_imgbtn_1 = lv.imgbtn(about)
        about_imgbtn_1.set_pos(23, 22)
        about_imgbtn_1.set_size(54, 57)

        about_imgbtn_1_imgReleased = "U:/img/mp-2145617244.png"
        about_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_1_imgReleased, None, None)
        about_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, about_imgbtn_1_imgReleased, None, None)
        about_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, about_imgbtn_1_imgReleased, None, None)
        about_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, about_imgbtn_1_imgReleased, None, None)

        about_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
        about_imgbtn_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.home_btn = about_imgbtn_1

        about_imgbtn_2 = lv.imgbtn(about)
        about_imgbtn_2.set_pos(27, 127)
        about_imgbtn_2.set_size(45, 44)

        about_imgbtn_2_imgReleased = "U:/img/mp753364720.png"
        about_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_2_imgReleased, None, None)
        about_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, about_imgbtn_2_imgReleased, None, None)
        about_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, about_imgbtn_2_imgReleased, None, None)
        about_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, about_imgbtn_2_imgReleased, None, None)
        about_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
        about_imgbtn_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.monitor_btn = about_imgbtn_2

        about_imgbtn_3 = lv.imgbtn(about)
        about_imgbtn_3.set_pos(27, 202)
        about_imgbtn_3.set_size(45, 44)

        about_imgbtn_3_imgReleased = "U:/img/mp-370417216.png"
        about_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_3_imgReleased, None, None)
        about_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, about_imgbtn_3_imgReleased, None, None)
        about_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, about_imgbtn_3_imgReleased, None, None)
        about_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, about_imgbtn_3_imgReleased, None, None)

        about_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
        about_imgbtn_3.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_btn = about_imgbtn_3

        about_imgbtn_4 = lv.imgbtn(about)
        about_imgbtn_4.set_pos(27, 281)
        about_imgbtn_4.set_size(45, 44)

        about_imgbtn_4_imgReleased = "U:/img/mp1105200495.png"
        about_imgbtn_4.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_4_imgReleased, None, None)
        about_imgbtn_4.set_src(lv.imgbtn.STATE.PRESSED, about_imgbtn_4_imgReleased, None, None)
        about_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, about_imgbtn_4_imgReleased, None, None)
        about_imgbtn_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, about_imgbtn_4_imgReleased, None, None)
        about_imgbtn_4.add_flag(lv.obj.FLAG.CHECKABLE)
        about_imgbtn_4.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.dev_btn = about_imgbtn_4

        about_imgbtn_5 = lv.imgbtn(about)
        about_imgbtn_5.set_pos(26, 367)
        about_imgbtn_5.set_size(49, 41)

        about_imgbtn_5_imgReleased = "U:/img/mp256257620.png"
        about_imgbtn_5.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_5_imgReleased, None, None)
        about_imgbtn_5.set_src(lv.imgbtn.STATE.PRESSED, about_imgbtn_5_imgReleased, None, None)
        about_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, about_imgbtn_5_imgReleased, None, None)
        about_imgbtn_5.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, about_imgbtn_5_imgReleased, None, None)
        about_imgbtn_5.add_flag(lv.obj.FLAG.CHECKABLE)
        about_imgbtn_5.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_cont_5 = lv.obj(about)
        about_cont_5.set_pos(100, 28)
        about_cont_5.set_size(753, 452)
        about_list_1 = lv.list(about_cont_5)
        about_list_1.set_pos(82, 94)
        about_list_1.set_size(616, 304)

        about_list_1_btn_0_img = "U:/img/mp552145469.png"
        about_list_1_btn_0 = about_list_1.add_btn(about_list_1_btn_0_img, "iccid: 8987321382769737")

        # add style for about_list_1_btn_0
        about_list_1_btn_0.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_list_1_btn_1_img = "U:/img/mp-956155400.png"
        about_list_1_btn_1 = about_list_1.add_btn(about_list_1_btn_1_img, "IMEI: 4345343453453434")

        # add style for about_list_1_btn_1 mp1344530085
        about_list_1_btn_1.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)
        about_list_1_btn_2_img = "U:/img/mp1344530085.png"
        about_list_1_btn_2 = about_list_1.add_btn(about_list_1_btn_2_img, "软件版本: V 1.0.0")

        # add style for about_list_1_btn_2
        about_list_1_btn_2.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_list_1_btn_3_img = "U:/img/mp-708110542.png"
        about_list_1_btn_3 = about_list_1.add_btn(about_list_1_btn_3_img, "模块版本: ECXXXCN_LX_V00")

        # add style for about_list_1_btn_3
        about_list_1_btn_3.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_list_1_btn_4_img = "U:/img/mp2028397566.png"
        about_list_1_btn_4 = about_list_1.add_btn(about_list_1_btn_4_img, "运行时间: 3D-15H-37M")

        # add style for about_list_1_btn_4
        about_list_1_btn_4.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_list_1_btn_5_img = "U:/img/mp-1092957702.png"
        about_list_1_btn_5 = about_list_1.add_btn(about_list_1_btn_5_img, "使用者名称: 管理员1")

        # add style for about_list_1_btn_5
        about_list_1_btn_5.add_style(self.style_list_btn_label, lv.PART.MAIN | lv.STATE.DEFAULT)
        about_list_1.add_style(self.style_main_list, lv.PART.MAIN | lv.STATE.DEFAULT)
        about_list_1.add_style(self.style_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

        about_cont_5.add_style(self.style_cont_main, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_imgbtn_6 = lv.imgbtn(about)
        about_imgbtn_6.set_pos(26, 415)
        about_imgbtn_6.set_size(49, 41)

        about_imgbtn_6_imgReleased = "U:/img/mp-1736843955.png"
        about_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_6_imgReleased, None, None)
        about_imgbtn_6.set_src(lv.imgbtn.STATE.RELEASED, about_imgbtn_6_imgReleased, None, None)
        about_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, about_imgbtn_6_imgReleased, None, None)
        about_imgbtn_6.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, about_imgbtn_6_imgReleased, None, None)
        about_imgbtn_6.add_flag(lv.obj.FLAG.CHECKABLE)
        about_imgbtn_6.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_img_1 = lv.img(about)
        about_img_1.set_pos(798, 8)
        about_img_1.set_size(20, 15)
        about_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

        about_img_1_img = "U:/img/mp2146739423.png"

        about_img_1.set_src(about_img_1_img)
        about_img_1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_label_1 = lv.label(about)
        about_label_1.set_pos(124, 8)
        about_label_1.set_size(76, 13)
        about_label_1.set_text("Union")
        about_label_1.set_long_mode(lv.label.LONG.WRAP)
        about_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        about_label_1.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_img_2 = lv.img(about)
        about_img_2.set_pos(764, 9)
        about_img_2.set_size(18, 12)
        about_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

        about_img_2_img = "U:/img/mp-1849026116.png"

        about_img_2.set_src(about_img_2_img)
        about_img_2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_label_2 = lv.label(about)
        about_label_2.set_pos(703, 10)
        about_label_2.set_size(50, 13)
        about_label_2.set_text("12:00")
        about_label_2.set_long_mode(lv.label.LONG.WRAP)
        about_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        about_label_2.add_style(self.style_siyuan_14, lv.PART.MAIN | lv.STATE.DEFAULT)

        about_label_19 = lv.label(about)
        about_label_19.set_pos(416, 78)
        about_label_19.set_size(102, 28)
        about_label_19.set_text("About")
        about_label_19.set_long_mode(lv.label.LONG.WRAP)
        about_label_19.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        about_label_19.add_style(self.style_siyuan_22, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.home_btn.add_event_cb(lambda e: self.__home_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.monitor_btn.add_event_cb(lambda e: self.__monitor_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.dev_btn.add_event_cb(lambda e: self.__dev_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.setting_btn.add_event_cb(lambda e: self.__setting_btn_event_cb(e), lv.EVENT.PRESSED, None)

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