# learning to code in python
#

# using Serenade, which is a voice to code program

myint = 7   # this is how to set an integer
print(myint)

#
# floating integers must be declared separately
# there are two ways to add floating integers:

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# but I think it will be easier to just use myfloat = 7.0

#
# this is a string

mystring = "hello"

#
# let's write a program

print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+ 1) + ' in a year.')

# Hello world!
# What is your name?
#  - > Input was: Gail
# It is good to meet you, Gail
# The length of your name is:
# 4
# What is your age?
#  - > Input was: 77
# You will be 78 in a year.

# ~-~-~-~--~--~--~--~--~-~-~-~
#
# Python Data types, Data Structures, and Objects

# Data Types:

# Integers
#
  int
#
# Integers are whole numbers
  1  7  300  5  25

# Floating Point
#
float
#
# numbers with a decimal point
  2.3  9.9  40.6

# Strings
#
str
#
# ordered sequence of characters
  'hello' 'cat' "ain't" "1300" "7+7"


# Data Structures:

# Lists
#
list
#
# ordered sequence of objects
  [10,"world",203.3]

# Dictionaries
#
dict
#
# unordered key:value pairs
  {"mykey":"value","name":"Frank"}

# Tuples
#
tup
#
# ordered immmutable sequence of objects
  (10,"hello",199.9)

# Sets
#
set
#
# unordered collection of unique objects
{"a","b"}

# booleans
#
bool
#
# logical value indicating true or false
True    False



#
# variables
#

# names cannot start with a number
# there can be no spaces in the name, use _ underscore instead
# cant use any of these symbols :"",<>/?|\()!@#$%^&*~-+

# its best practices that names are lowercase

# in python, dynamic typing is possible.

# here the variable we're assigning is an integer
my_dogs=2

# here the variable is now two strings in a list
my_dogs = ["fido","spot"]

# in python,its okay do this
# In other languages, you'll get errors

# the type function can help with this
type()


# variable time!


my_income=100

tax_rate=0.1

my_taxes = my_income * tax_rate

# 10.0


# strings
#
# strings can have either single '' quotes or double "" quotes
"hello" "12345" 'hello' 'this is in single quotes'

# strings can be indexed
"hello"[4]
# o |-> h 0  e 1  l 2  l 3  0 4

# strings can also be reverse indexed
"hello"[-1]
# o |-> h 0  e -4  l -3  l -2  0 -1

# strings can be sliced into subsections
# this has its own syntax, [start:stop:step]


# defining string length
len("this is a string")

# using variables
mystring = "abcdefghijk"

mystring[6]
# g

# using slicing syntax
# include everything from index number to end
mystring[6:]
# ghijk

# include everything up to index number
mystring[:3]
# abc

# increase step size
mystring[::2]
# acegik

mystring[::3]
# adgj


# let's put this into practice
mystring[3:6]
# def

mystring[1:3]
# abc

mystring[3::2]
#dfhj

#
# String Interpolation
#
# (also known as:)
# String formatting for printing

# Two methods
 .format()   f-strings  # string literals

# 
# .format() method:
# 'string {} and also if yu feel like it {}'.format('string1','string2')

print('Stringy stringy strings! {}'.format('REDACTED'))
# Stringy stringy strings! REDACTED

print('Stringy stringy strings! {2} {1} {0}'.format('REDACTED','######',"CENSORED"))
# Stringy stringy strings! CENSORED ###### REDACTED

# this has possibilities. 
print('Stringy stringy strings! {0} {0} {0}'.format('REDACTED','######',"CENSORED"))
# Stringy stringy strings! REDACTED REDACTED REDACTED

# assigning variables is a thing. 
print('Stringy stringy strings! {pnd} {c} {r}'.format(r='REDACTED', pnd='######', c="CENSORED"))
# Stringy stringy strings! ###### CENSORED REDACTED

# Float formatting with .format() method:
# "{value:width.precision f}"
result = 355 / 113       
result                   # 3.1415929203539825 |-> closer approximation to pi than 22/7. Thank u, google

print("The result was {r}".format(r=result))
# The result was 3.1415929203539825

# changing the decimal place!
print("The result was {r:1.5f}".format(r=result))
# The result was 3.14159

print("The result was {r:1.5f}".format(r=result))
# The result was 3


#
# f-strings (string literal) method:
name = "Jose"
age = 40

print(f'{name} is {age} years old') 
# Jose is 40 years old



#
# Lists
# Ordered sequences that can hold many object types
# [1,2,3,4,5]
# Lists can be indexed, sliced, or nested, Methods can be called off of them. 

my_list = [1,2,3]

# or maybe
my_list = ['A string',23,100.232,'o']

len(my_list)
# 4

my_list = ['one','two','three',4,5]

my_list[0]
# 'one' 

my_list[1:]
# ['two', 'three', 4, 5]

# Let's make a new list
new_list = ["6", "7", "eight"]

# list cancatenation is possible.
# here, the two lists are cancatenated and the new outcome assigned to a third variable, another_list  
another_list = my_list + new_list

# call the new list
another_list
# ['one', 'two', 'three', 4, 5, '6', '7', 'eight']

# replacement of list items is possible
new_list[0] = "ONE ALLCAPS"
# ['ONE ALLCAPS', 'two', 'three', 4, 5, '6', '7', 'eight'] 

# add an item to a list 
new_list.append("nine")
new_list
# ['ONE ALLCAPS', 'two', 'three', 4, 5, '6', '7', 'eight', "nine"] 

# remove items from the list with the 'pop method'
# Without a number specified, .pop() will remove the last item on the list
new_list.pop()
# "nine"
new_list
# ['ONE ALLCAPS', 'two', 'three', 4, 5, '6', '7', 'eight'] 

# you can save the object you popped off the list, too
popped_item = new_list.pop()                # this pops off 'eight'
popped_item
# 'eight'

new_list
# ['ONE ALLCAPS', 'two', 'three', 4, 5, '6', '7']

# remove an index position from a list
new_list.pop(0)
# 'ONE ALLCAPS'
new_list
# ['two', 'three', 4, 5, '6', '7']

# let's explore some other methods for lists 
# first, let's redefine the list 
new_list = ['a','e','x','b','c']        # redefining overwrites the content of the variable 
num_list = [4,1,8,3]                    # making a second list named num_list

new_list.sort()                         # this won't outwardly do anything, but when you call new_list
new_list                                # the list sorts in alphabetical order
# ['a', 'b', 'c', 'e', 'x']

new_list.reverse()                      # this (if you haven't noticed) is a method to reverse strings 
new_list
# ['x', 'e', 'c', 'b', 'a']            

# !! - Remember! None of these actually save the new variable, list, etc! You have to assign your changes to a new variable! - !!




















