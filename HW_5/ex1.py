#exercise1
"""
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""
import re
pattern = input('Enter a pattern: ')
if re.search(r'a(b*)', pattern):
    print('Match found!')
else:
    print('No match found.')    


# #exercise2
"""
Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
"""
import re

string = input("Enter a string: ")

if re.search(r'a(b{2,3})', string):
    print("Match found!")
else:
    print("No match found.")

#exercise 3
"""
Write a Python program to find sequences of lowercase letters joined with a underscore.
"""
import re

string1  = input('Enter a string: ')
if re.findall("[a-z]_[a-z]{1}", string1):
    print('Match found!')
else:
    print('No match found.')    


#exercise 4
"""
Write a Python program to find the sequences of one upper case letter followed by lower case letters.
"""
import re
string2 = ('Enter a string: ')
if  re.findall("[A-Z][a-z]+", string2):
    print('Match found!')
else:
    print('No match found.')



#exercise 5
"""
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
"""
import re
string3 = ('Enter a string: ')
if re.findall('a[^ b]*b', string3):
    print('Match found!')
else:
    print('No match found.')


#exercise 6
"""
Write a Python program to replace all occurrences of space, comma, or dot with a colon.
"""
import re
string4 = ('Enter a string: ')
if  re.sub("[ ,.]", ":", string4):
    print('Match found!')
else:
    print('No match found.')

#exercise 7
"""
Write a python program to convert snake case string to camel case string.
"""

import re
test_str = input()
print("The original string is : " + str(test_str))
init, *temp = test_str.split('_')
res = ''.join([init.lower(), *map(str.title, temp)])
print("The camel case string is : " + str(res))


#exercise 8
"""
Write a Python program to split a string at uppercase letters.
"""
import re
string5 = input(('Enter a string: '))
if  re.findall('[A-Z][^A-Z]*', string5):
    print('Match found!')
else:
    print('No match found.')


#exercise 9
"""
Write a Python program to insert spaces between words starting with capital letters.
"""
import re

def insert_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

text = input()
formatted_text = insert_spaces(text)
print(formatted_text) 


#exercise 10
"""
Write a Python program to convert a given camel case string to snake case.
"""
def camel_to_snake(text1):
    
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text1).lower()

text1 = input()
snake_case_text = camel_to_snake(text1)
print(snake_case_text)  








