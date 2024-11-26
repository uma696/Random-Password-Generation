print("RANDOM PASSWORD GENERATION")

print("WELCOME")

import random
import string

#the shuffle function -created for shuffling the password,
def shuffle(strings):
    templist = list(strings)
    random.shuffle(templist)
    return templist

#**Password letters generation**
alphabets = list(string.ascii_letters)
#print(alphabets)
letters = int(input("how many letters you require in your password ?: "))
myalphalist = random.choices(alphabets,k=letters)
#print(f"Chosen Alphabets list = {myalphalist}")

#**Password numbers generation**
Numbers = list(string.digits)
#print(Numbers)
digits= int(input("how many digits/numbers you require in your password ?: "))
mydigitslist = random.choices(Numbers,k=digits)
#print(f"Chosen Digits list = {mydigitslist}")

#**Password punctuation generation**
specialchars = list(string.punctuation)
#print(specialchars)
punctuations = int(input("how many special chars you require in your password ?: "))
myspecialcharslist = random.choices(specialchars,k=punctuations)
#print(f"Chosen Punctuation list = {myspecialcharslist}")

#Concatenating the characters, digits and special chars in the password
password1 = myalphalist + myspecialcharslist + mydigitslist

#calling the shuffle function to shuffle the password
password = shuffle(password1)

#The Shuffled password will be a list, now converting list to string with 'join' function
Random_password = ''.join(password)

print(f"Generated password : {Random_password}")







