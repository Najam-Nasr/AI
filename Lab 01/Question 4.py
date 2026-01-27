while True:
  print ("1. Add two numbers: ")
  print ("2. Subtract two numbers: ")
  print ("3. Exit")
  choice = int (input ("Enter your choice: "))
  if choice == 1:
    a = int (input ("Enter first number: "))
    b = int (input ("Enter second number: "))
    Sum = a + b
    print ("Result = ", Sum)
  elif choice == 2:
    a = int (input ("Enter first number: "))
    b = int (input ("Enter second number: "))
    Sub = a - b
    print ("Result =", Sub)
  elif choice == 3:
    print ("Exit")
    break
  else:
    print ("Invalid input")
