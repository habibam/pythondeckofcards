class Card(object):
    def __init__(self, suit, cNumOrFace, value):
        self.suit = suit
        self.cNumOrFace = cNumOrFace
        self.value = value


    def getCardValue(self): #returns a numerical value based on cardFace value (mostly for the royalty)
        if isinstance(self.cNumOrFace, str):
            if(self.cNumOrFace == "Jack"):
                return 10
            elif(self.cNumOrFace == "Queen"):
                return 10
            elif(self.cNumOrFace == "King"):
                return 10
            elif(self.cNumOrFace == "Ace"):
                return [11]
        else:
            return self.cNumOrFace

    def display(self):
        print "{} of {}".format(self.cNumOrFace, self.suit)
        return self

if __name__ =="__main__":
    c1 = Card("heart", "ace", 11)
    c1.display()