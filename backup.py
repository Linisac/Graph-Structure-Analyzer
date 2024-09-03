class sndCompColor:
    def __init__(self):
        self.numberOfColors = 0
        self.colorAndOccur = []
    def indexOf(self, color):
        numOfColors = self.numberOfColors
        if numOfColors == 0:
            return -1
        else:
            i = 0
            while (i < numOfColors):
                if color == (self.colorAndOccur[i])[0]:
                    return i
                i = i + 1
            return -1            
    def addColor(self, color):
        index = self.indexOf(color)
        if index == -1:
            self.colorAndOccur.append([color, 1])
            self.numberOfColors = self.numberOfColors + 1
        else:
            self.increment(index)
    def increment(self, ind):
        self.colorAndOccur[ind][1] = self.colorAndOccur[ind][1] + 1
    def flatten(self, level):
        collectionOfElements = []
        for i in range(self.numberOfColors):
            collectionOfElements.append(("COLOR: " + str(self.colorAndOccur[i][0]) + " OCCUR: " + str(self.colorAndOccur[i][1])))
        collectionOfElements.sort()
        return str(collectionOfElements)
    def __repr__(self):
        if self.numberOfColors == 0:
            return "Empty"
        else:
            message = ""
            for i in range(self.numberOfColors):
                message = message + "Color " + repr(i) + ": " + repr(self.colorAndOccur[i][0]) + "\nOccurrence(s): " + repr(self.colorAndOccur[i][1]) + "\n"
            return message
    def __str__(self):
        if self.numberOfColors == 0:
            return "Empty"
        else:
            message = ""
            for i in range(self.numberOfColors):
                message = message + "Color " + str(i) + ": " + str(self.colorAndOccur[i][0]) + "\nOccurrence(s): " + str(self.colorAndOccur[i][1]) + "\n"
            return message
