
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from moduler.customwidgets.mylabel import MyLabel
from moduler.customwidgets.mytextinput import MyTextInput
from moduler.cuttingdata_calculations import ra


class SurfaceRa(GridLayout):
    def __init__(self, tabcontroll, **kwargs):
        super(SurfaceRa, self).__init__(**kwargs)

        self.master = tabcontroll

        self.cols = 1
        self.padding = 10
        self.spacing = 7

        ################################################################################################################
        feed_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text1 = MyTextInput(hint_text="mm/m or mm/o", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        feed_layout.add_widget(Label(text="Feedrate:", font_size=20))
        feed_layout.add_widget(self.text1)

        ################################################################################################################
        noserad_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text2 = MyTextInput(hint_text="R", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        noserad_layout.add_widget(Label(text="Nose radius:", font_size=20))
        noserad_layout.add_widget(self.text2)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", font_size=20, on_press=self.calculate))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout.add_widget(MyLabel(text="RA: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout.add_widget(self.res_label)

        ################################################################################################################

        self.add_widget(feed_layout)
        self.add_widget(noserad_layout)
        self.add_widget(button_layout)
        self.add_widget(spacer_layout)
        self.add_widget(result_layout)

        self.master.add_widget(self)

    def calculate(self, touch):
        """ Calculating RA """

        try:
            feed = float(self.text1.text.replace(',', '.'))
        except ValueError:
            feed = 0

        try:
            nose_radius = float(self.text2.text.replace(',', '.'))
        except ValueError:
            nose_radius = 0

        result = ra(feed, nose_radius)

        if result == "Error":
            self.res_label.text = "Error"
        else:
            self.res_label.text = str(round(result, 2))


