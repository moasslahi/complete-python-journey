#function that prints the highest even

def highes_even(li):
    evens = []     # empty variable so we can add to it later
    for items in li:
        if items % 2 == 0:  # to check if its even
         evens.append(items)  #then add it to the evens variable
    return max(evens)  #return themax even form the evens variable

print(highes_even([1,2,3,4,5,6,7,8]))

