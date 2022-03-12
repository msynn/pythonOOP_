class Item:
    def __init__(self, name: str , price: float, quantity=0):
        # Run validations to the received argument
        assert price >= 0, f"Price {price} is not greated than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greated or equal to zero!"
        
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 200, 9)

item2 = Item("Laptop", 2000, 3)

print(item1.calculate_total_price())