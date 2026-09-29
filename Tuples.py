t = (3, 3.14, "bruce Lee", True)
print(type(t)) #tuple
print(len(t))
print(type(t[1]))

fruits = ('appple', 'orange', 'pear', 'banana')
print(fruits[1:3]) #start from 1, and stop at 3
print(fruits[:3])
print(fruits[2:])
print(fruits[:])

t = (0,1,2,3,4,5)
print(t[-3:])
print(t[:-3])
# t[0] = 20; Error TypeError: 'tuple' object does not support item assignment
print(t[0])

s = ['apple', 'orange', 'pear']
print(fruits[-2]) #orange
s.pop()

fruit_by_code={'hgfhgf': 'apple', 20: 'orange'}
print(fruit_by_code[20])
print(fruit_by_code['hgfhgf'])