""" This is the entry module to the Cnc-Calculator GUI application """

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.config import Config

from moduler.cuttingdata import Cuttingdata
from moduler.helix_angle import HelixAngle
from moduler.materialremoval import MaterialRemoval
from div.toolmonitor import ToolMonitor
from div.toolmonitor_addition_1 import ToolMonitorAddition1

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

# TODO: Look into pickling data for persistance instead of writing files, this includes the excel database.
# A pickled database system is in place

# TODO: Internal data storage and data generation on demand, meaning instead of writing out data beforehand
# TODO: make it possible to generate the data when you need it

# TODO: Some kind of feedback on what the toolmonitor is doing and when it is done

# TODO: Need to make a tool table parser for Heidenhain tool tables

# TODO: Production_time.py is getting slow, needs a rework

# TODO: Write moar tests


class MainBody(TabbedPanel):
    """ Main body for the GUI application """

    def __init__(self, **kwargs):
        super(MainBody, self).__init__(**kwargs)

        self.do_default_tab = False
        self.tab_height = 50
        self.tab_width = 125

        self.tab1 = TabbedPanelItem(text="Cutting Speed")
        self.tab2 = TabbedPanelItem(text="Toolpath Angle")
        self.tab3 = TabbedPanelItem(text="Material Removal")
        self.tab4 = TabbedPanelItem(text="Tool Monitor")
        self.tab5 = TabbedPanelItem(text="TM Addition 1")

        self.cuttingdata()
        self.helix_angle()
        self.material_removal()
        # self.toolmonitor()
        # self.toolmonitoradd1()

        self.add_widget(self.tab1)
        self.add_widget(self.tab2)
        self.add_widget(self.tab3)
        # self.add_widget(self.tab4)
        # self.add_widget(self.tab5)
        self.default_tab = self.tab1

    def cuttingdata(self):

        """ Gui body for the cuttingdata tab """

        Cuttingdata(self.tab1)

    def helix_angle(self):

        HelixAngle(self.tab2)

    def material_removal(self):

        MaterialRemoval(self.tab3)

    def toolmonitor(self):

        ToolMonitor(self.tab4)

    def toolmonitoradd1(self):

        ToolMonitorAddition1(self.tab5)

    def surface_roughness(self):
        pass


class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        return MainBody()


CncCalculators().run()
