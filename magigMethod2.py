class Game : # class Game
    def __init__(self,tittle,price) : 
        self.tittle = tittle
        self.price = price

    def __str__(self) : # print
        return f"{self.tittle} - {self.price}"
    
    def __eq__(self, other) : # ==
        return self.tittle == other.tittle 

    def __gt__(self, other) : # > 
        return self.price > other.price 

    def __add__(self, other) : # +
        return self.price + other.price

zilong = Game("Mobile Legends", 32000)
zilong2 = Game("Mobile Legends", 34000)
luffy = Game("Bounty Hunter", 25000)


print(zilong2 == luffy) # zilong2 == luffy = False
print(zilong > luffy) # zilong > luffy = True
print(zilong + luffy) # zilong + luffy = 57000