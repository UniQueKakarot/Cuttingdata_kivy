
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel
from moduler.cuttingdata_calculations import cuttingdata


class Cuttingdata(GridLayout):

    def __init__(self, tab_controller, **kwargs):
        super(Cuttingdata, self).__init__(**kwargs)

        self.cols = 1
        self.padding = 10
        self.spacing = 7

        self.master = tab_controller

        self.res_label1 = None
        self.res_label2 = None

        self.text1 = None
        self.text2 = None
        self.text3 = None
        self.text4 = None

        # main_layout = GridLayout(cols=1, padding=10, spacing=7)

        ################################################################################################################
        cuttingspeed_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text1 = MyTextInput(hint_text="m/min", multiline=False, write_tab=False, font_size=20, on_text_validate=self.calculate)
        cuttingspeed_layout.add_widget(Label(text="Cutting Speed:", font_size=20))
        cuttingspeed_layout.add_widget(self.text1)

        ################################################################################################################
        milldia_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text2 = MyTextInput(hint_text="ø", multiline=False, write_tab=False, font_size=20, on_text_validate=self.calculate)
        milldia_layout.add_widget(Label(text="Mill Diameter:", font_size=20))
        milldia_layout.add_widget(self.text2)

        ################################################################################################################
        numteeth_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text3 = MyTextInput(hint_text="z", multiline=False, write_tab=False, font_size=20, on_text_validate=self.calculate)
        numteeth_layout.add_widget(Label(text="Number of Teeths:", font_size=20))
        numteeth_layout.add_widget(self.text3)

        ################################################################################################################
        feedtooth_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text4 = MyTextInput(hint_text="mm/o", multiline=False, write_tab=False, font_size=20, on_text_validate=self.calculate)
        feedtooth_layout.add_widget(Label(text="Feed per Tooth:", font_size=20))
        feedtooth_layout.add_widget(self.text4)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", font_size=20, on_press=self.calculate))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout1 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label1 = Label(text="", font_size=30)

        result_layout1.add_widget(Label(text="Spindel RPM: ", font_size=20))
        result_layout1.add_widget(self.res_label1)

        ################################################################################################################
        result_layout2 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label2 = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout2.add_widget(MyLabel(text="Feedrate: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout2.add_widget(self.res_label2)

        ################################################################################################################
        self.add_widget(cuttingspeed_layout)
        self.add_widget(milldia_layout)
        self.add_widget(numteeth_layout)
        self.add_widget(feedtooth_layout)
        self.add_widget(button_layout)
        self.add_widget(spacer_layout)
        self.add_widget(result_layout1)
        self.add_widget(result_layout2)

        self.master.add_widget(self)

    def calculate(self, touch):

        try:
            cuttingspeed = float(self.text1.text.replace(',', '.'))
        except ValueError:
            cuttingspeed = 0

        try:
            milldia = float(self.text2.text.replace(',', '.'))
        except ValueError:
            milldia = 0

        try:
            numz = float(self.text3.text.replace(',', '.'))
        except ValueError:
            numz = 0

        try:
            feedprtooth = float(self.text4.text.replace(',', '.'))
        except ValueError:
            feedprtooth = 0

        # Cuttingdata function is in its own file
        calculation_result = cuttingdata(cuttingspeed, milldia, numz, feedprtooth)

        self.res_label1.text = str(int(round(calculation_result[0], 0)))
        self.res_label2.text = str(int(round(calculation_result[1], 0)))

