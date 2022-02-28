# StaticMethod

class User :
    total = 0
    def __init__(self, name, damage, role) :
        self.name = name  # zilong, aurora, argus, etc.
        self.damage = damage # 100, 200, 300, etc.
        self.__role = role  # assassin, mage, warrior, etc.
        User.total += 1 
    def info(self) : 
        return f"{self.name} - {self.__role} - {self.damage}"

    @property #
    def role(self) :
        return self.__role

    @role.setter
    def role(self, new_role) :
        if self.__role == "assassin" :
            self.__role = new_role
        else :
            print("Role anda tidak bisa diubah")

    @classmethod
    def setTotal(cls, total) :
        cls.total = total

    @classmethod
    def from_string(cls, string_param) :
        name, damage, role = string_param.split("-")
        return cls(name, int(damage), role)
    @staticmethod
    def tweet(word):
        return word

# zilong = User("zilong", 100, "assassin")
# argus = User.from_string("argus-300-warrior")

# print(argus.info())
# print("")
# print(User.total)
# User.setTotal(10)
# print(User.total)

tweet = User.tweet("Hallo sakina!")
print("")
print(tweet)