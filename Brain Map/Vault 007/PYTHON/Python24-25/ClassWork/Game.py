def displayMenu():
    print(f"""
    {"="*20}
    1 : Move forward
    2: Move Left
    3: Move Right
    4: Action
    {"=" *20}
""")

def verifyInput(ui):
    print(ui,type(ui))
    if type(ui) == 'str':
        print("This is a string, lets make it a int")
        ui = int(ui)
        return ui

def uInput():
    userINput = input("Enter a option: ")
    userINput = verifyInput(userINput)
    print(f"You have selected: {userINput}")

    match userINput:
        case 1 |"1":
            print("You moved forward, hastily")
        case 2:
            print("You moved to the left")
        case 3:
            print("You moved to the right")
        case 4:
            print("ACTION!")
        case _:
            print("UNKNOWN ERROR")

def game():
    displayMenu()
    uInput()

game()