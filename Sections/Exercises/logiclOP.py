#wizard game

is_magician = False
is_expert = True

#check if magician AND Expert: 'master magician'

#check if magician but not expert: 'at least your getting there'

#if your not a magician: 'you need magic power'

if is_magician and is_expert:
    print("You are a master magician")

elif is_magician and not is_expert:
    print("At least your getting there")

elif not is_magician:
    print("You need magic powers !")