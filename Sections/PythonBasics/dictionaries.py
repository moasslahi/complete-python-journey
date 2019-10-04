# Dictionary
#data type + data structure
#organize our data 
#key and value pair 
#unordered !

myDict = [
    {
    'name': 'Mo',
    'age': 20,
    'number': [1,2,3]
    },
    {
    'name': 'Ahmed'
    }
]

print(myDict[0]['name'])
print(myDict[1]['name'])

#------------------------

# dictionary methods 1

# 1)get method
user = {
    'name': 'Mo'
}
print(user.get('name')) 

# to create dict = not common 
user2 = dict(name='Ahmed')
print(user2)

#------------------------

#dictionary methods 2 
user3 = {
    'name': 'Mo',
    'age': 20
}
#to check if a key exists
print('name' in user3)

#to check if a value exists
print(20 in user3.values())

#item() grabs the entire item
print(user3.items())

# update()
print(user3.update({'age': 55}))
print(user3)