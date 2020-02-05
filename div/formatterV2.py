from pathlib import Path

# This one is working as intended now


class Formatter:

    def __init__(self, tooltable_file):

        self.rawfile = tooltable_file
        self.filecontent = []
        self.tool_list = []
        self.pot_list = []
        self.tooldata = {}
        self.end_tool = None

        self.file_toolid()

    def file_toolid(self):

        # Reading in the raw file to a list and removing unnecessary whitespace
        with open(self.rawfile) as file_content:
            for i in file_content:
                i = i.strip('\n')
                i = i.strip()
                self.filecontent.append(i)

        # Popping off the first 4 elements, which is lineust unnecessary file header information
        for i in range(4):
            self.filecontent.pop(0)

        # Find all lines starting with S. Lines starting with S should only appere first in the file
        # because S denotes the tools Pot number in the magazine. Split on T which is the denote for Tool
        # and build a list of all tool id's 
        idx = 0
        while self.filecontent[idx][0] == 'S':
            tool = self.filecontent[idx].split('T')
            self.tool_list.append('T' + tool[1])
            self.pot_list.append(tool[0])
            idx += 1

        # Find the last tool number, we might use it to denote an end to a row in the tool table
        self.end_tool = self.filecontent[idx - 1].split('T')
        self.end_tool = 'T' + self.end_tool[1]

        # The flags are for segments that have information regarding a tool that does not fall on the same line
        # because of this we have to append info which is either one line ahead or two lines ahead.
        # for each toolid we build a dict with toolid and relevant tool data for that tool 
        m53_flag = 0
        m93_flag = 0
        info = []
        for toolid in self.tool_list:
            count = 0
            for line in self.filecontent:
                if line == 'M53':
                    m53_flag = 1
                elif line == 'M93':
                    m93_flag = 1

                file_toolid = line.split('S')

                if file_toolid[0] == toolid:
                    if m53_flag:
                        info.append(self.filecontent[count+1])
                        info.append(self.filecontent[count+2])
                        m53_flag = 0
                    elif m93_flag:
                        info.append(self.filecontent[count+1])
                        m93_flag = 0
                    else:
                        info.append(f'S{file_toolid[1]}')
                count += 1

            self.tooldata[toolid] = info
            info = []

        with open('.\div\self.tool_list.txt', 'w') as file1:
            for i in self.tool_list:
                file1.write(i + '\n')

        with open('.\div\self.pot_list.txt', 'w') as file1:
            for i in self.pot_list:
                file1.write(f'{i}\n')

        with open('.\div\self.filecontent.txt', 'w') as file1:
            for i in self.filecontent:
                file1.write(i + '\n')

        with open('.\div\self.tooldata.txt', 'w') as file1:
            for i in self.tooldata:
                file1.write(f'{i}: {self.tooldata[i]}\n')

        #print(self.end_tool)
        #print(self.tool_list)
        #print(self.filecontent)
        #print(self.tooldata)
        print('Done')


if __name__ == '__main__':

    tooltable = Path('./div/1000')
    Formatter(tooltable)
