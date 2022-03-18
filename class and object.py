class GameCharacter:
    
    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount # Self.x_pos = self.x_pos + by_x_amount
        self.y_pos += by_y_amount # Self.y_pos = self.y_pos + by_y_amount

char1 = GameCharacter('Karakter1', 50, 100, 110, 120)
print(char1.name)
print(char1.width)
print(char1.height)
char1.name = 'Karakter baru'
print(char1.name)

char1.move(70, 80)
print(char1.x_pos)
print(char1.y_pos)