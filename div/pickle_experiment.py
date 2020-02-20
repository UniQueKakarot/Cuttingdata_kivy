""" This is a test regarding to internalizing data storage in the Tool life/Cuttingdata application """

import pickle
from pathlib import Path

from div.formatterV2 import Formatter

# New_tooltable dict is not neccessary since we can get fresh data directly from the formatter
# Store a list of Unused tools, used tools and special tools


class Database:

    """ The goal of this object is to store all data needed for the CncTools survailance tool,
        and then pickle it for persistant storage of data """

    def __init__(self, raw_tooltable):

        self.data = None

        self.new_tooltable: dict = {}
        self.old_tooltable: dict = {}

        self.used_tools = []
        self.unused_tools = []
        self.special_tools = []

        self.generate_data(raw_tooltable)
        self.generate_used_tools()

        # Self.data should after this hold the formatter object with its "public" methods which contain lists and dicts
        # with tool information

    def generate_data(self, raw_tooltable):

        """ Run the formatter to genereate new input """

        self.data: object = Formatter(raw_tooltable)

    def generate_used_tools(self):

        # The 4th element in the list is the toollife
        # print(len(self.data.tooldata))
        self.old_tooltable = self.data.tooldata


if __name__ == '__main__':
    path1 = Path('./1000')
    path2 = Path('./Database.p')
    if path2.is_file():
        instance1 = pickle.load(open(path2, 'rb'))
        print(instance1.old_tooltable)
    else:
        instance1 = Database(path1)

    pickle.dump(instance1, open(path2, 'wb'))
