# for loops
# allows us to iterate through list of items
for x in range(1,10):
	print(x) 

# iterable = loops over

for item in "Mo Asslahi":
	print(item)

for item in [1,2,3,4,5]:
	print(item)

# nesting 
for item in (1,2,3):
	for x in ['a','b','c']:
		print(item,x)

# iterable 
#collection of item that can be iterated over 
# can go one by one to check each item in the collection

#iterating an object 

user1 = {
	'name': 'Mo',
	'Age': 20,
	'can_swim': False
}
for item in user1:   # printing the keys 
	print(item)

# to print the values 
for item in user1.items():   # printing the values
	print(item)              # or use .values()

# to print seperately
for item in user1.items():
	key, value = item;
	print(key, value)

# short hand way
for key, value in user1.items():
	print(key, value)




	