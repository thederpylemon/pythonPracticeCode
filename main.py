
if 5 > 2: 
 print("Five is greater than two!")

# this is a comment

"""
You can use a multi-line string 
to indicate a multi-line comment
"""

# setting a variable
x = 112
y = "COS"

# to cast a variable to a specific type
x = str(112) # "112"
y = float(3) # 3.0 

#to get the type
x = 112
print(type(x))

#to slice a string
x = "112 COS"
print(x[:3])
print(x[4:])

#boolean check
x= 200
if bool(x):
  print('boolean does exist!')

#function check 
def boolCheck(args):
  if bool(args):
    print('variable does exist!')

x = 200
boolCheck(x)

#string condtional
txt = "The 112COS is best the squadron!"

if ("worst" in txt):
  print("112COS is the worst")
elif ("best" in txt):
  print("112COS is the best")
else:
  print("112COS is average")

#lists
list = ["mip1", "mip2","mip3","mip3000"]
#using list index
firstMip = list[0]
print("This is the first mip : " + firstMip)

#adding and removing new list item
newMip = "mip4"
list.append(newMip)
list.pop(3)
print("New list: ", list) 

#tuples
tuple = ("mip1","mip2","mip3", "mip4")
lastMip = tuple[-1]

#unpacking a tuple
(firstMip, secondMip, *otherMips) = tuple
print("First mip: ", firstMip)
print("Second mip: ", secondMip)
print("Other mips: ", otherMips)

#sets
set1 = {"mip1", "mip2", "mip3"}
print("Old set1", set1)

set2 = {"mip4", "mip5", "mip6"}
print("Old set2", set2)

#combine sets
set1.update(set2)
print("New set1", set1)

#Dictionaries
airmanDict = {
  "lastName": "Snuffy",
  "rank": "E2",
  "D.O.E": 2020,
  "AFSC": ["1D7X1A","1B4X1"]
}
#accessing item
rank = airmanDict["rank"]
print("Rank: ", rank) 

#adding key:value
airmanDict["T.I.G(months)"] = 6

#removing key:value
airmanDict.pop("D.O.E")
print(airmanDict)

#looping through a string
string = "BADABAA"
for x in string:
    print("Letter: ", x)

#looping through a list
list = ["mip1", "mip2","mip3","mip3000"]
for x in list:
  print(x)
  if x == "mip3":
    break

#while loop
list = ["mip1", "mip2","mip3","mip3000"]
i = 0

while i < len(list):
  print(list[i])
  i += 1
else:
  print("List iteration is done")


#constructor
class Plane:
    def __init__(self):
      print("this is a Plane")
       
ba = Plane()


#class
class Plane:
    def __init__(self, name):
        self.wings = 2
        self.name = name

        # fly
        self.nameDeclare()
        self.drive()
        self.flaps()
        self.wheels()

    def nameDeclare(self):
            print("Boarding", self.name)
    
    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

ba = Plane("Air Force One")

#properties
class Plane:
    def __init__(self, name):
        self.wings = 2
        self.name = name

ba = Plane("Air Force One")
print(ba.name,"has", ba.wings, "wings")

#methods
class Plane:
    def __init__(self, name):
        self.wings = 2
        self.name = name

        # fly
        self.nameDeclare()
        self.drive()
        self.flaps()
        self.wheels()

    def nameDeclare(self):
            print("Boarding", self.name)
    
    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

ba = Plane("Air Force One")
ba.nameDeclare()

#Inheritence
class Plane:
    def __init__(self, name):
        self.wings = 2
        self.name = name

        # fly
        self.nameDeclare()
        self.drive()
        self.flaps()
        self.wheels()

    def nameDeclare(self):
            print("Boarding", self.name)
    
    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

#ba = Plane("Air Force One")
#new Class
class tinyPlane(Plane):
  def __init__(self, name):
    super().__init__(name)
    self.planeSize = "tiny"
    
  def sizeDeclare(self):
    print("Welcome to the smallest plane, at size:", self.planeSize)
    
bb= tinyPlane("C-17")
bb.sizeDeclare()

