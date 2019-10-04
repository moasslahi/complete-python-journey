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

#---------------------------
#set methods 2 
myset = {1,2,3,4,5}
yourset = {4,5,6,7,8,9,10}

#.differnece()
print(myset.difference(yourset))

#.discard
print(myset.discard(1))

#.difference_update()
print(myset.difference_update(yourset))

#.intersection()
print(myset.intersection(yourset))

#isdisjoin()
print(myset.isdisjoint(yourset))
#or
print(myset | yourset)

#.union
print(myset.union(yourset))

#issubset
print(myset.issubset(yourset))

#issuperset
print(yourset.issuperset(myset))
