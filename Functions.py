#Functions
def greet():
    print("Hello World")

greet()

#with parameters
def add(a, b):
    print(a + b)

add(10, 5)

# Scope of Variables
def show():
    x = 10
    print(x)

show()

x = 20

def show():
    print(x)

show()
print(x)

#Assignment Operators
a = 10
print(a)
a += 5  # a = a + 5
print(a)
a -= 3  # a = a - 3
print(a)
a *= 2  # a = a * 2
print(a)
a /= 4  # a = a / 4
print(a)

#Logical Operators
x = 5
y = 10
print(x > 3 and y < 15)  # True
print(x > 3 or y > 15)   # True
print(not(x > 3))        # False

#Comparison Operators
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Arithmetic Operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)