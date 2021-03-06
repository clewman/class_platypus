#Password Generator
#By Skyler Parker
#Created on 14AUG18

import random
import string

appExit = False


def password_generator(length):
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)

    print(password)


def picky_password_generator(num_lowercase, num_uppercase, num_numbers):
    password = []
    for i in range(num_lowercase):
        password.append(random.choice(string.ascii_lowercase))

    for i in range(num_uppercase):
        password.append(random.choice(string.ascii_uppercase))

    for i in range(num_numbers):
        password.append(random.choice(string.digits))

    random.shuffle(password)
    password = ''.join(password)
    print(password)


while appExit != bool(True):
    menuAnswer = int(input('\nMenu:\n\n1 - Create New Password\n2 - Create New Custom Password\n3 - Close Program'))

    if menuAnswer == 1:
        length = int(input('How long would you like the password to be?'))
        password_generator(length)

    elif menuAnswer == 2:
        num_lowercase = int(input('How many lowercase letters would you like?'))
        num_uppercase = int(input('How many uppercase letters would you like?'))
        num_numbers = int(input('How many numbers would you like?'))
        picky_password_generator(num_lowercase, num_uppercase, num_numbers)

    else:
        appExit = True

