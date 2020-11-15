import random
import sys
import os

print(“Hello World”)
#Comment
'''
Multiline Comment
'''

#----------VARIABLES AND DATATYPES----------#
name=“Derek”
Print(name)

#Datatypes: Numbers, Strings, List, Tuples, Dictionary/Map
#Arithmetic: +, - , *, /, %, **, //(floor division)

#----------LISTS (MUTABLE)----------#
grocery_list = [‘Juice’, ’Tomatoes’, ‘Potatoes’, ‘Bananas’]
print(‘First Item’, grocery_list[0])
grocery_list[0] = “Green Juice”       	#First Item Juice
print(‘First Item’, grocery_list[0])    #First Item Green Juice
print(grocery_list[1:3])    			#[’Tomatoes’, ‘Potatoes’]

other_events = [‘Wash Car’, ‘Pick Up Kids’, ‘Cash Check’]
To_do_list = [other_events, grocery_list]
print(to_do_list)    #[[‘Wash’, ‘ Pick Up Kids’, ‘Cash Check’], [‘Green Juice’, ’Tomatoes’, ‘ Potatoes’, ‘Bananas’]]

print((to_do_list[1][1]))     #Tomatoes

grocery_list.append(‘Onions’)
grocery_list.insert(1, “Pickle”)
grocery_list.remove(“Pickle”)
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]

to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#----------TUPLES (IMMUTABLE)----------#

pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple)    #converting list and tuple
new_list = tuple(new_tuple)

len(tuple)    min(tuple)    max(tuple)

#----------DICTIONARY/HASHMAP----------#

super_villains = {‘Fiddler’ : ‘Isaac Bowin’,
                            ‘Captain Cold : ‘Leonard Snart’,
                            ‘Weather Wizard’ : ‘Mark Mardon’,
                            ‘Mirror Master’ : ’Sam Scudder’,
                            ‘Pied Piper’ : ’Thomas Peterson’}

print(super_villains[‘Captain Cold’])    	# Leonard Snart
del super_villains[‘Fiddler’]
super_villains[‘Pied Piper’] = ‘Hartley Rathaway’
print(len(super_villains))     				# 4
print(super_villains.get(“Pied Piper”))   	#Hartley Rathaway
print(super_villains.keys())    			#([‘Captain Cold’, ‘Weather Wizard’, ….])
print(super_villains.values())    			#([‘Leonard Snart’, ‘Mark Mardon’, ….])

#----------CONDITIONS----------#
#If else elif == != > >= <=

age = 21
if age >= 16 :
	print("You are old enough to drive")
else :
	print("You are not old enough to drive")

if age >= 21 :
    print("You are old enough to drive a tractor trailer")
elif age >= 16 :
	print("You are old enough to drive a car")
else : 
	print("You are not old enough to drive")


#and or not
if ((age >= 1) and (age <= 18)):
	print("You get a birthday")
elif (age == 21) or (age >= 65):
	print("You get a birthday")
elif not(age == 30):
	print("You don't get a birthday")
else:
	print("You get a birthday party yeah")


#----------LOOPING----------#

for x in range(0, 10):    #end="" means no new lines
	print(x, ' ', end="")    #0 1 2 3 4 5 6 7 8 9

grocery_list = [‘Juice’, ’Tomatoes’, ‘Potatoes’, ‘Bananas’]
for y in grocery_list:
	print(y)		#Juice Tomatoes Potatoes Bananas (on new lines)

for x in [2,4,6,8,10]:
	print(x)		#2 4 6 8 10 (on new lines)

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
	for y in range(0,3):
		print(num_list[x][y])

#WHILE
random_num = random.randrange(0,100)
while(random_num != 15):
	print(random_num)
	random_num = random.randrange(0,100)

i = 0
while(i <= 20):
	if(i%2 == 0)
		print(i)
	elif(i == 9):
		break
	else:
		i += 1
		continue
	i += 1

#----------FUNCTION----------#
def addNumber(fNum, lNum):
	sumNum = fNum + lNum
	return sumNum

print(addNumber(1,4))    #5

#----------USER-INPUT----------#
print('What is your name')
name = sys.stdin.readline()
print('Hello', name)

#----------SUB-STRING----------#
long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4])     #I'll
print(long_string[-5:])     #Floor
print(long_string[:-5])     #I'll catch you if you fall - The
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f" %
		('X', 'favorite', 1, .14))
print(long_string.capitalize())     #capitalize first letter of string
print(long_string.find("Floor"))    #33 (33rd character of the string of 'Floor')
print(long_string.isalpha())		#returns true if all characters are letters
print(long_string.isalnum())		#returns true if all characters are numbers
print(len(long_string)				#returns length
print(long_string.replace("Floor", "Ground"))	#replaces "Floor" with "Ground"
print(long_string.strip())			#removes white space
quote_list = long_string.split(" ")
print(quote_list)					#["I'll", 'catch', 'you', ...]

#----------FILE-IO----------#
#write
test_file = open("test.txt", "wb")
print(test_file.mode)				#wb
print(test_file.name)				#test.txt
test_file.write(bytes("Write me to the file\n", "UTF-8"))
test_file.close()

#read
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)					#Write me to the file

#delete
os.remove("test.txt")

#----------OBJECT-ORIENTED----------#

class Animal:
	__name = ""
	__height = 0
	__weight = 0
	__sound = 0

	#initialize function
	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound

	#setters and getters
	def set_name(self, mame):
		self.__name = name

	def set_height(self, height):
		self.__height = height

	def set_weight(self, weight):
		self.__weight = weight

	def set_sound(self, sound):
		self.__sound = sound

	def get_name(self):
		return self.__name

	def get_height(self):
		return self.__height

	def get_weight(self):
		return self.__weight

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
																	 self.__height,
																	 self.__weight,
																	 self.__sound)

cat = Animal("Whiskers", 33, 10, "Meow")
print(cat.toString())

#Inheritance
class Dog(Animal):
	__owner = ""
	def __init__(self, name, height, weight, sound, owner):
		self.__owner = owner
		super(Dog, self).__init__(name, height, weight, sound)

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dog")

	def toString(self):    #Overriding: use function thats already in super class

spot = Dog("Spot", 53, 27, "Ruff", "Derek")

#Polymorphism
class AnimalTest:
	def get_type(self, animal):
		animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)     #Animal
test_animals.get_type(spot)	   #Dog























