print("RANDOM PASSWORD GENERATION")

print("WELCOME")

import random
import string

#the shuffle function defined by passing the password,
# the function returns a string in single quotation which is joined
def shuffle(strings):
    templist = list(strings)#As shuffle function works with mutable.
# Lists are mutable,A list object is a collection which is ordered and changeable.
# so Im creating a list object with list()
    random.shuffle(templist)
    return templist

#**Password letters generation**
alphabets = list(string.ascii_letters)
#print(alphabets)
letters = int(input("how many letters you require in your password ?: "))
myalphalist = random.choices(alphabets,k=letters)
print(f"Chosen Alphabets list = {myalphalist}")

#**Password punctuation generation**
specialchars = list(string.punctuation)
#print(specialchars)
punctuations = int(input("how many special chars you require in your password ?: "))
myspecialcharslist = random.choices(specialchars,k=punctuations)
print(f"Chosen Punctuation list = {myspecialcharslist}")

#**Password numbers generation**
Numbers = list(string.digits)
#print(Numbers)
digits= int(input("how many special chars you require in your password ?: "))
mydigitslist = random.choices(Numbers,k=digits)
print(f"Chosen Digits list = {mydigitslist}")

#Concatenating the characters, digits and special chars in the password
password1 = myalphalist + myspecialcharslist + mydigitslist

#calling the shuffle function to shuffle the password
password = shuffle(password1)

#The Shuffled password will be a list, now converting list to string with 'join' function
Random_password = ''.join(password)

print(f"Generated password : {Random_password}")






