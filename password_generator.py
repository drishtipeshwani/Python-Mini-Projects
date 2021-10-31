import random

print('Welcome to random password generator')

passlength = int(input('Enter the length of password'))

s = "abcdefghijklmnopqrstuvwxyzABCBEFGHIJKLMNOPQRSTUVWXYZ@!*"

password = "".join(random.sample(s,passlength));

print(password)