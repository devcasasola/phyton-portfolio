#PASSWORD GENERATOR BY @DEVCASASOLA
import random

print("Password Generator by @devcasasola")
print("Wellcome To Your Password Generator")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

number = input("Number of character of you can generate your password: ")
number = int(number)

length = input("Your password length: ")
length = int(length)

print("\nHere your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
