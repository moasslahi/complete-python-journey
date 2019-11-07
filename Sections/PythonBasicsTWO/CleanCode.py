#clean code

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2!=0:
        return False
is_even(50)


# to clean the code even more
def is_even_clean(num):
    return num % 2 == 0

print(is_even(50))