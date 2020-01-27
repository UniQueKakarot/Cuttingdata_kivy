from pathlib import Path


class Formatter:

    def __init__(self, tooltable_file):

        self.rawfile = tooltable_file
        self.filecontent = []
        self.tool_list = []
        self.tooldata = {}
        self.end_tool = None

        self.test()

    def test(self):

        with open(self.rawfile) as file_content:
            for i in file_content:
                i = i.strip('\n')
                i = i.strip()
                self.filecontent.append(i)

        for i in range(4):
            self.filecontent.pop(0)

        idx = 0
        while self.filecontent[idx][0] == 'S':
            tool = self.filecontent[idx].split('T')
            self.tool_list.append('T' + tool[1])
            idx += 1

        self.end_tool = self.filecontent[idx - 1].split('T')
        self.end_tool = 'T' + self.end_tool[1]

        m53_flag = 0
        m93_flag = 0
        info = []
        for i in self.tool_list:
            count = 0
            for j in self.filecontent:
                if j == 'M53':
                    m53_flag = 1
                elif j == 'M93':
                    m93_flag = 1

                if i in j:
                    if m53_flag:
                        info.append(j + self.filecontent[count+1] + self.filecontent[count+2])
                        m53_flag = 0
                    elif m93_flag:
                        info.append(j + self.filecontent[count+1])
                        m93_flag = 0
                    else:
                        info.append(j)
                count += 1

            self.tooldata[i] = info
            info = []

        print(self.end_tool)
        print(self.filecontent)
        print(self.tooldata)


if __name__ == '__main__':

    tooltable = Path('./1000')
    Formatter(tooltable)
