**OBJECT ORIENTED PROGRAMMING** 
+ We build classes and give it attributes
+ Objects have methods
+ object variables are only for that specific object

# Basic Class Object set up

**INPUT**

```
class Vehicle:
	def __init__(self)
		print("Im alive")
	
	def birthCertificate():
	print("This is my birth certificate")	
	
v1 = Vehicle()
v2 = Vehicle()
v3 = Vehicle()
```

**OUTPUT**

```
Im alive
Im alive
Im alive
```

+ **__init__** (a dunder method) gets ran every time an object comes to life in my code.
	+ EVERY TIME you create an object everything in the **__init__** method 
	+ We created 3 object that ran the **__init__** 3 times to EACH object
	+ THE REASON why **birthCertificate** didnt run is because i did not give it a SELF argument, meaning the object it SELF
	+ **def birthCertificate(==self==): is the correct way to run it
	+ WE CREATE INDIVIDUALITY WITH INIT

# LETS ADD PARAMETERS TO OBJECTS

```
class Vehicle:
	def __init__(self,year,make,model,color):
		self.year = year
		self.make = make
		self.modle = model
		self.color = color
	def carShow(self):
		print(f'Hi! I am a {self.make} {self.model})
		
v1 = Vehicle(1996,"Ford","Mustang","Blue")
print(v1.color)
v1.carShow()

```
	

+ Here we are using self to make the objects awareness of its attributes.
	+ when we make v1 we send in arguments such as 1996
		+ but atm the object does not know what to attach it to
		+ now we attach it by **self.year = year**
		+ this brings the object attributes to life!
+ To print the color we use **v1.color**
```
blue
Hi I am a Ford Mustang
```

# BLACK BOX OBJECTS (PROTECT THEM)

+ I can change my objects data or anyone can to mess it up I can take the year of the car and assign it a new value and save it.
+ We use a getter to get the data from objects.

```
v1.year = 199999999996
print(v1.year)
```

+ This is miss use of data! We need to secure it through setters! 