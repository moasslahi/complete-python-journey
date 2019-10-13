#enumerate
#gives you index counter

for i,char in enumerate('Hello'):
    print(i, char)

#exercise to find the index of 50
for i, char in enumerate(list(range(100))):
    if char ==50:
        print(f'the index of 50 is: {i}')
