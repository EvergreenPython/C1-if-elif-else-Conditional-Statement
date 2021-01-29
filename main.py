'''
01/28/2021

Review:

if/else conditional statement

if (Condition):
  Body Statement1
else:
  Body Statement2

Condition:
  - Boolean Expression; True / False

  a = 5
  b = int(input())
  a == b
  1 >= 0


if/elif/else conditional statement
- used for decision-making operations with conditions

Formula:
if (Condition):
  Body Statement

elif (Condition):
  Body Statement

elif (Condition):
  Body Statement

.
.
.

else:
  Body Statement


Condition:
An expression that evaluates to produce a result which is a Boolean value (Boolean expression)

In a conditional statement,
1x if header
infinite x elif header(s) 
1x (optional) else clause

1x (Maximum) output/result
   (Minimum) none

# Ex

a = 1

if (a == 0):
  print ("hi")

elif (a != 2):
  print ("welcome")

elif (a > 4):
  print ("Congratz")

elif (a < 10):
  print ("hello")

else:
  print ("bye")

'''


a = 5000 # Hard coding (not recommend)
num = int(input("Enter a number: "))

if (num > 0):
  print ("I see that your number is positive")
elif (num == 0):
  print ("You entered 0")
else:
  print ("It's negative")

# Ask the user for their age
# If they are 17 and older, they can watch all movies
# If they are 13 and older but younger than 17, they only watch PG-13/PG/G movies
# If they are younger than 13, tell them they can only watch PG/G movies

age = int(input("Enter your age: "))

if (age > 16):
  print ("You can watch all movies")

elif (age > 12):
  print ("You can watch PG-13/PG/G movies")

else:
  print ("You can only watch PG/G movies")


is_Hungry = True
is_Sleepy = False

if (is_Hungry):
  print ("You should go eat")
if (is_Sleepy == True):
  print ("You should go sleep")
if (is_Sleepy == False):
  print ("Wow you're well-rested")
