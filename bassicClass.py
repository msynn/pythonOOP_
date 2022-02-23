class User:
    def __init__(self, name, damage, role):
        self.name = name   # zilong, aurora
        self.damage = damage   # 100, 200
        self.role = role   # assassin, mage, warrior
# name, role, damage

zilong = User("zilong", 100, "assassin")
aurora = User("aurora", 200, "mage")

print(zilong.name)
print(zilong.damage)
print(zilong.role)
