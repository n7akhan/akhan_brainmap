'''
Task-Wk04_01-Invitation
ESYST-131
#####################
Scenario:
You’re having a last minute party and you want to make sure some of your closest friends across time and realities are there to partake. 
You know with some quick Python skills you can take this list of people and turn it into a quick announcement. 
Let’s do it!
#####################

Do NOT alter the names, order, spelling or capitalization. Merely copy and past the list into your IDE

friends:
johnny bravo
marilyn Monroe
Nikola Tesla
cleopatra
Steve rogers
helen of Troy
bruce bAnner
Natasha Romanoff
'''

##################################
#1.	Create a variable ‘friends’ with the value of a list of the above friends.
##################################
#Enter code below:
friends = [

    "johnny bravo",
    "marilyn Monroe",
    "Nikola Tesla",
    "cleopatra",
    "Steve rogers",
    "helen of Troy",
    "bruce bAnner",
    "Natasha Romanoff"
]


##################################
#2.	Print your friends list now
##################################
print("."*20)
#Enter code below:
print(friends)



##################################
#3.	Let’s personalize out invite. First names only
##################################
print("."*20)
#Enter code below:
for names in friends:
    print(names.split(" ")[0])



##################################
#4.	Capitalize our names
##################################
print("."*20)
#Enter code below:
for names in friends:
    print(names.split(" ")[0].title())


##################################
#5. Send out the Invites
##################################
print("."*20)
#Enter code below:
for names in friends:
    print(f'I am stoked to see you at my party this weekend, {names.split(" ")[0].title()}')