
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

        self.grid1 = BoxLayout(orientation='vertical', padding=10)

        self.grid2 = BoxLayout(orientation='vertical', spacing=1)

        self.grid3 = GridLayout(cols=1, spacing=1, padding=10, size_hint_y=None)
        self.grid3.bind(minimum_height=self.grid3.setter('height'))

        self.scrollwidget = None

        # ---------------------------------------------------------------------

        self.grey = [1, 1, 1, 0.2]

        #######################################################################

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
        self.testing()
        self._parts_possible()

        print(self.children)

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

        self.grid1.add_widget(MyLabel(text='Special Tools:', font_size=20, bcolor=self.grey))

        for i in special_tools:
            self.grid1.add_widget(Label(text=i, font_size=20))

        self.add_widget(self.grid1)

    def testing(self):

        btn1 = Button(text='Calculate', size_hint_y=None, height=30)
        btn1.bind(on_press=self.test2)

        btn2 = Button(text='Clear', size_hint_y=None, height=30)
        btn2.bind(on_press=self.test3)

        self.grid2.add_widget(btn1)
        self.grid2.add_widget(btn2)
        self.grid2.add_widget(Button(text='Grab new data', size_hint_y=None, height=30))
        self.grid2.add_widget(Label())

        self.add_widget(self.grid2)

    def test2(self, touch):

        self.remove_widget(self.scrollwidget)

    def test3(self, touch):

        self._parts_possible()

    def _parts_possible(self):

        toolinfo = GibbsCam(self.config_path)
        tools_in_use = toolinfo.piece_count
        max_pieces = toolinfo.max_piece_count

        self.grid3.add_widget(MyLabel(text='Tools in use:', size_hint_y=None, height=45, font_size=20, bcolor=self.grey))

        for i, j in zip(tools_in_use, max_pieces):
            self.grid3.add_widget(Label(text=f'{i} : {tools_in_use[i]}/{max_pieces[i]}', size_hint_y=None, height=30, font_size=20))

        self.scrollwidget = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 57))
        self.scrollwidget.add_widget(self.grid3)

        self.add_widget(self.scrollwidget)

