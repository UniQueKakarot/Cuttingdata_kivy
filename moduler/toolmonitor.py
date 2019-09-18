
import configparser
from pathlib import Path

from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.toolmonitor_data.exceldatabase import Database
from moduler.toolmonitor_data.gibbscam import GibbsCam
from moduler.customwidgets.mylabel import MyLabel


class ToolMonitor(BoxLayout):

    def __init__(self, tab_controll, **kwargs):
        super(ToolMonitor, self).__init__(**kwargs)

        self.master = tab_controll
        # self.grid1 = GridLayout(cols=1, spacing=1, padding=10)
        self.grid1 = BoxLayout(orientation='vertical')
        self.grid2 = GridLayout(cols=1, spacing=1, padding=10)

        # Config generation
        # ---------------------------------------------------------------------
        self.config_path = Path('./moduler/toolmonitor_data/config/Toolmonitor.ini')

        self._config_gen()

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        #######################################################################

        # Run the exceldatabase object to make sure we atleast have 1 raw database sheet
        # to work with
        self.exceldatabase = Database(self.config_path)

        self._special_tools()
        self.skrot()

        self.master.add_widget(self)

    def _config_gen(self):

        """ Check if config file exists, if not, make one """

        if not self.config_path.is_file():

            config = configparser.ConfigParser()

            config['Paths'] = {'Rawdata': 'Q:/DNC/Mask20/1000',
                               'Fdata': './moduler/toolmonitor_data/rawdata/Formatted.csv',
                               'Rawdatabase': './moduler/toolmonitor_data/results/RawDatabase.xlsx',
                               'Resultdatabase': './moduler/toolmonitor_data/results/Database.xlsx',
                               'Tooltime': './moduler/toolmonitor_data/rawdata/Time.txt',
                               'Toolinfo': './moduler/toolmonitor_data/rawdata/Tools.txt',
                               'Unused_tools': './moduler/toolmonitor_data/results/unused_tools.txt',
                               'Tidskalkyle': './moduler/toolmonitor_data/results/Tidskalkyle.xlsx'}

            with open(self.config_path, 'w') as config_file:
                config.write(config_file)

    def _special_tools(self):

        special_tools = self.exceldatabase.special_tools
        special_tools.sort()

        self.grid1.add_widget(MyLabel(text='Special Tools:', font_size=20, bcolor=[1, 1, 1, 0.2]))

        for i in special_tools:
            self.grid1.add_widget(Label(text=i, font_size=20))

        self.add_widget(self.grid1)

    def _parts_possible(self):
        pass

    def skrot(self):

        test2 = GridLayout(cols=1, spacing=7, padding=10, size_hint_y=None)
        test2.bind(minimum_height=test2.setter('height'))

        for i in range(100):
            test2.add_widget(Label(text=f"Tool{i + 1}", size_hint_y=None, height=20))

        scroll_test = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 75))
        scroll_test.add_widget(test2)

        self.add_widget(scroll_test)

