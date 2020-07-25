import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz1234567890!?.,'
length = input('password length?')
length = int(length)
n = int(input('HOw many passwords do you require?'))
for p in range(n):
    password=''
    for c in range(length):
        password += random.choice(chars)

    print(password) 