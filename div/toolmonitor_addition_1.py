from pathlib import Path
import configparser

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from moduler.customwidgets.mytextinput import MyTextInput
from moduler.customwidgets.mylabel import MyLabel
from div.toolmonitor_data.gibbscam import GibbsCam


class ToolMonitorAddition1(GridLayout):

    def __init__(self, tab_controll, **kwargs):
        super(ToolMonitorAddition1, self).__init__(**kwargs)

        self.cols = 2
        self.padding = 10
        self.spacing = 7

        self.grey = [1, 1, 1, 0.2]  # color for MyLabel

        self.master = tab_controll

        # config
        # -------------------------------------------------------------------------------------------------------------
        self.config_path = Path('./moduler/toolmonitor_data/config/Toolmonitor.ini')

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        ###############################################################################################################

        # Toolinfo
        # -------------------------------------------------------------------------------------------------------------
        self.gibbs_toolinfo = GibbsCam(self.config_path)
        ###############################################################################################################

        # Input handling
        # -------------------------------------------------------------------------------------------------------------
        input_layout = BoxLayout(orientation='vertical')
        self.text1 = MyTextInput(hint_text="Antall biter",
                                 multiline=False,
                                 write_tab=False,
                                 font_size=20,
                                 size_hint_y=None,
                                 height="40dp",
                                 on_text_validate=self.calculate)

        self.order_number_lbl = MyLabel(text=f'Order: {self.gibbs_toolinfo.ordernumber}',
                                        size_hint_y=None, height="40dp",  font_size=20, bcolor=self.grey)
        input_layout.add_widget(self.order_number_lbl)

        input_layout.add_widget(Label())
        input_layout.add_widget(self.text1)
        input_layout.add_widget(Label(size_hint_y=None, height="40dp"))

        btn1 = Button(text='DO IT', size_hint_y=None, height="40dp")
        btn1.bind(on_press=self.calculate)
        input_layout.add_widget(btn1)

        input_layout.add_widget(Label(size_hint_y=None, height="300dp"))
        ###############################################################################################################

        # Output handling
        # -------------------------------------------------------------------------------------------------------------
        output_layout = BoxLayout(orientation='vertical')
        for i in range(10):
            output_layout.add_widget(Label(text=f'Test: {i}', font_size=20))

        ###############################################################################################################

        # Layout managment
        # -------------------------------------------------------------------------------------------------------------
        self.add_widget(input_layout)
        self.add_widget(output_layout)
        self.master.add_widget(self)
        ###############################################################################################################

    def calculate(self, *args):

        parts = int(self.text1.text)

        max_parts = self.gibbs_toolinfo.max_piece_count
        parts_left = self.gibbs_toolinfo.piece_count

        for i, j in zip(max_parts, parts_left):

            if parts > max_parts[i]:
                print('Total time not enough')
            elif parts > parts_left[j]:
                print('Tool change needed')

        self.order_number_lbl.text = f'Order: {self.gibbs_toolinfo.ordernumber}'
        print(f'Order: {self.gibbs_toolinfo.ordernumber}')
        print(f'Max Antall: {self.gibbs_toolinfo.max_piece_count}')
        print(f'Antall: {self.gibbs_toolinfo.piece_count}')
        pass
