# Ceci est un commentaire sur une ligne
"""
    Ceci est un long long
    commentaire sur plusieurs
    lignes
"""

"""
    Take input from a user
"""
print("Welcome new user!!")

last_name = input("Enter your last name:")
first_name = input("Enter your first name:")

fullname = last_name + " " + first_name

print("So your name is " + fullname)

age = input("How old are you?")
age = int(age)

print(type(age))
print("So you are",age)