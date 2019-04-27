import os


class Musicchange():
    def __init__(self):
        self.l=[]
        for i in os.listdir("music/"):
            if os.path.splitext(i)[1] == ".mp3":
                self.l.append(i)
        self.flag = 0

    def changemu(self):
        if self.flag < len(self.l):
            i = self.l[self.flag]
            self.flag += 1
            return i
        else:
            self.flag = 0
            return self.l[0]