
import configparser
from pathlib import Path

import kivy
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from moduler.toolmonitor_data.exceldatabase import Database
from moduler.toolmonitor_data.gibbscam import GibbsCam
from moduler.toolmonitor_data.production_time import production_time
from moduler.customwidgets.mylabel import MyLabel


class ToolMonitor(BoxLayout):

    def __init__(self, tab_controll, **kwargs):
        super(ToolMonitor, self).__init__(**kwargs)

        self.master = tab_controll

        self.special_layout = BoxLayout(orientation='vertical', padding=10, size_hint_x=None, width=300)

        self.controll_layout = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint_x=None, width=150)

        self.pieces_layout = GridLayout(cols=1, spacing=1, padding=10, size_hint_y=None)
        self.pieces_layout.bind(minimum_height=self.pieces_layout.setter('height'))

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

        # Read in relevant path info
        # ---------------------------------------------------------------------

        if Path(self.config['Paths']['Rawdata']).is_file():
            self.raw_path = Path(self.config['Paths']['Rawdata'])
        else:
            self.raw_path = Path('./moduler/toolmonitor_data/rawdata/1000')

        self.unused_tools_path = Path(self.config['Paths']['Unused_tools'])
        self.tidskalkyle_path = Path(self.config['Paths']['Tidskalkyle'])

        #######################################################################

        # Run the exceldatabase object to make sure we atleast have 1 raw database sheet
        # to work with
        self.exceldatabase = Database(self.config_path)

        self._special_tools()
        self.controll_widgets()
        self._parts_possible()

        self.master.add_widget(self)

    def controll_widgets(self):

        btn1 = Button(text='Refresh Part Data', size_hint_y=None, height=30)
        btn1.bind(on_press=self.redraw)

        btn3 = Button(text='Grab new data', size_hint_y=None, height=30)
        btn3.bind(on_press=self.run_all)

        # self.controll_layout.add_widget(Label(size_hint=(1, 0.05)))
        self.controll_layout.add_widget(btn1)
        self.controll_layout.add_widget(btn3)
        self.controll_layout.add_widget(Label())

        self.add_widget(self.controll_layout)

    def redraw(self, touch):

        self.pieces_layout.clear_widgets()
        self.scrollwidget.remove_widget(self.pieces_layout)
        self.remove_widget(self.scrollwidget)

        self._parts_possible()

    def run_all(self, touch):

        self.load_data()
        self.save_unused_tools()
        self.time_calc()

    def load_data(self):

        self.exceldatabase.load_new_data(self.raw_path)
        print('New data loaded')

    def save_unused_tools(self):

        # if file does not exist, write out all currently unused tools to the file unused_tools.txt
        if not self.unused_tools_path.is_file():
            with open(self.unused_tools_path, 'w') as first_output:
                for i in self.exceldatabase.unused_tools:
                    first_output.write('{0}\n'.format(i))

        collected_tools = []
        with open(self.unused_tools_path, 'r') as file_input:
            for i in file_input:
                collected_tools.append(i[:-1])

        # print(self.exceldatabase.used_tools)

        for used_tool in self.exceldatabase.used_tools:
            if used_tool in collected_tools:
                # remove "unused_tool" from collected_tools
                collected_tools.remove(used_tool)
                # print('Hello, {0}'.format(used_tool))

        with open(self.unused_tools_path, 'w') as file_output:
            for i in collected_tools:
                file_output.write('{0}\n'.format(i))

        print('Unused tools recorded')

    def time_calc(self):

        timedata = GibbsCam(self.config_path)

        production_time(self.tidskalkyle_path, timedata.ordernumber, timedata.total_time)

        print('Production time calculated')

    def _parts_possible(self):

        toolinfo = GibbsCam(self.config_path)
        tools_in_use = toolinfo.piece_count
        max_pieces = toolinfo.max_piece_count

        self.pieces_layout.add_widget(MyLabel(text='Parts before toolchange:', size_hint_y=None, height=45, font_size=20, bcolor=self.grey))
        self.pieces_layout.add_widget(MyLabel(text=f'Order: {toolinfo.ordernumber}', size_hint_y=None, height=45, font_size=20, bcolor=self.grey))

        for i, j in zip(tools_in_use, max_pieces):
            self.pieces_layout.add_widget(Label(text=f'{i} : {tools_in_use[i]}/{max_pieces[i]}', size_hint_y=None, height=30, font_size=20))

        self.scrollwidget = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 57))
        self.scrollwidget.add_widget(self.pieces_layout)

        self.add_widget(self.scrollwidget)

    def _special_tools(self):

        special_tools = self.exceldatabase.special_tools
        special_tools.sort()

        self.special_layout.add_widget(MyLabel(text='Special Tools:', font_size=20, bcolor=self.grey))

        for i in special_tools:
            self.special_layout.add_widget(Label(text=i, font_size=20))

        self.add_widget(self.special_layout)

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

