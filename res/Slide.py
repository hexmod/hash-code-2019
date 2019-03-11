
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

    def getTags(self):
        if len(self.pics) == 2:
            return list(set(self.pics[0].getTags() + self.pics[1].getTags()))
        else:
            return self.pics[0].getTags()

    def calculateScore(self, slide):
        aa = len(set(self.getTags()).intersection(set(slide.getTags())))
        diff1 = len(set(self.getTags()).difference(set(slide.getTags())))
        diff2 = len(set(slide.getTags()).difference(set(self.getTags())))
        return min(aa, diff1, diff2)


