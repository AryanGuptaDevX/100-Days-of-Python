a = input("Please enter the number of a : ")
b = input("please enter the number of b : ")

print("choose the operation You want to preform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = input("please select the opration (1/2/3/4):")

if option == "1":
	result = float(a) + float(b)
	print("The result is : " , result)
elif option == "2":
	result = float(a) - float(b)
	print("The result is : " , result)
elif option == "3":
	result = float(a) * float(b)
	print("The result is : " , result)
elif option == "4":
	if float(b) == 0:
		print("Error: Division by zero is not allowed.")
	else:
		result = float(a) / float(b)
		print("The result is : " , result)