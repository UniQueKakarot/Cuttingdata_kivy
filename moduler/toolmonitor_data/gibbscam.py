
""" This file extract time data from the macrogenerated gibbscam files """

from pathlib import Path
import configparser

import openpyxl as op

# from moduler.toolmonitor_data.exceldatabase import Database
from moduler.toolmonitor_data.database_handler import DatabaseHandler


class GibbsCam:

    """ This class extract all necessary information from the macrofiles Gibbscam spew out
        and make the data available in class attributes"""

    def __init__(self, config_path):
        
        # make paths available to the class methods
        self.config_path = config_path

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        self.time_file = Path(self.config['Paths']['tooltime'])
        self.tool_file = Path(self.config['Paths']['Toolinfo'])
        self.raw_database = Path(self.config['Paths']['Rawdatabase'])

        # -------------------------------------------------------------------------------
        # Attributes ment to be accessed outside of the class
        self.tools = {}
        self.tools_with_time = {}
        self.ordernumber = None
        self.total_time = 0
        self.piece_count = {}
        self.max_piece_count = {}
        #################################################################################

        self._tool_data()
        self._time_data()
        self._pieces()

    def _tool_data(self):

        """ Extracting toolid and position in tool list from the output file from gibbscam.
            This method has to run before you call time_data!"""

        with open(self.tool_file, 'r') as file1:
            file_content = file1.readlines()

        # cleaning up the input and collecting it in a dict
        for i in file_content:
            content = i.split(',')
            toolid_stripped = content[1].strip()

            self.tools[int(content[0][:-7])] = int(toolid_stripped[:-7])

    def _time_data(self):

        """ Collecting the total time each tool has been used in this program
            and makes it available for further use, time values are givven in
            seconds """

        # self._tool_data()

        with open(self.time_file) as file1:
            file_content = file1.readlines()

        self.ordernumber = file_content.pop(0)
        self.ordernumber = self.ordernumber[:-1]  # Removeing the newline char at the end

        local_toollist = []
        local_tooldict = {}
        for item in file_content:
            content = item.split(',')

            # collecting total time in seconds
            self.total_time += float(content[1].strip())

            local_toollist.append(int(float(content[0])))
        
        for number in set(local_toollist):
            tooltime = 0

            for time in file_content:
                content = time.split(',')

                if number == int(float(content[0])):
                    tooltime += float(content[1].strip())
                
                local_tooldict[number] = round(tooltime, 2)  # GibbsCam toolid + time in seconds

        for i in local_tooldict:
            self.tools_with_time[self.tools[i]] = local_tooldict[i]  # Machine Toolid + time in seconds
        
        # return self.tools_with_time

    def _pieces(self):

        """ Based on the machining time Gibbscam has calculated, calculate how many pieces we can
            machine with the tools we use before we have to replace one of them """

        # TODO: Rewrite this to use the new database handler

        # Check if the raw data excel sheet is available, if not generate it
        database_handler = DatabaseHandler(self.config_path)
        tooltable = database_handler.tool_table()

        # workbook = op.load_workbook(self.raw_database)
        # worksheet = workbook['New Data']

        time_minutes = []  # Holds timeinfo in minutes instead of seconds
        for i in self.tools_with_time.keys():

            toollife_remain = tooltable[f'T{i}'][4]

            # Shaving of an S before we convert to float, and then converting minutes to seconds
            toollife_remain = float(toollife_remain[1:]) * 60

            # Dividing remining tool life with machining time to get the piece count
            # and rounding the number up 1, because as long as the tool has some life
            # left we can switch it in to the machine and use it
            int_pieces = int(toollife_remain / self.tools_with_time[i])
            raw_pieces = toollife_remain / self.tools_with_time[i]

            if int_pieces < raw_pieces:
                time_minutes.append(int_pieces + 1)
            else:
                time_minutes.append(int_pieces)

        for tools, pieces in zip(self.tools_with_time.keys(), time_minutes):
            self.piece_count[tools] = pieces

        """Calculate maximun number of pieces based off max tool life"""

        time_minutes = []  # Holds timeinfo in minutes instead of seconds
        for i in self.tools_with_time.keys():

            toollife_remain = tooltable[f'T{i}'][3]

            # Shaving of an S before we convert to float, and then converting minutes to seconds
            toollife_remain = float(toollife_remain[1:]) * 60

            # Dividing remining tool life with machining time to get the piece count
            time_minutes.append(int(toollife_remain / self.tools_with_time[i]))

        for tools, pieces in zip(self.tools_with_time.keys(), time_minutes):
            self.max_piece_count[tools] = pieces

    def specified_number(self, number: int):
        """ This method is for the tab TM Addition 1. You specify the number of pieces you want
            to machine, and we bring you the tools that either needs to be replaced or the ones
            that dont have the required tool life length """
        pass


if __name__ == '__main__':

    fil1 = Path('./Filehandling/Tools.txt')
    fil2 = Path('./Filehandling/Time.txt')
    # config_path = Path('./Config/Toolmonitor.ini')

    test = GibbsCam(Path('C:/Users/heiv085/Documents/Github/ToolMonitor/Config/Toolmonitor.ini'))
    # test.tool_data()
    test._pieces()

    print(test.tools_with_time, '\n', test.total_time)
