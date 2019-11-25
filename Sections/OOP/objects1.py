# OOP

# wizard game


class PlayerCharacter:
    def __init__(self, name, age):  # constructor method
        self.name = name  # properties of objects
        self.age = age

    def run(self):
        print('run!')
        return 'done'


player1 = PlayerCharacter('Mo', 18)
player2 = PlayerCharacter('Ahmed', 16)

print(player1.run())
print(player1.age)
print(player2.age)
