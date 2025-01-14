class Soda:
    def __init__(self, add=None):
        self.add=add

    def ShowMyDrink(self):
        if self.add is not None:
            print("soda and ", self.add)
        else:
            print("standart")

soda=Soda(2)
soda.ShowMyDrink()