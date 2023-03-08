#ex1

def num(list):
    answer = 1
    for i in list:
        answer *= i
    
    return answer

list = [int(input()) for i in range(int(input()))]

print(num(list))

#ex2

input1 = str(input())

cnt1 = 0
cnt2 = 0

for i in input1:
    if i.isupper():
        cnt1 += 1
    if i.islower():
        cnt2 += 1

print(cnt1, " ", cnt2)

#ex3
str = str(input())
str2=reversed(str)

if list(str)==list(str2):
    print("Palindrome")
else:
    print('Not palindrome')

#ex4
from time import sleep  
import math

number = int(input())
milliseconds = int(input())

sleep(milliseconds/1000)

print("Square root of {n} after {m} miliseconds is {sq}".format(n = number, m = milliseconds, sq = math.sqrt(number)))

#ex5
def true(tuple):
    for i in tuple:
        if not i:
            return False
    return True

tuple = (True, True)

print(true(tuple))