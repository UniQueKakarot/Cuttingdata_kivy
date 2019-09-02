""" This is the entry module to the Cnc-Calculator GUI application """


from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.config import Config

from moduler.cuttingdata import Cuttingdata
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()


class MainBody(TabbedPanel):
    """ Main body for the GUI application """

    def __init__(self, **kwargs):
        super(MainBody, self).__init__(**kwargs)

        self.do_default_tab = False

        self.tab1 = TabbedPanelItem(text="Cutting Speed")

        self.cuttingdata()

        self.add_widget(self.tab1)
        self.default_tab = self.tab1

    def cuttingdata(self):

        """ Gui body for the cuttingdata tab """

        Cuttingdata(self.tab1)


class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        return MainBody()


CncCalculators().run()
