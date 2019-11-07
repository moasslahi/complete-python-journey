# arguemnt and key word argument

#*args #and #**kwargs

def super_func(*args, **kwargs): # this can accept as many as i want
    total = 0
    for items in kwargs.values():
        total+= items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

#rule(order): params, *args, default paramaterts, **kwargs
