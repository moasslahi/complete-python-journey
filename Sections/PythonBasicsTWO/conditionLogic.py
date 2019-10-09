
#conditional

is_old = True
is_licenced = True

if is_old:
    print("Your old enough to drive")
else:
    print("Sorry you cant")

#elif 
if is_old:
    print("Your old enough to drive")
elif is_licenced:
    print("Go Go")
else:
    print("Sorry you cant")

# and keyword

if is_licenced and is_old:
    print('yes Go Go !')


# truthy value any string or num
# falsey 0 or an empty string

password = '123'
username = 'Mo'

if password and username:
    print('Hello')
else: 
    print('Wrong')
