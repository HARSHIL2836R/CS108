## Dynamicness of Python's variables

x = 5
print("Initial x:", x, "Type:", type(x))

x = "Hello"
print("Updated x:", x, "Type:", type(x))

## Casting in Python

a = str(3)      # a will be '3'
# b = int("3.5")  # error
b = int(float("3.5"))  # b will be 3
c = float("2")  # c will be 2.0

print("a:", a, "Type:", type(a))
print("b:", b, "Type:", type(b))
print("c:", c, "Type:", type(c))

## Multiple Assignment

name, age, city = "John", 25, "New York"
print("Name:", name, "Age:", age, "City:", city)

''' Initial x: 5 Type: <class 'int'>
Updated x: Hello Type: <class 'str'>
a: 3 Type: <class 'str'>
b: 3 Type: <class 'int'>
c: 2.0 Type: <class 'float'>
Name: John Age: 25 City: New York '''
