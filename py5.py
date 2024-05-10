
class Finder():

    def __init__(self):
        self.createList()

    def createList(self):
        self.myList=list((input("List daxil edin :").split(',')))

    def find(self,target):
        self.target=target
        self.index=False
        for i in range(len(self.myList)) :
            for j in range(i+1,len(self.myList)):
                if self.target==int(self.myList[i])+int(self.myList[j]):
                    print("Listin {} ve {} indeksindeki elementlerin cemi hedefe beraberdir".format(i,j))
                    self.index=True
                    break
        if not self.index:
            return -1           

finder=Finder()
#finder.find(9)
