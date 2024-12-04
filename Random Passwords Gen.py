print("RANDOM PASSWORD GENERATION DEPENDING ON USER REQUIREMENT")

print("WELCOME")

import random
import string

#the shuffle function -created for shuffling the password,
def shuffle(strings):
    templist = list(strings)
    random.shuffle(templist)
    return templist

#**Password letters generation with user requirement**
letters = int(input("how many letters you require in your password ?: "))
alphabets = list(string.ascii_letters)
myalphalist = random.choices(alphabets,k=letters)

#**Password numbers generation with user requirement**
digits= int(input("how many digits/numbers you require in your password ?: "))
Numbers = list(string.digits)
mydigitslist = random.choices(Numbers,k=digits)

#**Password punctuation generation with user requirement**
punctuations = int(input("how many special chars you require in your password ?: "))
specialchars = list(string.punctuation)
myspecialcharslist = random.choices(specialchars,k=punctuations)

#Concatenating the characters, digits and special chars in the password
password1 = myalphalist + myspecialcharslist + mydigitslist

#calling the shuffle function to shuffle the password
password = shuffle(password1)

#The Shuffled password will be a list, now converting list to string with 'join' function
Random_password = ''.join(password)

print(f"Generated password : {Random_password}")

