""" This is the entry module to the Cnc-Calculator GUI application """


from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

from moduler.customwidgets.mytextinput import MyTextInput

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()


class MainBody(TabbedPanel):
    """ Main body for the GUI application """

    def __init__(self, **kwargs):
        super(MainBody, self).__init__(**kwargs)

        self.do_default_tab = False

        self.tab1 = TabbedPanelItem(text="Tab1")

        self.cuttingdata()

        self.add_widget(self.tab1)
        self.default_tab = self.tab1

    def cuttingdata(self):

        """ Gui body for the cuttingdata tab """

        main_layout = BoxLayout(orientation="vertical")

        cuttingspeed_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text1 = MyTextInput(hint_text="m/min", multiline=False, write_tab=False)
        cuttingspeed_layout.add_widget(Label(text="Cutting Speed:"))
        cuttingspeed_layout.add_widget(text1)

        milldia_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text2 = MyTextInput(hint_text="ø", multiline=False, write_tab=False)
        milldia_layout.add_widget(Label(text="Mill Diameter:"))
        milldia_layout.add_widget(text2)

        numteeth_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text3 = MyTextInput(hint_text="z", multiline=False, write_tab=False)
        numteeth_layout.add_widget(Label(text="Number of Teeths:"))
        numteeth_layout.add_widget(text3)

        feedtooth_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")

        text4 = MyTextInput(hint_text="mm/o", multiline=False, write_tab=False)
        feedtooth_layout.add_widget(Label(text="Feed per Tooth:"))
        feedtooth_layout.add_widget(text4)

        main_layout.add_widget(cuttingspeed_layout)
        main_layout.add_widget(milldia_layout)
        main_layout.add_widget(numteeth_layout)
        main_layout.add_widget(feedtooth_layout)

        self.tab1.add_widget(main_layout)



class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        return MainBody()


CncCalculators().run()
