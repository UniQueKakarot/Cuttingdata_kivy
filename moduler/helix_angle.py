
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel
from moduler.cuttingdata_calculations import helix_angle


class HelixAngle(GridLayout):

    def __init__(self, tab_controll, **kwargs):
        super(HelixAngle, self).__init__(**kwargs)

        self.master = tab_controll

        self.cols = 1
        self.padding = 10
        self.spacing = 7

        ################################################################################################################
        milld_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text1 = MyTextInput(hint_text="dia", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        milld_layout.add_widget(Label(text="Mill Diameter:", font_size=20))
        milld_layout.add_widget(self.text1)

        ################################################################################################################
        holed_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text2 = MyTextInput(hint_text="dia", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        holed_layout.add_widget(Label(text="Hole Diameter:", font_size=20))
        holed_layout.add_widget(self.text2)

        ################################################################################################################
        pitch_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text3 = MyTextInput(hint_text="z step", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        pitch_layout.add_widget(Label(text="Z Step/Pitch:", font_size=20))
        pitch_layout.add_widget(self.text3)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", font_size=20, on_press=self.calculate))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout.add_widget(MyLabel(text="Helix Angle: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout.add_widget(self.res_label)

        ################################################################################################################

        self.add_widget(milld_layout)
        self.add_widget(holed_layout)
        self.add_widget(pitch_layout)
        self.add_widget(button_layout)
        self.add_widget(spacer_layout)
        self.add_widget(result_layout)

        self.master.add_widget(self)

    def calculate(self, touch):

        try:
            milld = float(self.text1.text.replace(',', '.'))
        except ValueError:
            milld = 1

        try:
            holed = float(self.text2.text.replace(',', '.'))
        except ValueError:
            holed = 1

        try:
            step = float(self.text3.text.replace(',', '.'))
        except ValueError:
            step = 1

        result = helix_angle(holed, milld, step)

        if result == "Error":
            self.res_label.text = "Error"
        else:
            self.res_label.text = str(round(result, 2))
