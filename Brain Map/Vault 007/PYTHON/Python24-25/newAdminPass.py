'''
#Our testing condition variables
correct_username = "admin"
correct_password = "pass123"

#Attempts Counter
MaxAttempts = int(3)
AttemptsCounter = int(0)

while AttemptsCounter < MaxAttempts:
    #Inital input from user and this will break upon correct input
    username, password = input("Enter Username and password: ").split()
    if username == correct_username and password == correct_password:
        print(f"Welcome user {correct_username}")
        break
    #Compare the usernames but also use attempt to keep track
    elif username != correct_username:
        AttemptsCounter += 1
        newAttempt = MaxAttempts - AttemptsCounter
        print(f"Incorrect username try again! Attempts left {newAttempt}")
    #Compare the passwords but also use attempt to keep track
    elif password != correct_password:
        AttemptsCounter += 1
        newAttempt = MaxAttempts - AttemptsCounter
        print(f"Incorrect password try again! Attempts left {newAttempt}")
    #Final message to say the access is denied
    if AttemptsCounter == MaxAttempts:
        print(f"Access Denied! You have reached {MaxAttempts} attempts!"
'''
#remove this for access

###################### VERSION 2 #######################
################In this version we dont treat password and username as two seperate things###################

correct_username = "admin"
correct_password = "pass123"

#Attempts Counter
MaxAttempts = int(3)
AttemptsCounter = int(0)

while AttemptsCounter < MaxAttempts:
    #Inital input from user and this will break upon correct input
    username, password = input("Enter Username and password: ").split()
    if username == correct_username and password == correct_password:
        print(f"Welcome user {correct_username}")
        break

    else:
        AttemptsCounter += 1
        newAttempt = MaxAttempts - AttemptsCounter
    if newAttempt > 0:
        print(f"Wrong credentials! You have {AttemptsCounter} attempts left!")
    else:
        print(f"Access Denied! Max Attempts used")
