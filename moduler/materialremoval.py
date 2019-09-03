
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel
from moduler.cuttingdata_calculations import material_removal


class MaterialRemoval(GridLayout):

    def __init__(self, tab_controll, **kwargs):
        super(MaterialRemoval, self).__init__(**kwargs)

        self.master = tab_controll

        self.cols = 1
        self.padding = 10
        self.spacing = 7

        ################################################################################################################
        doc_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text1 = MyTextInput(hint_text="ap", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        doc_layout.add_widget(Label(text="Depth of Cut:", font_size=20))
        doc_layout.add_widget(self.text1)

        ################################################################################################################
        woc_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text2 = MyTextInput(hint_text="ae", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        woc_layout.add_widget(Label(text="Width of Cut:", font_size=20))
        woc_layout.add_widget(self.text2)

        ################################################################################################################
        feed_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.text3 = MyTextInput(hint_text="mm/m", multiline=False, write_tab=False, font_size=20,
                                 on_text_validate=self.calculate)

        feed_layout.add_widget(Label(text="Feedrate:", font_size=20))
        feed_layout.add_widget(self.text3)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", font_size=20, on_press=self.calculate))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        self.res_label = MyLabel(text="", font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout.add_widget(MyLabel(text="Material Removal Rate: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout.add_widget(self.res_label)

        ################################################################################################################

        self.add_widget(doc_layout)
        self.add_widget(woc_layout)
        self.add_widget(feed_layout)
        self.add_widget(button_layout)
        self.add_widget(spacer_layout)
        self.add_widget(result_layout)

        self.master.add_widget(self)

    def calculate(self, touch):

        try:
            ap = float(self.text1.text.replace(',', '.'))
        except ValueError:
            ap = 1

        try:
            ae = float(self.text2.text.replace(',', '.'))
        except ValueError:
            ae = 1

        try:
            feed = float(self.text3.text.replace(',', '.'))
        except ValueError:
            feed = 1

        self.res_label.text = str(round(material_removal(ap, ae, feed), 2)) + ' cm³/min'
