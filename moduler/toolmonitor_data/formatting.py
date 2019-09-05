
""" Takes in the raw tool list the machine spits out and formats it to a workable format """

from pathlib import Path

class FileFormatter():

    def __init__(self, raw_filename, filename):
        self.formatting = []
        self.header = []
        self.table = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]

        self._input_to_csv(raw_filename, filename)
        self.formatted_to_table(filename)

    def _input_to_csv(self, raw_filename, filename):

        with open(raw_filename) as file1:

            for lines in file1:

                tool_table = list(lines)
                try:
                    t_index = tool_table.index('T')
                except ValueError:
                    t_index = -1

                try:
                    s_index = tool_table.index('S')
                except ValueError:
                    s_index = -1


                if t_index > 0 and t_index < 5:
                    tool_table.insert(t_index, ',')
                    #file1.writelines(tool_table)
                    self.formatting.append(tool_table)

                elif s_index > 0 and s_index < 5:
                    tool_table.insert(s_index, ',')
                    #file1.writelines(tool_table)
                    self.formatting.append(tool_table)

                elif t_index == 0:
                    #file1.writelines(tool_table)
                    self.formatting.append(tool_table)

                elif s_index == 0:
                    #file1.writelines(tool_table)
                    self.formatting.append(tool_table)

        with open(filename, 'w') as file2:

            for i in self.formatting:

                i.pop()

                try:
                    i.remove(' ')
                except:
                    pass

                file2.writelines(i)
                file2.writelines('\n')

    def formatted_to_table(self, filename):

        """ Iterating through the raw list in blocks of 128, and appending each block 
            to its own list in a list """

        with open(filename) as file2:

            switch = 0
            switch_4 = 0
            switch_5 = 0

            for _ in range(2000):

                value = file2.readline()
                value = value.split(',')

                if switch == 0:

                    # Pot number and Tool number

                    self.table[0].append(value[0])

                    self.table[1].append(value[1].strip())

                elif switch == 1:

                    if value[1].strip() == 'T295':
                        pass
                    else:
                        self.table[2].append(value[1].strip())

                elif switch == 2:

                    self.table[3].append(value[1].strip())


                elif switch == 3:

                    self.table[4].append(value[1].strip())

                elif switch == 4:

                    if value[0][0] == 'T':
                        pass
                    elif switch_4 == 1:
                        self.table[5].append(value[0].strip())
                    elif switch_4 == 2:
                        self.table[6].append(value[0].strip())

                    switch_4 += 1

                    if switch_4 > 2:
                        switch_4 = 0

                elif switch == 5:
                    if switch_4 == 1:
                        self.table[5].append(value[0].strip())
                    elif switch_4 == 2:
                        self.table[6].append(value[0].strip())

                    switch_4 += 1

                    if switch_4 > 3:
                        if switch_5 == 1:
                            self.table[7].append(value[0].strip())

                        switch_5 += 1

                        if switch_5 > 1:
                            switch_5 = 0

                elif switch == 6:

                    if switch_5 == 1:
                        self.table[7].append(value[0].strip())
                    elif switch_5 > 1:
                        self.table[8].append(value[1].strip())

                    switch_5 = 2

                elif switch == 7:
                    self.table[9].append(value[1].strip())

                elif switch == 8:
                    self.table[10].append(value[1].strip())

                elif switch == 9:
                    self.table[11].append(value[1].strip())

                elif switch == 10:
                    self.table[12].append(value[1].strip())
                
                elif switch == 11:
                    self.table[13].append(value[1].strip())

                if value[0].strip() == 'S128':
                    switch += 1

                elif value[0].strip() == 'T295':
                    switch += 1

        return self.table

if __name__ == '__main__':

    #raw_data = Path('Q:/DNC/Mask20/1000')
    raw_data = Path('./1000')
    formatted_datafile = Path('./Filehandling/Formatted.csv')

    test1 = FileFormatter(raw_data, formatted_datafile)
    #test1.formatted_to_table(formatted_datafile)
    print(test1.table)
