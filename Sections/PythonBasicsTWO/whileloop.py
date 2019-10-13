#while loop 1

 #while condition:
     #do something

#infinte loop = program doesnt know when to stop

#break statment 

i = 0
while i < 50:
    print(i)
    i += 1

# else block will only excute if theresnt a break
#special case
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done!')

#---------------------------------------------
#while loop 2

#very flexible
#more powerful

#ALWAYS REMEBER TO INCREMENT
# DONT FORGET THE BREAK !
mylist = [1,2,3]

i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

#best way 
while True:
    response = input('Say Something: ')
    if (response == 'bye'):
        break

#----------------------------------------
#break, continue and pass

# break works in for loop
for item in mylist:
    print(item)
    break #breaks out of the loop

#continue 
for item in mylist:
    print(item)
    continue # back to the for loop

#pass passes to the next line 
#placeholder


