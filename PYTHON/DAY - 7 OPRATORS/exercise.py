a = input("Enter the number of a: ")
b = input("Enter the number of b: ")

print("Choose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    result = float(a) + float(b)
    print("The result of addition is:", result)

elif choice == '2':
    result = float(a) - float(b)
    print("The result of subtraction is:", result)

elif choice == "3":
    result = float(a) * float(b)
    print("The result of multiplication is:", result)

elif choice == "4":
    if float(b) != 0:
        result = float(a) / float(b)
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")

        