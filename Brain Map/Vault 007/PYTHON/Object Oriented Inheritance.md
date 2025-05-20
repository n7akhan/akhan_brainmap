+ An object class that inherits from other classes and so on

```
class Creature:  
  
    def __init__(self,legs, wings):  
  
        #attributes of the class creature  
        self.legs = legs  
        self.wings = wings  
        print(f'I am a {type(self)}') #Announcess what creature it is  
  
    def makeSound(self):  
        print("SCREEEEEEECH!")  
  
  
#This creates an inheritance new class, we extend the creautres stuff with the ()  
#We pass Creature class to Golem, parent to a child, specfially the init self constructor  
  
class Golem(Creature):  
    def __init__(self,legs, wings):  
        #The super () is the inheritance from the creature class!  
        super().__init__(legs,wings)  
    def makeSound(self): #Here we have a golem specific method!  
        print("Rawwr!")  
  
c1 = Creature(4,True)  
c2 = Creature(2,True)  
g1 = Golem(2,False)  
g1.makeSound()  
c1.makeSound()
```

**SUPER().__init__**

+ Here I am taking the self constructor from the creature class and the class as a whole into my Golem class! 
+ Golem prints "I am class Golem" because of the super() init!

**MAKE SOUND FUNCTION**
+ We have a makeSound() in both parent class (Creature) and child class (Golem) in this case Golem is asked to make a sound it will say "Idk how to make a sound let me ask my parents" **Golem will go to the parents class and ask creature parents make a sound "screech"**
+ Now if Golem already has a makeSound() method now it looks to itself first and makes sound which is "Rawwr!"
+ The hierarchy is the super().__init() this says "go one up"
