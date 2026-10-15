#List
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])

fruits.append("orange")
fruits.remove("banana")

print(fruits)

#Tuple
numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[1])
print(len(numbers))

#Set
numbers = {10, 20, 20, 30, 40}

print(numbers)

numbers.add(50)
numbers.remove(10)

print(numbers)

#Dictionary
student = {
    "name": "Alishba",
    "age": 18,
    "marks": 85
}

print(student["name"])
print(student["marks"])

student["age"] = 19
student["grade"] = "A"

print(student)