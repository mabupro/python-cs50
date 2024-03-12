# Ask your for their name
# name = input("Whats's your name? ")
name = input("Whats's your name? ").strip().title()
# PS C:\Users\Bilde\Documents\GitHub\python-cs50> python hello.py
# Whats's your name? mano shinya
# hello, Mano Shinya


# Remove whitespace from str
# name = name.strip()
# PS C:\Users\Bilde\Documents\GitHub\python-cs50> python hello.py
# Whats's your name?         mano
# hello, mano
# PS C:\Users\Bilde\Documents\GitHub\python-cs50> python hello.py
# Whats's your name?     m    a n        o
# hello, m    a n        o



# Capitalize user's name

# name = name.capitalize()
# PS C:\Users\Bilde\Documents\GitHub\python-cs50> python hello.py
# Whats's your name? mano
# hello, Mano

# name = name.title()
# PS C:\Users\Bilde\Documents\GitHub\python-cs50> python hello.py
# Whats's your name? mano shinya
# hello, Mano Shinya



# Remove whitespace from str and capitalize user's name

# name = name.strip().title()



# Split user's name into first name and last name
first,last = name.split(" ")



# Say hello to user
# print("hello," + name)
# print("hello,", name)
# print("hello, ",end="")
# print(name)
# print("hello,", name, sep="!!!")
# print('hello, "friend"')
# print("hello, \"friend\"")
# print(f"hello, {name}")
print(f"hello, {first}")
