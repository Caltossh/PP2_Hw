#exercise 1
def my_function():
    print("Hello from a function")

#exercise 2
def my_function():
    print("Hello from a function")
#name function: "my_function"

#exercise 3
def my_function(fname, lname):
  print(fname)
fname = "Salta"
lname = "Dina"
my_function(fname,lname)

#exercise 4
def my_function(x):
    return x + 5
x = 4
my_function(x)

#exercise 5
def my_function(*kids):
  print("The youngest child is " + kids[2])
kids = ("Dina", "Salta", "SSSS")

#exercise 6
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Dina", lname = "Salta")
