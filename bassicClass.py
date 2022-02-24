class User:
    total = 0

    def __init__(self, name, damage, role):
        self.name = name   # zilong, aurora, argus, etc.
        self.damage = damage   # 100, 200, 300, etc.
        self.role = role   # assassin, mage, warrior, etc.
        User.total += 1
        
# instance variable VS class variable

zilong = User("zilong", 100, "assassin")
print(User.total)

aurora = User("aurora", 200, "mage")
print(User.total)

argus = User("argus", 300, "warrior")
print(User.total)