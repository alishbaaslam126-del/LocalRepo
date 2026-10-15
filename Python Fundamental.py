#Question # 1 The bill splitter

bill = float(input("Enter the total bill amount: "))
tip = float(input("Enter the tip percentage: "))
people = int(input("Enter the number of people to split the bill: "))

total_tip = bill * tip / 100
total_bill = bill + total_tip
if people > 0:
    amount_per_person = total_bill / people

    print("Tip:", total_tip)
    print("Total Bill:", total_bill)
    print("Each person pays:", amount_per_person)

else:
    print("Number of people must be greater than 0")

#Question #2 #Password Strength Checker

password = input("Enter your password: ")

upper = any(ch.isupper() for ch in password)
lower = any(ch.islower() for ch in password)
number = any(ch.isdigit() for ch in password)

if len(password) < 6:
    print("Weak Password")
elif len(password) >= 8 and upper and lower and number:
    print("Strong Password")
else:
    print("Moderate Password")

#Question#3 The Guessing Game

secret = 42
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number (1-100): "))

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100")
        continue

    attempts += 1

    if guess == secret:
        print("Correct! won!")
        break
    else:
        print("Wrong guess! Attempts used:", attempts)

else:
    print("Game Over! Lost!.")

#Question 4: String Slicer & Manipulator

name = input("Enter your full name: ").strip()
parts = name.split()

if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]

    print("Initials:", first_name[0].upper() + ". " + last_name[0].upper() + ".")
    print("Uppercase:", name.upper())
    print("Reversed:", name[::-1])
else:
    print("Please enter your first and last name.")

#Question 5: Global vs. Local Bank

bank_balance = 5000

def deposit(amount):
    global bank_balance
    bank_balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global bank_balance

    if amount <= bank_balance:
        bank_balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance!")

deposit(1000)
withdraw(2000)

print("Updated balance:", bank_balance)

#Question 6: Unique Character Counter

sentence = input("Enter a sentence: ")

characters = set(sentence.replace(" ", ""))

print("Unique characters:", characters)
print("Total unique characters:", len(characters))

#Question 7: The Student Grading System

students = {
    "Ali": 85,
    "Ayesha": 92,
    "Ahmed": 76,
    "Sara": 65,
    "Usman": 45
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"

    print(name, "-", marks, "-", grade)





