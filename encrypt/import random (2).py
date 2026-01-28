import random
import string

char = string.punctuation + string.digits + string.ascii_letters

char = list(char)
key = char.copy()

random.shuffle(key)

#print(char)
#print(key)

#encrpye
plane_text = input(": ")
cipher_text = ""

for letter in plane_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f"ecrypted text:{cipher_text}")

#decrpye 

cipher_text = input(": ")
plane_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plane_text += char[index]

print(f"ecrypted text:{plane_text} ")

exit = input(": ")




