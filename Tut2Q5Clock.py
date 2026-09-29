# Challenge 5
#
# Rotating Lock
# Optional
# A lock has three digit wheels. One turn moves every digit forward by one: 8 becomes 9 and 9 becomes 0. Turning a wheel past 9 never carries into the next wheel.
#
# Input
# Read four integers, one per line: code (0–999), turns (0–9), target (0–999) and attempts_left (0–5). Treat code and target as three digits: for example, 7 represents 007.
#
# Output
# Calculate the code after the turns. Print the new code as an integer without leading zeros, then True or False on the next line. Always print the calculated code, even with zero attempts left; do not subtract an attempt for this exercise.
#
# Example
# Input	Expected output
# 789
# 4
# 123
# 1	123
# True
# 999
# 1
# 0
# 0	0
# False

def rotate(n, m):
    n += m
    n %= 10
    return n

code = 789
turns = 4
target =123
left = 1

hundred = code//100
ten = (code%100)//10
digit = code%10

hundred = rotate(hundred, turns)
ten = rotate(ten, turns)
digit = rotate(digit, turns)

if hundred >= 10:
    hundred = hundred%10
if ten >= 10:
    ten = ten%10
if digit >=10:
    digit = digit%10

res = hundred*100+ten*10+digit
print(res)

if res==target and left>0:
    print("True")
else:
    print("False")


