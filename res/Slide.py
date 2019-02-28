
class Slide:

    def __init__(self, pic1=None, pic2=None):
        self.pics = [pic1]
        if pic2:
            self.noPics = 2
            self.pics.append(pic2)
        else:
            self.noPics = 1

    def getPictures(self):
        res = str(self.pics[0].getId())
        if len(self.pics) == 2:
            res += " " + str(self.pics[1].getId())
        return res


