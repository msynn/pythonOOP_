class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    def __init__(self, name: str , price: float, quantity=0):
        # Run validations to the received argument
        assert price >= 0, f"Price {price} is not greated than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greated or equal to zero!"
        
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Action to execute
        Item.all.append(self)
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        

item1 = Item("Phone", 200, 9)
item2 = Item("Laptop", 2000, 3)
item3 = Item("Mouse", 50, 10)
item4 = Item("Headset", 80, 4)
item5 = Item("Bag", 120, 8)

print(Item.all)