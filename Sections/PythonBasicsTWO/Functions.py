# functions
# DRY
# functions are useful when have things that you
# want to use over and over

#creating functions
def say_hello():
    print("Hello")

# we have to call it WITH BRACKETS to run  
say_hello()



#-------------------------------------------


# paramter are name of variables we recieve
def say_hello(name):
    print(f'Hello {name}')


#argumemnt are actual values we provide to the function
say_hello('Mo') #call , invoke


#-----------------------------------------------------

# propositional arguments require to proper postion

# key word argumnets = not worry about the position 
say_hello(name='AHMED') # its bad practice = complicated code

# default argumemnts
