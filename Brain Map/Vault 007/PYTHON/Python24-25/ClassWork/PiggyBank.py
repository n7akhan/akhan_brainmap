
#CODE BY ARLSAN KHAN

#Create a program that takes in money and displays how much people added and what the total is

#Take in inputs from the user
intPen = int(input("Enter how many penny: "))
intNic = int(input("Enter how many nickel: "))
intDime = int(input("Enter how many dimes: "))
intQuart = int(input("Enter how many quarters: "))
intDollar = int(input("Enter how many dollars: "))

#Caluculate the total and times their respective amounts

total = ((intPen * 0.01) + (intNic * 0.05) + (intDime * 0.10) + (intQuart * 0.25) + (intDollar * 1.00))

#Round the total by using round() function

total = round(total,2)

#Print out the results with printf statements

print(f""" You entered these values:
Pennies : {intPen}
Nickels : {intNic}
Dimes : {intDime}
Quarters : {intQuart}
Dollars : {intDollar}
======================================================
Total : {total}
""")