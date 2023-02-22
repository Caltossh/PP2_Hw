#ex1
"""
1.Create a generator that generates the squares of numbers up to some number N.
"""
n = int(input())
squares_generator = (i * i for i in range(n))
for i in squares_generator:
    print(i, end =" ")


#ex2
"""
Write a program using generator to print the even numbers
 between 0 and n in comma separated form where n is input from console.
"""
def even_number(c):
    for i in range(0, c+1):
        if i%2 == 0:
            yield i
for k in even_number(int(input())):
    print(k, end = ',')
               

#ex3
"""
Define a function with a generator which can iterate the numbers,
 which are divisible by 3 and 4, between a given range 0 and n.
"""
def numbers(a):
    for i in range(0, a+1):
        if i%3 == 0 and i%4 == 0:
            yield i
for i in numbers(int(input())):
    print(i, end = ' ')

#ex4
"""
Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.
""" 
x = int(input())
y = int(input())  
def all_number(x, y):
    for i in range(x, y + 1):
        yield i**2

for i in all_number(x, y):
    print(i, end = " ")  

#ex5
"""
Implement a generator that returns all numbers from (n) down to 0.
"""
def allnum(z):
    for i in range(z, -1, -1):
        yield i 

for i in allnum(int(input())):
    print(i, end =' ')