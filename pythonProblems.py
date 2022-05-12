import os 

#Problem 1.1
Script = """

DATE=$(date +%Y-%d-%b)    
   
for file in *.txt; do
    mv "$file" "${DATE} ${file}"
done

ls -l
"""
process = os.popen(Script).read()
print(process)

#Problem 1.2
process = os.popen("mkdir pythonPractice; ls -l").read()
print(process)

#Problem 2.1
tag= "I"
word = "Yay"

ansString= "<" + tag + ">" + word + "</" + tag + ">"
print(ansString)

#Problem 2.2
oldString= "Event ID:97,Event ID:2"
print(oldString)
newString = oldString.split(",")
print(newString)

#Problem 3.1
def make_tags(tag, word):
  ansString= "<" + tag + ">" + word + "</" + tag + ">"
  return ansString

print(make_tags("i","Yay"))

#Problem 3.2
def splitString(oldString):
   return oldString.split(",")

print(splitString("Event ID:97,Event ID:2"))

#Problem 4.1
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return 40 <= cigars
          
    return 40 <= cigars and cigars <= 60

#Problem 5.1
  
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

print(first_last6([1,2,6])) 

#Problem 6.1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

#Problem 7.1
for x in range(2, 30, 3): 
    print(x)

#Problem 8.1
class Vehicle:
  def __init__(self, max_speed, mileage):
      self.max_speed = max_speed
      self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

#Problem 9.1
class Vehicle:
  def __init__(self, max_speed, mileage):
      self.max_speed = max_speed
      self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#Problem 10.1
#Get-ChildItem -Recurse | Get-Member

#Problem 10.2
#Get-ChildItem -Recurse | Where-Object {$_.LastWriteItem -gt "04/12/2022"}
