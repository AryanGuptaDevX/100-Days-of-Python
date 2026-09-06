# import time
# print(time.strftime("%H:%M:%S"))

# timestamp = int(time.strftime("%H"))
# print(timestamp)

# if timestamp < 12:
#     print("Good Morning")
# elif timestamp < 16:

#     print("Good Afternoon")
# elif timestamp < 20:
#     print("Good Evening")
# else:
#     print("Good Night")

time = int(input("Enter the time in 24 hour format: "))

if time < 12:
    print("Good Morning")
elif time < 16:
    print("Good Afternoon")
elif time < 20:
    print("Good Evening")
else:
    print("Good Night")