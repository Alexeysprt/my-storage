class Game:
    def __init__(self, name):
        self.__name=name

    def getName(self):
        return self.__name
    
    def setName(self, newname):
        self.__name=newname

game=Game("Uncharted")
print(game.getName())

game.setName("God of War")
print(game.getName()) 
print(game.__name) 