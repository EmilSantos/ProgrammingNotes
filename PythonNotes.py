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
If else elif == != > >= <=

age = 21
if age >= 16 :
    print(‘You are old enough to drive’)
else :
    print(‘You are not old enough to drive’)

if age >= 21 :
    print(‘You are not old enough to drive’)

if age >= 
