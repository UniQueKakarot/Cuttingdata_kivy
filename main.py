""" This is the entry module to the Cnc-Calculator GUI application """


from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()


class MainBody(TabbedPanel):
    """ Main body for the GUI application """

    def __init__(self, **kwargs):
        super(MainBody, self).__init__(**kwargs)
        self.result1: str = ""
        self.result2: str = ""

        self.do_default_tab = False

        self.tab1 = TabbedPanelItem(text="Cutting Speed")

        self.cuttingdata()

        self.add_widget(self.tab1)
        self.default_tab = self.tab1

    def cuttingdata(self):

        """ Gui body for the cuttingdata tab """

        main_layout = GridLayout(cols=1, padding=10, spacing=7)

        ################################################################################################################
        cuttingspeed_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text1 = MyTextInput(hint_text="m/min", multiline=False, write_tab=False, font_size=20)
        cuttingspeed_layout.add_widget(Label(text="Cutting Speed:", font_size=20))
        cuttingspeed_layout.add_widget(text1)

        ################################################################################################################
        milldia_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text2 = MyTextInput(hint_text="ø", multiline=False, write_tab=False, font_size=20)
        milldia_layout.add_widget(Label(text="Mill Diameter:", font_size=20))
        milldia_layout.add_widget(text2)

        ################################################################################################################
        numteeth_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text3 = MyTextInput(hint_text="z", multiline=False, write_tab=False, font_size=20)
        numteeth_layout.add_widget(Label(text="Number of Teeths:", font_size=20))
        numteeth_layout.add_widget(text3)

        ################################################################################################################
        feedtooth_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text4 = MyTextInput(hint_text="mm/o", multiline=False, write_tab=False, font_size=20, on_text_validate=self.test)
        feedtooth_layout.add_widget(Label(text="Feed per Tooth:", font_size=20))
        feedtooth_layout.add_widget(text4)

        ################################################################################################################
        button_layout = BoxLayout(size_hint_y=None, height="40dp")
        button_layout.add_widget(Button(text="Calculate!", on_press=self.test))

        ################################################################################################################
        spacer_layout = BoxLayout()
        spacer_layout.add_widget(Label())

        ################################################################################################################
        result_layout1 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        res_label1 = Label(text=self.result1, font_size=30)

        result_layout1.add_widget(Label(text="Spindel RPM: ", font_size=20))
        result_layout1.add_widget(res_label1)

        ################################################################################################################
        result_layout2 = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        res_label2 = MyLabel(text=self.result2, font_size=30, bcolor=[1, 1, 1, 0.2])

        result_layout2.add_widget(MyLabel(text="Feedrate: ", font_size=20, bcolor=[1, 1, 1, 0.2]))
        result_layout2.add_widget(res_label2)

        ################################################################################################################
        main_layout.add_widget(cuttingspeed_layout)
        main_layout.add_widget(milldia_layout)
        main_layout.add_widget(numteeth_layout)
        main_layout.add_widget(feedtooth_layout)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(spacer_layout)
        main_layout.add_widget(result_layout1)
        main_layout.add_widget(result_layout2)

        self.tab1.add_widget(main_layout)

    def test(self, touch):
        print("Hello World!")


class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        return MainBody()


CncCalculators().run()
