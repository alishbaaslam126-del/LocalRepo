# For loop
marks =[80,35,60,25,90]

for mark in marks:
    if mark >= 50:
        print(marks,"Pass")
    else:
        print(mark,"Fail")

print()
     #while loop
marks =50

while marks <= 100:
    print(marks)
    marks +=10

#Break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

#Continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Loop else
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")

    #While loop else
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Finished")