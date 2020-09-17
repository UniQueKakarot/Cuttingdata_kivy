""" This is a test regarding to internalizing data storage in the Tool life/Cuttingdata application """

import pickle
from pathlib import Path
import configparser

from moduler.toolmonitor_data.tooltable_formatter_a66 import Formatter

# New_tooltable dict is not neccessary since we can get fresh data directly from the formatter
# Store a list of Unused tools, used tools and special tools


class Database:

    """ The goal of this object is to store all data needed for the CncTools survailance tool,
        and then pickle it for persistant storage of data """

    def __init__(self):

        self.stored_tooltable: dict = {}

        self.used_tools: list = []  # Store tools that have their lifetime reduced
        self.unused_tools: set = set()  # A record of tools that have not been used
        self.special_tools: list = []  # A list of tool id's for swappable tools
        self.special_tools_id: set = {f'T{toolid}' for toolid in range(700, 721, 1)}  # Numbers considered for special tools

        self.raw_timedata: dict = {}  #
        self.timedata_results: dict = {}


class DatabaseHandler:

    def __init__(self, config_path):

        self.config_path = config_path

        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        # -----------------------------------------------------------------------------------------

        self.data = None
        # self.database_path = Path(self.config['Paths']['Rawdatabase'])
        self.database_path = Path('./moduler/toolmonitor_data/results/Database.p')

        # This is a fallback solution, if we dont have access to the network drive location
        # we use a local copy of the raw data table
        if Path(self.config['Paths']['Rawdata']).is_file():
            self.raw_tooltable = Path(self.config['Paths']['Rawdata'])
        else:
            self.raw_tooltable = Path('./moduler/toolmonitor_data/rawdata/1000')

        # -----------------------------------------------------------------------------------------

        self.generate_data(self.raw_tooltable)

        if self.database_path.is_file():
            try:
                self.database = pickle.load(open(self.database_path, 'rb'))
            except pickle.UnpicklingError:
                print('Handled a exception')
                self.database = Database()
                self.first_time_data()
        else:
            self.database = Database()
            self.first_time_data()

    def generate_data(self, raw_tooltable):

        """ Run the formatter to genereate new input """

        self.data: object = Formatter(raw_tooltable)

    def first_time_data(self):

        """ This method should only run the very first time this object is invoked """

        # Since this is the first run we dont have anything to compare with
        # so we just shuffle the the fresh tool table over to the old tool table
        self.database.stored_tooltable = self.data.tooldata

        # Add all tools in magazine to the unused tools list since we dont have
        # any data on what tools are used or not yet
        self.database.unused_tools = set(self.data.tool_list)

        pickle.dump(self.database, open(self.database_path, 'wb'))

    def generate_tool_data(self):

        """ Generate all neccessary tool data here """

        # The 4th element in the list is the toollife
        self.database.used_tools.clear()

        for oldkey, newkey in zip(self.database.stored_tooltable, self.data.tooldata):
            old_data = self.database.stored_tooltable[oldkey]
            new_data = self.data.tooldata[newkey]

            # If remainig tool life is not the same = used, else = unused
            if new_data[4] != old_data[4]:
                self.database.used_tools.append(new_data[1])
                # Check if used tool is in unused tools, if it is, remove it
                if new_data[1] in self.database.unused_tools:
                    self.database.unused_tools.remove(new_data[1])

            if new_data[1] in self.database.special_tools_id and new_data[1] not in self.database.special_tools:
                self.database.special_tools.append(new_data[1])

        # Move the freshly parsed toolinfo over to the old data once we are done processing it
        self.database.stored_tooltable = self.data.tooldata
        # Save the pickle file
        pickle.dump(self.database, open(self.database_path, 'wb'))

    def load_new_data(self):

        self.data = Formatter(self.raw_tooltable)

        if self.data.tooldata == self.database.stored_tooltable:
            print('No Changes to tooldata')
        else:
            self.generate_tool_data()

    def tool_table(self):

        return self.database.stored_tooltable

    def special_tools(self):

        return self.database.special_tools

    def view_data(self):

        print(f'Used tools: {self.database.used_tools}')
        print(f'Unused tools: {self.database.unused_tools}')
        print(f'Old Tooltable: {self.database.stored_tooltable}')
        print(f'Special tools in mag: {self.database.special_tools}')
        print(f'Special toolids: {self.database.special_tools_id}\n')


# if __name__ == '__main__':
#     path1 = Path('./1000')
#     path2 = Path('./Database.p')
#     path3 = Path('./1001')
#
#     test = 0
#     terminate = 0
#     while not terminate:
#
#         if test == 0:
#             instance1 = DatabaseHandler(path1, path2)
#             test = 1
#         else:
#             instance1 = DatabaseHandler(path3, path2)
#             test = 0
#
#         print('Press 0 to exit')
#         print("Press 1 to rerun generate_used_tools method")
#         print("Press 2 to view data\n")
#         choice = input()
#
#         if choice == '0':
#             terminate = 1
#         elif choice == '1':
#             instance1.generate_tool_data()
#         elif choice == '2':
#             instance1.generate_tool_data()
#             instance1.view_data()
#
#     # pickle.dump(instance1, open(path2, 'wb'))
