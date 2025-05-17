#Assignment: VehicleClass1
#Author: Arslan Khan
#File name: VehicleClass1
#Contrib Auth: NONE
#Version: v1. (2025_05_16) (YYYY_MM_DD)
#==========================================================#
#Project Description:
#==========================================================#
'''
This project will call on the vehile construtor and create two vehicle objects with attributes
'''
#==========================================================#
# ::Variables::
#v1 to create lamborghini
#v2 to create a ferrari

# ::Logic::
#create a class called Vehicle, have a constructor, have a startUp method to start the car and shutDown method to shut down the car

class Vehicle:

    #Use a dunder method to create the object using self and attribute

    def __init__(self,year,make,model,color):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.engineStatus = False

    #make a start up method that takes in self as a argument

    def startUp(self):
        if self.engineStatus == False:
            self.engineStatus = True
            print("VROOOOOOOOOOOOM VROOoooOOOooM")
        else:
            print("Engine is already on!")

    #make a shutDown method to shut off the car only if engine is on

    def shutDown(self):
        if self.engineStatus == True:
            self.engineStatus = False
            print("puuurrrrttttt......")
        else:
            print("Engine is already off!")


#bring objects to life but giving it attributes!

v1 = Vehicle(1974,"Lamborghini","Countach","Yellow")
v2 = Vehicle(1962,"Ferrai","250 GTO","Red")

v1.startUp()
v1.startUp()
v1.shutDown()
v1.shutDown()
v1.startUp()
v1.shutDown()