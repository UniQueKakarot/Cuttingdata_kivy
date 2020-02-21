""" This is a test regarding to internalizing data storage in the Tool life/Cuttingdata application """

import pickle
from pathlib import Path

from div.formatterV2 import Formatter

# New_tooltable dict is not neccessary since we can get fresh data directly from the formatter
# Store a list of Unused tools, used tools and special tools


class Database:

    """ The goal of this object is to store all data needed for the CncTools survailance tool,
        and then pickle it for persistant storage of data """

    def __init__(self):

        self.new_tooltable: dict = {}
        self.old_tooltable: dict = {}

        self.used_tools = []
        self.unused_tools = []
        self.special_tools = []
        self.special_tools_id = [str(toolid) for toolid in range(700, 721, 1)]  # Make this into a set instead


class DatabaseHandler:

    def __init__(self, raw_tooltable, database_path):

        self.data = None
        self.database_path = database_path

        self.generate_data(raw_tooltable)

        if database_path.is_file():
            self.database = pickle.load(open(database_path, 'rb'))
        else:
            self.database = Database()
            self.first_time_data()

    def generate_data(self, raw_tooltable):

        """ Run the formatter to genereate new input """

        self.data: object = Formatter(raw_tooltable)

    def first_time_data(self):

        """ This method should only run the very first time this object is invoked """

        self.database.old_tooltable = self.data.tooldata
        pickle.dump(self.database, open(self.database_path, 'wb'))

    def generate_tool_data(self):

        """ Generate all neccessary tool data here """

        # The 4th element in the list is the toollife
        self.database.used_tools.clear()

        for oldkey, newkey in zip(self.database.old_tooltable, self.data.tooldata):
            old_data = self.database.old_tooltable[oldkey]
            new_data = self.data.tooldata[newkey]

            # If remainig tool life is not the same = used, else = unused
            if new_data[4] != old_data[4]:
                self.database.used_tools.append(new_data[1])

            pickle.dump(self.database, open(self.database_path, 'wb'))

    def view_data(self):

        print(f'Used tools: {self.database.used_tools}')
        print(f'Unused tools: {self.database.unused_tools}')
        print(f'Special toolids: {self.database.special_tools_id}\n')


if __name__ == '__main__':
    path1 = Path('./1000')
    path2 = Path('./Database.p')

    instance1 = DatabaseHandler(path1, path2)

    terminate = 0
    while not terminate:

        print('Press 0 to exit')
        print("Press 1 to rerun generate_used_tools method")
        print("Press 2 to view data\n")
        choice = input()

        if choice == '0':
            terminate = 1
        elif choice == '1':
            instance1.generate_tool_data()
        elif choice == '2':
            instance1.view_data()

    # pickle.dump(instance1, open(path2, 'wb'))
