#IF , ELIF,ELSE
marks=75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")

else:
    print("Grade C")

print()
       #NESTED IF
marks = 75

if marks >= 50:
    print("Pass")

    if marks >= 80:
        print("Gade A")
    else:
        print("Grade B")
else: 
    print("Fail")

print()

        #for loop
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