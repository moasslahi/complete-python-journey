# unordred collections of unique objects
# no duplicates 

my_set = {1,2,3,4,5}
print(my_set)

my_set.add('a')
print(my_set)

# if u had list of duplicates
# how would u return it without duplicates? 

my_set2 = {1,2,3,4,5,5,2}
print(set(my_set2))

# to check 
print(1 in my_set2)

#len 
print(len(my_set2))

