'''
Program: Words after "G"/"g"

Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z

Sample input:
enter a 1 sentence quote, non-alpha separate words: Wheresoever you go, go with all your heart

Sample output:

WHERESOEVER
YOU
WITH
YOUR
HEART

'''

string = input('enter a 1 sentence quote, non-alpha separate words:').upper() + " "

word = ''
for char in string: 
    if char.isalpha():
        word += char
    elif not word or word[0] >= "H":
        if not word:
            pass
        else:
            print(word)
        word = ''
    else:
        word = ''
        

# with regular expression

import re 
word = input("enter a 1 sentence quote, non-alpha separate words:") 
string = re.findall(r"[\w']+", word) 
for char in string:     
    if re.match('^[h-zH-Z]', char):         
        print(char.upper())
