#Import the color packages, Fore is font color, back is the background and style is glow

from colorama import Fore, Back, Style

#Print out a welcome bot with rules!

print(Fore.RED + Back.BLACK + Style.BRIGHT +
"""                                                               Welcome to CONVERSIONTRON!
                                                  Here we take your format of chocie and turn them into either
                                                             decimal, hexadecimal or binary! """)




#Use a while True loop and break out when its time or explicitly said so

while True:

#Ask for format and put it in variable CHOICE
#we use \n lists your options
    print("Choose the format of your input number!" + Back.RESET)
    choice = int(input(Fore.MAGENTA + "1)Decimal\n" + Fore.GREEN + "2)Binary\n" + Fore.YELLOW + "3)Hexadecimal: " + Back.RESET + Fore.RESET))

#Use IF statements to see when to do

    if choice == 1:
        user_input = int(input("Please enter a " + Fore.MAGENTA + "decimal " + Fore.RESET+ "number: "))
        binaryConverted = bin(user_input)[2:]
        hexConverted = hex(user_input)[2:].upper()
        print(Fore.GREEN + f"Binary = {binaryConverted}" + Fore.RESET)
        print(Fore.YELLOW + f"Hexadecimal = {hexConverted}" + Fore.RESET)

#For Binary you need to validate 1 and 0. Use the if all() method
#Binary input is taken as string! then decimalConverted is uses a int()
    elif choice == 2:
        user_input = input("Please enter a " + Fore.GREEN + "Binary " + Fore.RESET + "number: ")
        if all(char in '01' for char in user_input): #validate binary
            decimalConverted = int(user_input,2) #int() to base 2
            hexConverted = hex(decimalConverted)[2:].upper() #[2:] is for skipping first 2
            print(Fore.MAGENTA + f"Decimal = {decimalConverted}" + Fore.RESET)
            print(Fore.YELLOW + f"Hexadecimal = {hexConverted}" + Fore.RESET)
        else:
            print(Fore.RED + "invalid! Binary can only be 1's and 0's")

    elif choice == 3:
        user_input = input("Please enter a " + Fore.YELLOW + "Hexadecimal " + Fore.RESET + "number: ")
        try: #Use the try and if it doesnt work throw an exception and that exception is hex gone bad! 
            decimalConverted = int(user_input,16)
            binaryConverted = bin(decimalConverted)[2:]
            print(Fore.MAGENTA + f"Decimal = {decimalConverted}" + Fore.RESET)
            print(Fore.GREEN + f"Binary = {binaryConverted}" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Invalid HEX! try again!")
    else:
        print("You need to select 1 through 3")

    again = input("Would you like to contunue yes or no? ").lower()
    if again == "no":
        break



print(Back.BLACK+ Style.BRIGHT + Fore.WHITE + "Goodbye from CONVERSIONTRON!!!")



