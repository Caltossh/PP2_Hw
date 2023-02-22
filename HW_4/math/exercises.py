#ex1
"""
Input degree: 15
Output radian: 0.261904
"""
import math
a = int(input())
print(math.radians(a))

#ex2
"""
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""
import math
height = int(input())
first_value = int(input())
second_value = int(input())
area_formula = ((first_value +second_value)/2)* height
print(area_formula)

#ex3
"""
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
import math
number_of_side = int(input())
size_of_side = int(input())
p = number_of_side*size_of_side
print("perimeter - ", p)
print("tang - ", round(math.tan(math.radians(180/number_of_side))))
apothem = (size_of_side)/2*round(math.tan(math.radians(180/number_of_side)))
print("apothem - ", apothem)
area = (p*apothem)/2
print(area)


#ex4
"""
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
"""
size_base = int(input())
height_p = int(input())
area_p = size_base * height_p
print(area_p)