class Cat:
    species = 'Mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Find the oldest cat


def oldest(*args):  # this takes many argument
    return max(args)  # prints the maximum


# Instantiate the Cat object with 3 cats
mo = Cat("Mo", 20)
loo = Cat("loo", 12)
foo = Cat("foo", 19)

# Output
print(f'The oldest cat is {oldest(mo.age,loo.age,foo.age)} years old')
