#exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#exercise 5  
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)