class Picture:

    def __init__(self, pictureString, id):
        parsed = pictureString.split(" ")
        self.orientation = parsed[0]
        self.noTags = parsed[1]
        self.tags = parsed[2:-1]
        # remove newline tag
        self.tags.append(parsed[-1][:-1])
        self.id = id

    def isVertical(self):
        return self.orientation == 'V'

    def getId(self):
        return self.id
