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


class Screen(object):
    """Abstract class of screen"""

    def __init__(self):
        super().__init__()
        self.style_siyuan_14_red = None
        self.style_siyuan_16_blue = None
        self.style_opa_btn = None
        self.style_siyuan_26 = None
        self.style_siyuan_20 = None
        self.style_siyuan_18 = None
        self.style_list_btn_label = None
        self.style_siyuan_22 = None
        self.style_line = None
        self.style_arc_knob = None
        self.style_arc_indicator_green = None
        self.style_arc_indicator_yellow = None
        self.style_arc_indicator_red = None
        self.style_tileview_scrollbar = None
        self.style_cont_main = None
        self.style_arc = None
        self.style_slider_knob = None
        self.style_slider_indicator = None
        self.style_slider = None
        self.style_btn = None
        self.style_sw_knob = None
        self.style_siyuan_12 = None
        self.style_sw_checked = None
        self.style_sw = None
        self.style_siyuan_16 = None
        self.style_ta = None
        self.style_tileview = None
        self.style_chart = None
        self.style_siyuan_14 = None
        self.style_cont_opa_57 = None
        self.style_scrollbar = None
        self.style_main_list = None
        self.style_main_list_label = None
        self.style_img = None
        self.style_cont_menu = None
        self.style_screen = None


    def create_style(self):
        """
        create style
        """
        # Interface style, background color: 3a5283
        style_screen = lv.style_t()
        style_screen.init()
        style_screen.set_bg_color(lv.color_make(0x3a, 0x52, 0x83))
        style_screen.set_bg_opa(255)
        self.style_screen = style_screen

        # The style of the left menu bar
        style_cont_menu = lv.style_t()
        style_cont_menu.init()
        style_cont_menu.set_radius(0)
        style_cont_menu.set_bg_color(lv.color_make(0x28, 0x39, 0x5c))
        style_cont_menu.set_bg_grad_color(lv.color_make(0x28, 0x39, 0x5c))
        style_cont_menu.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_cont_menu.set_bg_opa(255)
        style_cont_menu.set_border_color(lv.color_make(0x21, 0x95, 0xf6))
        style_cont_menu.set_border_width(0)
        style_cont_menu.set_border_opa(0)
        style_cont_menu.set_pad_left(0)
        style_cont_menu.set_pad_right(0)
        style_cont_menu.set_pad_top(0)
        style_cont_menu.set_pad_bottom(0)
        self.style_cont_menu = style_cont_menu

        # The main screen has four font styles
        style_cont_main = lv.style_t()
        style_cont_main.init()
        style_cont_main.set_radius(0)
        style_cont_main.set_bg_color(lv.color_make(0x30, 0x45, 0x70))
        style_cont_main.set_bg_grad_color(lv.color_make(0x30, 0x45, 0x70))
        style_cont_main.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_cont_main.set_bg_opa(255)
        style_cont_main.set_border_color(lv.color_make(0x21, 0x95, 0xf6))
        style_cont_main.set_border_width(0)
        style_cont_main.set_border_opa(0)
        style_cont_main.set_pad_left(0)
        style_cont_main.set_pad_right(0)
        style_cont_main.set_pad_top(0)
        style_cont_main.set_pad_bottom(0)
        self.style_cont_main = style_cont_main

        style_cont_opa_57 = lv.style_t()
        style_cont_opa_57.init()
        style_cont_opa_57.set_radius(15)
        style_cont_opa_57.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_cont_opa_57.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_cont_opa_57.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_cont_opa_57.set_bg_opa(100)
        style_cont_opa_57.set_border_color(lv.color_make(0x21, 0x95, 0xf6))
        style_cont_opa_57.set_border_width(0)
        style_cont_opa_57.set_border_opa(0)
        style_cont_opa_57.set_pad_left(0)
        style_cont_opa_57.set_pad_right(0)
        style_cont_opa_57.set_pad_top(0)
        style_cont_opa_57.set_pad_bottom(0)
        self.style_cont_opa_57 = style_cont_opa_57

        style_list_btn_label = lv.style_t()
        style_list_btn_label.init()
        style_list_btn_label.set_radius(1)
        style_list_btn_label.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_list_btn_label.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_list_btn_label.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_list_btn_label.set_bg_opa(0)
        style_list_btn_label.set_text_color(lv.color_make(0xf7, 0xf7, 0xf8))
        style_list_btn_label.set_text_font(lv.font_montserrat_18)
        self.style_list_btn_label = style_list_btn_label

        # Picture style with transparency of 255
        style_img = lv.style_t()
        style_img.init()
        style_img.set_img_opa(255)
        self.style_img = style_img

        # The style of each row of the homepage list
        style_main_list_label = lv.style_t()
        style_main_list_label.init()
        style_main_list_label.set_radius(3)
        style_main_list_label.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_main_list_label.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_main_list_label.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_main_list_label.set_bg_opa(0)
        style_main_list_label.set_text_color(lv.color_make(0xf7, 0xf7, 0xf8))
        style_main_list_label.set_text_font(lv.font_montserrat_14)
        self.style_main_list_label = style_main_list_label

        # The style of homepage list
        style_main_list = lv.style_t()
        style_main_list.init()
        style_main_list.set_radius(3)
        style_main_list.set_bg_color(lv.color_make(0x30, 0x45, 0x70))
        style_main_list.set_bg_grad_color(lv.color_make(0x30, 0x45, 0x70))
        style_main_list.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_main_list.set_bg_opa(255)
        style_main_list.set_border_color(lv.color_make(0xe1, 0xe6, 0xee))
        style_main_list.set_border_width(0)
        style_main_list.set_pad_left(5)
        style_main_list.set_pad_right(5)
        style_main_list.set_pad_top(0)
        self.style_main_list = style_main_list

        # Transparent style of scrollbar
        style_scrollbar = lv.style_t()
        style_scrollbar.init()
        style_scrollbar.set_bg_opa(0)
        self.style_scrollbar = style_scrollbar

        # 思源12字体label样式 字距2
        style_siyuan_12 = lv.style_t()
        style_siyuan_12.init()
        style_siyuan_12.set_radius(0)
        style_siyuan_12.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_12.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_12.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_12.set_bg_opa(0)
        style_siyuan_12.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_12.set_text_font(lv.font_montserrat_12)
        style_siyuan_12.set_text_letter_space(1)
        style_siyuan_12.set_pad_left(0)
        style_siyuan_12.set_pad_right(0)
        style_siyuan_12.set_pad_top(0)
        style_siyuan_12.set_pad_bottom(0)
        self.style_siyuan_12 = style_siyuan_12

        # 思源14字体label样式 字距0
        style_siyuan_14 = lv.style_t()
        style_siyuan_14.init()
        style_siyuan_14.set_radius(0)
        style_siyuan_14.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_14.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_14.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_14.set_bg_opa(0)
        style_siyuan_14.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_14.set_text_font(lv.font_montserrat_14)
        style_siyuan_14.set_text_letter_space(0)
        style_siyuan_14.set_pad_left(0)
        style_siyuan_14.set_pad_right(0)
        style_siyuan_14.set_pad_top(0)
        style_siyuan_14.set_pad_bottom(0)
        self.style_siyuan_14 = style_siyuan_14

        # 红色思源14字体label样式 字距0
        style_siyuan_14_red = lv.style_t()
        style_siyuan_14_red.init()
        style_siyuan_14_red.set_radius(0)
        style_siyuan_14_red.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_14_red.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_14_red.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_14_red.set_bg_opa(0)
        style_siyuan_14_red.set_text_color(lv.color_make(0xff, 0x4d, 0x4d))
        style_siyuan_14_red.set_text_font(lv.font_montserrat_14)
        style_siyuan_14_red.set_text_letter_space(0)
        style_siyuan_14_red.set_pad_left(0)
        style_siyuan_14_red.set_pad_right(0)
        style_siyuan_14_red.set_pad_top(0)
        style_siyuan_14_red.set_pad_bottom(0)
        self.style_siyuan_14_red = style_siyuan_14_red

        # 思源12字体label样式 字距2
        style_siyuan_16 = lv.style_t()
        style_siyuan_16.init()
        style_siyuan_16.set_radius(0)
        style_siyuan_16.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_16.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_16.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_16.set_bg_opa(0)
        style_siyuan_16.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_16.set_text_font(lv.font_montserrat_16)
        style_siyuan_16.set_text_letter_space(1)
        style_siyuan_16.set_pad_left(0)
        style_siyuan_16.set_pad_right(0)
        style_siyuan_16.set_pad_top(0)
        style_siyuan_16.set_pad_bottom(0)
        self.style_siyuan_16 = style_siyuan_16

        # 蓝色思源12字体label样式 字距2
        style_siyuan_16_blue = lv.style_t()
        style_siyuan_16_blue.init()
        style_siyuan_16_blue.set_radius(0)
        style_siyuan_16_blue.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_16_blue.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_16_blue.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_16_blue.set_bg_opa(0)
        style_siyuan_16_blue.set_text_color(lv.color_make(0x93, 0xec, 0xe6))
        style_siyuan_16_blue.set_text_font(lv.font_montserrat_16)
        style_siyuan_16_blue.set_text_letter_space(1)
        style_siyuan_16_blue.set_pad_left(0)
        style_siyuan_16_blue.set_pad_right(0)
        style_siyuan_16_blue.set_pad_top(0)
        style_siyuan_16_blue.set_pad_bottom(0)
        self.style_siyuan_16_blue = style_siyuan_16_blue

        # 思源12字体label样式 字距2
        style_siyuan_18 = lv.style_t()
        style_siyuan_18.init()
        style_siyuan_18.set_radius(0)
        style_siyuan_18.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18.set_bg_opa(0)
        style_siyuan_18.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_18.set_text_font(lv.font_montserrat_18)
        style_siyuan_18.set_text_letter_space(1)
        style_siyuan_18.set_pad_left(0)
        style_siyuan_18.set_pad_right(0)
        style_siyuan_18.set_pad_top(0)
        style_siyuan_18.set_pad_bottom(0)
        self.style_siyuan_18 = style_siyuan_18

        # 思源12字体label样式 字距2
        style_siyuan_20 = lv.style_t()
        style_siyuan_20.init()
        style_siyuan_20.set_radius(0)
        style_siyuan_20.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_20.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_20.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_20.set_bg_opa(0)
        style_siyuan_20.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_20.set_text_font(lv.font_montserrat_20)
        style_siyuan_20.set_text_letter_space(1)
        style_siyuan_20.set_pad_left(0)
        style_siyuan_20.set_pad_right(0)
        style_siyuan_20.set_pad_top(0)
        style_siyuan_20.set_pad_bottom(0)
        self.style_siyuan_20 = style_siyuan_20

        # 思源12字体label样式 字距2
        style_siyuan_26 = lv.style_t()
        style_siyuan_26.init()
        style_siyuan_26.set_radius(0)
        style_siyuan_26.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_26.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_26.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_26.set_bg_opa(0)
        style_siyuan_26.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_26.set_text_font(lv.font_montserrat_22)
        style_siyuan_26.set_text_letter_space(1)
        style_siyuan_26.set_pad_left(0)
        style_siyuan_26.set_pad_right(0)
        style_siyuan_26.set_pad_top(0)
        style_siyuan_26.set_pad_bottom(0)
        self.style_siyuan_26 = style_siyuan_26

        # 思源22字体label样式 字距2
        style_siyuan_22 = lv.style_t()
        style_siyuan_22.init()
        style_siyuan_22.set_radius(0)
        style_siyuan_22.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_22.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_22.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_22.set_bg_opa(0)
        style_siyuan_22.set_text_color(lv.color_make(0xff, 0xff, 0xff))
        style_siyuan_22.set_text_font(lv.font_montserrat_22)
        style_siyuan_22.set_text_letter_space(1)
        style_siyuan_22.set_pad_left(0)
        style_siyuan_22.set_pad_right(0)
        style_siyuan_22.set_pad_top(0)
        style_siyuan_22.set_pad_bottom(0)
        self.style_siyuan_22 = style_siyuan_22

        # 主页图表样式
        style_chart = lv.style_t()
        style_chart.init()
        style_chart.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_chart.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_chart.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_chart.set_bg_opa(34)
        style_chart.set_pad_left(5)
        style_chart.set_pad_right(5)
        style_chart.set_pad_top(5)
        style_chart.set_pad_bottom(5)
        style_chart.set_line_color(lv.color_make(0xc6, 0xbe, 0xbe))
        style_chart.set_line_width(2)
        style_chart.set_line_opa(255)
        self.style_chart = style_chart

        # 主页透明按钮样式
        style_opa_btn = lv.style_t()
        style_opa_btn.init()
        style_opa_btn.set_radius(5)
        style_opa_btn.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_opa_btn.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_opa_btn.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_opa_btn.set_bg_opa(0)
        style_opa_btn.set_shadow_color(lv.color_make(0x21, 0x95, 0xf6))
        style_opa_btn.set_shadow_opa(0)
        style_opa_btn.set_border_width(0)
        self.style_opa_btn = style_opa_btn

        # 滑动页样式
        style_tileview = lv.style_t()
        style_tileview.init()
        style_tileview.set_radius(0)
        style_tileview.set_bg_color(lv.color_make(0x30, 0x45, 0x70))
        style_tileview.set_bg_grad_color(lv.color_make(0x30, 0x45, 0x70))
        style_tileview.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_tileview.set_bg_opa(213)
        self.style_tileview = style_tileview

        # 滑动页scrollbar样式
        style_tileview_scrollbar = lv.style_t()
        style_tileview_scrollbar.init()
        style_tileview_scrollbar.set_radius(0)
        style_tileview_scrollbar.set_bg_color(lv.color_make(0xea, 0xef, 0xf3))
        style_tileview_scrollbar.set_bg_opa(87)
        self.style_tileview_scrollbar = style_tileview_scrollbar

        # textarea样式
        style_ta = lv.style_t()
        style_ta.init()
        style_ta.set_radius(4)
        style_ta.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_ta.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_ta.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_ta.set_bg_opa(255)
        style_ta.set_border_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_ta.set_border_width(2)
        style_ta.set_text_color(lv.color_make(0x00, 0x00, 0x00))
        style_ta.set_text_font(lv.font_montserrat_12)
        style_ta.set_text_letter_space(2)
        style_ta.set_text_align(lv.TEXT_ALIGN.LEFT)
        style_ta.set_pad_left(2)
        style_ta.set_pad_right(2)
        style_ta.set_pad_top(2)
        style_ta.set_pad_bottom(2)
        self.style_ta = style_ta

        # 开关样式
        style_sw = lv.style_t()
        style_sw.init()
        style_sw.set_radius(100)
        style_sw.set_bg_color(lv.color_make(0xe6, 0xe2, 0xe6))
        style_sw.set_bg_grad_color(lv.color_make(0xe6, 0xe2, 0xe6))
        style_sw.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_sw.set_bg_opa(255)
        self.style_sw = style_sw

        # create style style_sw_checked
        style_sw_checked = lv.style_t()
        style_sw_checked.init()
        style_sw_checked.set_radius(100)
        style_sw_checked.set_bg_color(lv.color_make(0x42, 0xb8, 0xaa))
        style_sw_checked.set_bg_grad_color(lv.color_make(0x33, 0xb1, 0xc1))
        style_sw_checked.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_sw_checked.set_bg_opa(255)
        self.style_sw_checked = style_sw_checked

        # create style style_sw_knob
        style_sw_knob = lv.style_t()
        style_sw_knob.init()
        style_sw_knob.set_radius(100)
        style_sw_knob.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_sw_knob.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_sw_knob.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_sw_knob.set_bg_opa(255)
        self.style_sw_knob = style_sw_knob

        # 蓝色不透明按钮样式
        style_btn = lv.style_t()
        style_btn.init()
        style_btn.set_radius(5)
        style_btn.set_bg_color(lv.color_make(0x23, 0xc6, 0xd1))
        style_btn.set_bg_grad_color(lv.color_make(0x23, 0xc6, 0xd1))
        style_btn.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_btn.set_bg_opa(189)
        style_btn.set_shadow_color(lv.color_make(0x21, 0x95, 0xf6))
        style_btn.set_shadow_opa(0)
        style_btn.set_border_color(lv.color_make(0x21, 0x95, 0xf6))
        style_btn.set_border_width(0)
        style_btn.set_border_opa(255)
        self.style_btn = style_btn

        # create style style_slider
        style_slider = lv.style_t()
        style_slider.init()
        style_slider.set_radius(50)
        style_slider.set_bg_color(lv.color_make(0xf2, 0xf6, 0xf7))
        style_slider.set_bg_grad_color(lv.color_make(0xed, 0xf0, 0xf3))
        style_slider.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_slider.set_bg_opa(128)
        style_slider.set_outline_color(lv.color_make(0x21, 0x95, 0xf6))
        style_slider.set_outline_width(0)
        style_slider.set_outline_opa(255)
        style_slider.set_pad_left(0)
        style_slider.set_pad_right(0)
        style_slider.set_pad_top(0)
        style_slider.set_pad_bottom(0)
        self.style_slider = style_slider

        # create style style_slider_indicator
        style_slider_indicator = lv.style_t()
        style_slider_indicator.init()
        style_slider_indicator.set_radius(50)
        style_slider_indicator.set_bg_color(lv.color_make(0x38, 0xb9, 0xc2))
        style_slider_indicator.set_bg_grad_color(lv.color_make(0x38, 0xb9, 0xc2))
        style_slider_indicator.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_slider_indicator.set_bg_opa(197)
        self.style_slider_indicator = style_slider_indicator

        # create style style_slider_knob
        style_slider_knob = lv.style_t()
        style_slider_knob.init()
        style_slider_knob.set_radius(50)
        style_slider_knob.set_bg_color(lv.color_make(0xe6, 0xee, 0xf5))
        style_slider_knob.set_bg_grad_color(lv.color_make(0xee, 0xf3, 0xf6))
        style_slider_knob.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_slider_knob.set_bg_opa(234)
        self.style_slider_knob = style_slider_knob

        # create style style_arc
        style_arc = lv.style_t()
        style_arc.init()
        style_arc.set_border_width(0)
        style_arc.set_arc_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_arc.set_arc_width(8)
        self.style_arc = style_arc

        # create style style_arc_indicator绿色
        style_arc_indicator_green = lv.style_t()
        style_arc_indicator_green.init()
        style_arc_indicator_green.set_arc_color(lv.color_make(0x53, 0xdf, 0x89))
        style_arc_indicator_green.set_arc_width(8)
        self.style_arc_indicator_green = style_arc_indicator_green

        # create style style_arc_indicator黄色
        style_arc_indicator_yellow = lv.style_t()
        style_arc_indicator_yellow.init()
        style_arc_indicator_yellow.set_arc_color(lv.color_make(0xd8, 0x88, 0x2c))
        style_arc_indicator_yellow.set_arc_width(8)
        self.style_arc_indicator_yellow = style_arc_indicator_yellow

        # create style style_arc_indicator红色
        style_arc_indicator_red = lv.style_t()
        style_arc_indicator_red.init()
        style_arc_indicator_red.set_arc_color(lv.color_make(0xfa, 0x19, 0x28))
        style_arc_indicator_red.set_arc_width(8)
        self.style_arc_indicator_red = style_arc_indicator_red

        # create style style_arc_knob
        style_arc_knob = lv.style_t()
        style_arc_knob.init()
        style_arc_knob.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_arc_knob.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_arc_knob.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_arc_knob.set_bg_opa(0)
        style_arc_knob.set_pad_all(5)
        self.style_arc_knob = style_arc_knob

        # line style
        style_line = lv.style_t()
        style_line.init()
        style_line.set_line_color(lv.color_make(0xf2, 0xf2, 0xf2))
        style_line.set_line_width(1)
        style_line.set_line_rounded(255)
        self.style_line = style_line

    def create_screen(self):
        """create screen"""
        pass

    @staticmethod
    def publish_ope():
        # Get operator's name
        return EventMesh.publish("screen_get_ope")

    @staticmethod
    def publish_sig():
        # Get signal strength
        return EventMesh.publish("screen_get_sig")

    @staticmethod
    def publish_time():
        # Get system time
        return EventMesh.publish("screen_get_time")

    @staticmethod
    def publish_battery():
        # Get battery power
        return EventMesh.publish("screen_get_battery")