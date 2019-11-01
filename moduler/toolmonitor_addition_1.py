
from kivy.uix.boxlayout import BoxLayout

from moduler.toolmonitor_data.gibbscam import GibbsCam
from moduler.toolmonitor_data.production_time import production_time


class ToolMonitorAddition1(BoxLayout):

    def __init__(self, tab_controll, **kwargs):
        super(ToolMonitorAddition1, self).__init__(**kwargs)

        self.master = tab_controll





        self.master.add_widget(self)
