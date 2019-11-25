# OOP
# wizard game


class PlayerCharacter:
    # class Object attribute , its static, actual attribute on the class
    membership = True

    def __init__(self, name, age):  # constructor method
        if (self.membership):
            self.name = name  # properties of objects , dynamic and unique to that object
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Mo', 18)
player2 = PlayerCharacter('Ahmed', 16)

print(player1.shout())
