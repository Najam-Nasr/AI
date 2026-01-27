n = int(input("Enter a number: "))
count = 0
print("Even numbers:", end=" ")

for i in range(2, n + 1, 2):
    print(i, end=" ")
    count += 1

print("\nTotal even numbers:", count)
