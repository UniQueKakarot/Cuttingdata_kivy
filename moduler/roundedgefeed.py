
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel
from moduler.cuttingdata_calculations import fz_with_round_edge


class RoundEdge(GridLayout):

    def __init__(self, tab_controll, **kwargs):
        super(RoundEdge, self).__init__(**kwargs)

        self.master = tab_controll

        self.cols = 1
        self.padding = 10
        self.spacing = 7

        ################################################################################################################
        insert_dia_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text1 = MyTextInput(hint_text="insert dia", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        insert_dia_layout.add_widget(Label(text="Insert Diameter:", font_size=20))
        insert_dia_layout.add_widget(self.text1)

        ################################################################################################################
        hex_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text2 = MyTextInput(hint_text="hex", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        hex_layout.add_widget(Label(text="Hex:", font_size=20))
        hex_layout.add_widget(self.text2)

        ################################################################################################################
        doc_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text3 = MyTextInput(hint_text="ap", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        doc_layout.add_widget(Label(text="Depth of cut:", font_size=20))
        doc_layout.add_widget(self.text3)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", font_size=20, on_press=self.calculate))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout.add_widget(MyLabel(text="Round edge feed: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout.add_widget(self.res_label)

        ################################################################################################################

        self.add_widget(insert_dia_layout)
        self.add_widget(hex_layout)
        self.add_widget(doc_layout)
        self.add_widget(button_layout)
        self.add_widget(spacer_layout)
        self.add_widget(result_layout)

        self.master.add_widget(self)

    def calculate(self, touch):

        try:
            ap = float(self.text1.text.replace(',', '.'))
        except ValueError:
            ap = 0

        try:
            ae = float(self.text2.text.replace(',', '.'))
        except ValueError:
            ae = 0

        try:
            feed = float(self.text3.text.replace(',', '.'))
        except ValueError:
            feed = 0

        result = fz_with_round_edge(ap, ae, feed)

        if result == "Error":
            self.res_label.text = result
        else:
            self.res_label.text = str(round(result, 2))
