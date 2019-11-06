
age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too yound to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def CheckIfCanDrive():
    age = input("whats your age?")
    if int(age) < 18:
        print("Sorry cant drive")
    elif int(age) >= 18:
        print("Power on!")
    else:
        print("I am sorry but you just cant drive right now !")
CheckIfCanDrive()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def CheckIfCanDrive(age=0):
    if int(age) < 18:
        print("Sorry cant drive")
    elif int(age) >= 18:
        print("Power on!")
    else:
        print("I am sorry but you just cant drive right now !")
CheckIfCanDrive(12)1