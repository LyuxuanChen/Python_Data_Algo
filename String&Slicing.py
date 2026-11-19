# \t is a tab \n = linebreak
print('\t hello\nworld')

# Triple quotation keeps line breaks
text = """This
Keeps
Format"""
print(text)

# raw string:
# add print(r"string"), keeps the format, special chacter such as \n ignored
print(r"this\name")
print("this\name")


# string concatenation (addition)
description = 'immutable'
message = description+' added'
print(message)
print(description*3) #immutableimmutableimmutable
# subtraction not supported for strings
print(message*0) #multiply by negative also empty string
print(repr(message*0)) #this shows '' to indicate empty string

# Substring Tests:
print('a' in 'program')
print('at' in 'battle')

# Slicing:
# list[a:b], including index a up to excluding b:
string = '01234'
print(string[1:3]) # 12
print(string[0:5]) # 01234
print(string[:4])  # 0123
print(string[1:])  # 1234

# Negative Index: -1 is the last item
print(string[-2:]) # 34
print(string[-4:-1])# 123
# Reverse String:
print("Reverse String:")
print(string[::-1])
print(reversed(string))
# Adding steps:
alphabet = 'abcdefghijklmn'
print(alphabet[1:10:1], alphabet[1:10:2], sep=' | ') # bcdefghij | bdfhj
print('a','b','c', sep=" | ")
print(alphabet[::3]) #adgjm
#Negative Steps: Move Backwards
print(alphabet[10:2:-1]) # kjihgfed

# Slicing can move beyond string:
text = 'Python'
print(text[:100])
print(repr(text[:100])) #S tops at Python
print(repr(text[100:])) # Becomes empty ''
# print(text[20]) # Error: select must exist

# String Comparison:
print("Apple" == "Apple")
print("Apple" != "Apple")
print("A"<'a') # Lower case has higher ASCII Value
print('cat'>'car')
print('a'<'c')
print('HKU'<'HKUST') # HKU same prefix, less char thus smaller

#String Functions:
def is_palindrome(text):
    return text == text[::-1]
print ("Palindrome Text for aba: ", is_palindrome('aba'))
# ord gives Code Point / Vice Versa
print(ord('a'), ord('A'), ord('陈')) # 97 65
print(chr(65)) # A
for number in range (65, 91):
    print(chr(number), end=' ') # Prints in one line with space in between
print()
# Useful Functions
print("hELlO World".capitalize()) # Capitalize First, lower other
print("hello".upper())
print("HELlO".lower())

print("red green blue".split()) #split into a string
print("red green blue".split("bl")) #split remove "bl" preserve space

print("banana".find("na")) # Finds first Instance 2, false = -1

print("strawberry".count("r")) # Count repetitions

print("hello123".isalnum()) # alnum = numbers + 26 letter
print("hello123$".isalnum())
print("hello".isalpha()) # alpha checks if are a-z characters
print('alpha')
print("123".isdecimal()) # Check if it is 0-9 numbers

# Remove Leading and Ending Spaces: .strip()
print("    T E S T   ".strip())

print("hello world".replace("world", "python"))

# Checking Start & End:
file = "report.csv"
print(file.startswith('rep'))
print(file.endswith('.csv'))


# String Immutability:
# cannot reassign like list:
text = 'Example'
# text[0] = 'a' #Error
# del text[1] #Error
l = [1,2,3]
del l[1]
print(l)

# Joining List:
text='Test'
letters = list(text)
letters[1] = 'E'
changed = ''.join(letters)
print(letters)
print(changed)
print(text)

name = '   Im   Alex'
words = name.split()
clean1 = ''.join(words) # No space In between
clean2 = ' '.join(words) # Preserves Space
print(clean1)
print(clean2)

contents = ['a', 'b', 'c', 'd']
print(f"Lockers: {' '.join(contents)}")
print("Lockers: " + "  ".join(contents))

# F string:
student = {'name': 'Alex', 'age': 18}
print(f'Student: {student['name']} is {student['age']} years old')
name = 'alex'
print(f"|{name:<20}|")
print(f"|{name:^20}|")
print(f"|{name:>20}|")
print(f"|{name:0<20}|")
print(f"|{name:0>20}|")
for numbers in [5, 9, 10, 15, 1234]:
    print(f'{numbers:03}') # Paddling: 0: fill with 0, 3: at least 3 digits

pi = 3.14159265
print(f'Pi is {pi:.4f}') # rounds to .1416


# Sortin Function:
alp = ['a', 'd', 'b', 'c']
print(sorted(alp)) #Doesn't change original list
print (alp)
alp.sort() # Changes original list in place
print(alp)
