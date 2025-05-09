'''

ESYST -131 - Numbers and Increments (with Logic)
J HUNT (4/22/2025

==============================================================

The program will print a list of numbers and pythonically increment each elemtns by a number of user's choosing.
After wards the sum of the number will be printed

===============================================================

Variables:
aList[] #A List to build given numbers
intcrAmt #Holds the users input in int
total #Holds the sum of the value plus incrementation
newList #New list to display and hold the values

================================================================

Functions:

sum() to get the total
append() to add to the newlist
enumurate()
Imports:

none

============================================================

'''


#Declaration of a list to test with
aList = [5,17,22,32,44]

#Declare a new list to put stuff in
newList = []

#Store user's input
intcrAmt = int(input("How would you like to increase? "))

#A loop to go through my list and performs functions and display the data
for i, v in enumerate(aList):

    total = v + intcrAmt
    newList.append(total)
    print(f'The value at index {i} is {v} and incremented by {intcrAmt} equals: {total}')

print(f'The sum is: {sum(newList)}')


