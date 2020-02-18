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



        self.generate_data(raw_tooltable)

        # Self.data should after this hold the formatter object with its "public" methods which contain lists and dicts
        # with tool information

    def generate_data(self, raw_tooltable):

        self.data: object = Formatter(raw_tooltable)

    def work_magic(self):

        """  """
        pass


if __name__ == '__main__':
    path1 = Path('./div/1000')
    path2 = Path('./div/Database.p')
    if path2.is_file():
        test = pickle.load(path2)
        test.generate_data(path1)
    else:
        instance1 = Database(path1)
