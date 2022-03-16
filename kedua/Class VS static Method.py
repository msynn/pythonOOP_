import csv
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
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')), 
            )
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count ut the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        


Item.instantiate_from_csv()
print(Item.all)