# Tuple
# like lists but cant be modified 
#immutable
#why? = so others know it shouldnt be changed => safer ,
# predictable but less flexible, fatser than list

my_tuple = (1,2,3)
#my_tuple[1] = 'a'
# this is wrong => error 

#methods
#1 count()
print(my_tuple.count(1))

#2 index()
print(my_tuple.index(3))

#3 len()
print(len(my_tuple))