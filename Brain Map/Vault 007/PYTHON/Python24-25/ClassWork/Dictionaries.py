



#We Create a dictionary within a dictionary to make it look well structured

phoneBook = {
        "Smith, Kevin" : {

            "LName" : "Smith",
            "FName" : "Kevin",
            "Phone" : "555-1230",
            "Address" : "123 Main Street",
            "City" : "Bev Hills",
            "Zip" : "90210"
        }
}

#Now I want to add onto this dictionary

phoneBook.update({
        "Fernando, Jane" : {

            "LName" : "Fernando",
            "FName" : "Jane",
            "Phone" : "555-666",
            "Address" : "321 Main Street",
            "City" : "Encino",
            "Zip" : "91234"
        }
     }
)

print()