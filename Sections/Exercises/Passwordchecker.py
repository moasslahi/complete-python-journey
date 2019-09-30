#My solution

username = input('Whats your name ?')
password = input('whats your password ? ')
passwordconverted = len(password) * '*'

print(f'{username} , Password {passwordconverted} is {len(password)} letters long')


#Andrei's solution

username1 = input('what is your username')
password1 = input('what is your password')
password_length = len(password1)
hidden_password = '*' * password_length

print(f'{username1}, your password, {hidden_password}, is {password_length} letters long')

