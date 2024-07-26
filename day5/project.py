from random import choice,shuffle
from string import ascii_letters, digits, punctuation

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

password = list()

for i in range(0,nr_letters):
    password.append(choice(ascii_letters))

for i in range(0,nr_symbols):
    password.append(choice(digits))

for i in range(0,nr_symbols):
    password.append(choice(punctuation))

shuffle(password)

for p,v in enumerate(password):
    print(v,end='')