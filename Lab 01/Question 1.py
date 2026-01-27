name = input("Enter student name: ")
marks = int(input("Enter marks: "))
print("Student name:", name)
print("Marks:", marks)

if marks > 100:
    print("Invalid marks")
else:
    if marks >= 85:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")
