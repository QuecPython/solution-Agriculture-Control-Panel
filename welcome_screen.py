import lvgl as lv
from usr.screen import Screen
from usr import EventMesh

class WelcomeScreen(Screen):
    def __init__(self):
        super().__init__()
        self.screen = None
        self.name = 'WelcomeScreen'
        super().create_style()

    def create(self):
        welcome = lv.obj()
        self.screen = welcome
        # create style style_welcome_main_main_default
        style_welcome_main_main_default = lv.style_t()
        style_welcome_main_main_default.init()
        style_welcome_main_main_default.set_bg_color(lv.color_make(0x31, 0x48, 0x77))
        style_welcome_main_main_default.set_bg_opa(255)

        # add style for welcome
        welcome.add_style(style_welcome_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)

        welcome_img_bg = lv.img(welcome)
        welcome_img_bg.set_pos(0, 0)
        welcome_img_bg.set_size(854, 480)
        welcome_img_bg.add_flag(lv.obj.FLAG.CLICKABLE)

        welcome_img_bg_img = "U:/img/mp-72558433.sjpg"
        welcome_img_bg.set_src(welcome_img_bg_img)
        welcome_img_bg.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        welcome_img_area1 = lv.img(welcome)
        welcome_img_area1.set_pos(137, 153)
        welcome_img_area1.set_size(600, 50)
        welcome_img_area1.add_flag(lv.obj.FLAG.CLICKABLE)

        welcome_img_area1_img = "U:/img/mp-1913163078.png"

        welcome_img_area1.set_src(welcome_img_area1_img)
        welcome_img_area1.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        welcome_img_area2 = lv.img(welcome)
        welcome_img_area2.set_pos(302, 228)
        welcome_img_area2.set_size(300, 70)
        welcome_img_area2.add_flag(lv.obj.FLAG.CLICKABLE)

        welcome_img_area2_img = "U:/img/mp-246393227.png"

        welcome_img_area2.set_src(welcome_img_area2_img)
        welcome_img_area2.add_style(self.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        welcome_label_title = lv.label(welcome)
        welcome_label_title.set_pos(150, 170)
        welcome_label_title.set_size(540, 32)
        welcome_label_title.set_text("Smart Agriculture Central Control System")
        welcome_label_title.set_long_mode(lv.label.LONG.WRAP)
        welcome_label_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        welcome_label_title.add_style(self.style_siyuan_22, lv.PART.MAIN | lv.STATE.DEFAULT)

        welcome_label_date = lv.label(welcome)
        welcome_label_date.set_pos(307, 238)
        welcome_label_date.set_size(240, 18)
        welcome_label_date.set_text("2022/05/30")
        welcome_label_date.set_long_mode(lv.label.LONG.WRAP)
        welcome_label_date.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        welcome_label_date.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)

        welcome_label_time = lv.label(welcome)
        welcome_label_time.set_pos(307, 268)
        welcome_label_time.set_size(242, 20)
        welcome_label_time.set_text("12:06")
        welcome_label_time.set_long_mode(lv.label.LONG.WRAP)
        welcome_label_time.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        welcome_label_time.add_style(self.style_siyuan_18, lv.PART.MAIN | lv.STATE.DEFAULT)
