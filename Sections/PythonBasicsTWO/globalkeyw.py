# global word

total = 0

def counter():
    global total
    total += 1
    return total

print(counter())

