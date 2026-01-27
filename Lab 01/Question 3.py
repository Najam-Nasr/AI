names = []
marks = []

for i in range(3):
    name = input("Enter student name: ")
    mark = input("Enter marks: ")
    names.append(name)
    marks.append(mark)

print("Student Records:")
for i in range(3):
    print(names[i], marks[i])
