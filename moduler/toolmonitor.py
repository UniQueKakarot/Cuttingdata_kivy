
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


class ToolMonitor(BoxLayout):

    def __init__(self, tab_controll, **kwargs):
        super(ToolMonitor, self).__init__(**kwargs)

        self.master = tab_controll
        self.grid1 = GridLayout(cols=1, spacing=1, padding=10)
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

        # gibbs_toolinfo = GibbsCam(self.config_path)

        special_tools = self.exceldatabase.special_tools
        special_tools.sort()

        print(f"self.special_tools: {special_tools}")

        # print(f"self.tools: {gibbs_toolinfo.tools}\n")
        # print(f"self.tools_with_time: {gibbs_toolinfo.tools_with_time}\n")
        # print(f"self.ordernumber: {gibbs_toolinfo.ordernumber}\n")
        # print(f"self.total_time: {gibbs_toolinfo.total_time}\n")
        # print(f"self.piece_count: {gibbs_toolinfo.piece_count}\n")
        # print(f"self.max_piece_count: {gibbs_toolinfo.max_piece_count}\n")

    def _parts_possible(self):
        pass

    def skrot(self):

        test = GridLayout(cols=1, spacing=1, padding=10)

        for i in range(10):
            test.add_widget(Label(text=f'Test{i + 1}', font_size=20))

        test2 = GridLayout(cols=1, spacing=7, padding=10, size_hint_y=None)
        test2.bind(minimum_height=test2.setter('height'))

        for i in range(100):
            test2.add_widget(Label(text=f"Tool{i + 1}", size_hint_y=None, height=20))

        scroll_test = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 75))
        scroll_test.add_widget(test2)

        self.add_widget(test)
        self.add_widget(scroll_test)

