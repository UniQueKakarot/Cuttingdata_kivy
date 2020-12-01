from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel


class MidPoint(GridLayout):

    def __init__(self, tab_controll, **kwargs):
        super(MidPoint, self).__init__(**kwargs)

        self.master = tab_controll

        self.cols = 1
        self.padding = 10
        self.spacing = 7

        ################################################################################################################
        tol_top_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text1 = MyTextInput(hint_text="tolerance topp", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        tol_top_layout.add_widget(Label(text="Tolerance Maximum:", font_size=20))
        tol_top_layout.add_widget(self.text1)

        ################################################################################################################
        dia_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text2 = MyTextInput(hint_text="diameter", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        dia_layout.add_widget(Label(text="Diameter:", font_size=20))
        dia_layout.add_widget(self.text2)

        ################################################################################################################
        tol_min_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text3 = MyTextInput(hint_text="tolerance bottom", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        tol_min_layout.add_widget(Label(text="Tolerance Minimum:", font_size=20))
        tol_min_layout.add_widget(self.text3)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", font_size=20, on_press=self.calculate))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout1 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label1 = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout1.add_widget(MyLabel(text="Tolerance Max: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout1.add_widget(self.res_label1)

        ################################################################################################################

        ################################################################################################################
        result_layout2 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label2 = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout2.add_widget(MyLabel(text="Tolerance Center: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout2.add_widget(self.res_label2)

        ################################################################################################################

        ################################################################################################################
        result_layout3 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label3 = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout3.add_widget(MyLabel(text="Tolerance Min: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout3.add_widget(self.res_label3)

        ################################################################################################################

        self.add_widget(tol_top_layout)
        self.add_widget(dia_layout)
        self.add_widget(tol_min_layout)
        self.add_widget(button_layout)
        self.add_widget(spacer_layout)
        self.add_widget(result_layout1)
        self.add_widget(result_layout2)
        self.add_widget(result_layout3)

        self.master.add_widget(self)

    def calculate(self, touch):

        try:
            tol_top = float(self.text1.text.replace(',', '.'))
        except ValueError:
            tol_top = 0

        try:
            dia = float(self.text2.text.replace(',', '.'))
        except ValueError:
            dia = 0

        try:
            tol_min = float(self.text3.text.replace(',', '.'))
        except ValueError:
            tol_min = 0

        dia_top = dia + tol_top
        dia_bot = dia + tol_min
        dia_mid = ((dia_top - dia_bot) / 2) + dia_bot

        self.res_label1.text = str(round(dia_top, 4))
        self.res_label2.text = str(round(dia_mid, 4))
        self.res_label3.text = str(round(dia_bot, 4))
