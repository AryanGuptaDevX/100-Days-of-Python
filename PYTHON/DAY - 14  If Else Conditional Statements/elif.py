applePrice = 10
budget = int(input("Enter your budget: "))
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
elif (budget - applePrice > 20):
    print("Alexa, add 500 gms Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")