"""
    Variables naming:
        - starts with any lowercase letter
        - Separate words with underscore
        - Can contain digits, but not at the beginning

    types in python:
        - str:(chaine de caractères){
            methods : len --> size of a str
                      rstrip,lstrip,strip --> remove whitespaces  
        }
        - int:(Nombre entier)
        - float:(Nombre à virgule)
"""
last_name = 'Mike'
first_name = 'Luke'
sentence = "This isn't right"

print(sentence)

age = 22

print(age)

height = 1.76
# Concatenation
full_name = last_name + ' ' + first_name 

print(type(last_name))

last_name = 40

print(type(last_name))