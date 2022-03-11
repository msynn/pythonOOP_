# innerFunction
# fungsi di dalam fungsi
class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def info(self):
        def print_title():
            return f"Title : {self.title}"
        def print_price():
            return f"Price : {self.price}"
        
        return print_title() + "\n" + print_price()
        
            
print("")

zaoyu = Game("Mobile Legends", 32000)
title = zaoyu.info()
print(title)
