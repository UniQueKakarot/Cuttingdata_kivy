""" This is the entry module to the Cnc-Calculator GUI application """


from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()


class MainBody(TabbedPanel):
    """ Main body for the GUI application """

    def __init__(self, **kwargs):
        super(MainBody, self).__init__(**kwargs)

        self.do_default_tab = False

        self.test1 = TabbedPanelItem(text="Tab1")

        self.master_layout = BoxLayout()

        btn = Button(text="Hello")
        self.master_layout.add_widget(btn)

        self.test1.add_widget(self.master_layout)
        self.add_widget(self.test1)

        self.default_tab = self.test1

        # self.content = self.master_layout


class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        return MainBody()


CncCalculators().run()
