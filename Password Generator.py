import random
import string
print("------Password Generator------")
length=int(input("Password length:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password+=random.choice(characters)
print("Generate password:",password)
