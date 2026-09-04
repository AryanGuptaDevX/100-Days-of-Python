name ="aryan"
friend = "rohan"
anotherfriend = 'sachin'

print(name + " is my name and " + friend + " is my friend and " + anotherfriend + " is also my friend")

apple = '''he wants ,' \
    hey i am good
hi harry
' "to eat apple"'''
print(apple)

test = """In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence o
r array of textual data.
 Strings are used when working
   with Unicode characters. """
print(test)

print(name[0]) # prints the first character of the string
print(name[1]) # prints the second character of the string
print(name[2]) # prints the third character of the string
print(name[3]) # prints the fourth character of the string
print(name[4]) # prints the fifth character of the string
# print(name[5]) #this will give an error because the string has only 5 characters and the index starts from 0 to 4

for character in test:
    print(character) # prints each character of the string in a new line