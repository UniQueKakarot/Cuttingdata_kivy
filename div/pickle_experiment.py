""" This is a test regarding to internalizing data storage in the TPV/Cuttingdata application """

import pickle


class Database:

    def __init__(self):

        self.new_tooltable = {}
        self.old_tooltable = {}