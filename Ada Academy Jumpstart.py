# Ada Academy JumpStart Material

# x += 3 assigns the value of x + 3 to the variable x
# x += y + 3 assigns the value of x + (y + 3) to the variable x
# x -= 2 assigns the value of x – 2 to the variable x
# x -= y – 5 assigns the value of x – (y – 5) to the variable x
# x /= 3 assigns the value of x / 3 to the variable x
# x //= 3 assigns the value of x // 3 to the variable x
# x *= y assigns the value of x * y to the variable x
# x %= y assigns the value of x % y to the variable x

# let's define two variables
x = 2
y = 5

# operations using these variables
x += 3                # x = 5 , y = 5

x += y + 3            # x = 10 , y = 5

x -= 2                # x = 0 , y = 5

x -= y - 5            # x = 2 , y = 5

x /= 3                # x = 0.6666666666666666 , y = 5

x //= 3               # x = 0 , y = 5

x *= y                # x = 10 , y = 5

x %= y                # 

print("x =", x)
print("y =", y)

# -----------------------

# store the name of a state in the variable state_name
state_name = "washington"

# use string interpolation and the method capitalize to output the state_name in a different string
print(f"{state_name.capitalize()} is a nice place to live!")
# Washington is a nice place to live!

# store a value in the variables value_1 and value_2
value_1 = "2"
value_2 = "hello"

# use string interpolation and the method capitalize to output whether or not the values are digits.
print(f"True or False? The value {value_1} is a digit: {value_1.isdigit()}")
print(f'True or False? The value {value_2.capitalize()} is a digit: {value_2.isdigit()}')
# True or False? The value 2 is a digit: True
# True or False? The value Hello is a digit: False

# ----------------------------

# Using compound assignment statements and string interpolation, complete the following problem in the code block below
# Assign values to three variables x1, x2, and x3
# Print three number equations that show the result of adding 20 to each of the variables
# For instance, if x1 = 25, the ouput of your code should be 25 + 20 = 45

# assign values to 3 variables
x1 = 2
x2 = 40
x3 = 800

# print the equations
print( x1, "+", "20", "=", x1 + 20 ) 
print( x2, "+", "20", "=", x2 + 20)
print( x3, "+", "20", "=", x3 + 20)
# 2 + 20 = 22
# 40 + 20 = 60
# 800 + 20 = 820

# ----------------------------

# String Concatenation and Duplication
# When combining strings, you can use the + and * operators
word_1 = "home"
word_2 = "work"

print(f"You can combine the words {word_1} and {word_2} \
to make the word {word_1+word_2}.")
# You can combine the words home and work to make the word homework.

print(f"These days, all I seem to do is {3*(word_1+word_2+' ')}.")
# These days, all I seem to do is homework homework homework .

# ------------------------------

a = 3
b = 4
c = a*a + b***b
print(c)

# 265

# Double multiply (**) is the same as exponential power (^)

# ----------------------------

# Practice problems: 

# problem 1.1
x = 5
# what value does x now hold?
 
# 5
 
 
# problem 1.2
z = "Hello"
# what value does z now hold?
 
# Hello
 
 
# problem 1.3
a = 5
b = 3.2
c = a + b
# what values does c now hold?
 
# 8.2
 
 
# problem 1.4
var1 = "lawl"
var2 = "brb"
# what value does var2 now hold?
 
# brb
 
 
# problem 1.5
e = 6 + 3
# what values does e now hold?
 
# 9
 
 
# problem 1.6
f = 3.5
f = f + 2
# what value does f now hold?
 
# on the first iteration, 5.5
# on the second (if this was looped), 7.5
# third, 9.5 etc.
 
 
# problem 1.7
poodle = 4
pitbull = 3
# what value does boxer now hold?
 
# boxer is not defined as a variable
 
 
# problem 1.8
h = 5
h = h + h
# what values does h now hold?
 
# 10
 
 
# problem 1.9
j = 1
k = 2
m = 3
n = j + k + m
# what value does n now hold?
 
# 6
 
 
# problem 1.10
l = "moo"
q = "quack"
l  = q
# what value does l now hold?
 
# quack
 
 
# problem 1.11
r = "moo"
s = "quack"
t = "woof"
r = t
# what value does r now hold?
 
# woof
 
 
# problem 1.12
u = 5
u = u * 2
u = u * 2
u = u * 2
# what value does u now hold?
 
# 40
 
 
# problem 1.13
v = "b"
z = "a"
# what value does v now hold?
 
# b
 
 
# problem 1.14
aa = 3234
bb = 2398
cc = 0
dd = (aa + bb) / cc
# what value does dd now hold?
 
# none / NA / error
# (one does not simply divide by zero)
 
 
# problem 1.15
yy = 7
zz = yy % 2
# what value does zz now hold?
 
# 1
 
 
# problem 1.16
ee = 12
ff = ee % 4
# what value does ff now hold?
 
# 0
 
 
# problem 1.17
zz = 17
hh = zz % 3
# what value does hh now hold?
 
# 2

# --------------------------------

# Moar Problems

d = 10
e = 5.0
f = 2
g = 11.0
h = 3
i = 1.5

# Operation                         Result                          Data Type

d + e                                 15.0                           Float 

f + h                                 5                              Integer
 
g + h                                 14.0                           Float 
 
d - f                                 8                              Integer
 
g - e                                 6.0                            Float 
 
(h + 1) - f                           2                              Integer 
 
(d - f) + e                           13.0                           Float 
 
d * f                                 20                             Integer 		

g * i		                          16.5                           Float

f * g		                          22.0                           Float

d / f		                          5                              Integer 

d / e		                          2.0                            Float

e / f		                          2.5                            Float       

(g * f) / f		                      11.0                           Float 

(d / f) * e		                      25.0                           Float 

21 / 5		                          4.2                            Float  

14 / 5		                          2.8                            Float 

10 % 3		                          1                              Integer  

20 % 2		                          0                              Integer

4 % 5		                          4                              Integer

8 % 1		                          0                              Integer


# ---------------------

# problem 3.1
my_string = "I love Seattle"
my_string[7]
 
# S
 
 
# problem 3.2
my_string = "I love Seattle"
my_string[2:4]
 
# lo
 
 
# problem 3.3
my_string = "Ada"
my_string += " Lovelace"
 
# Ada Lovelace
 
 
# problem 3.4
my_string = "Ada"
my_string += " codes" + " it!"
 
# Ada codes it
 
 
# problem 3.5
my_string = "Ada"
(my_string + " likes to code")[4:9]
 
# likes
 
 
# problem 3.6
my_string = "Hello world"
"Goodbye " + my_string[6:11] + "!"
 
# Goodbye world!
 
 
# problem 3.7
my_string = "Hello world!"
my_string[0:5] + ", goodbye!"
 
# Hello, goodbye!
 
 
# problem 3.8
my_string = "Hello world!"
my_string[:1] + "i" + "!"
 
# Hi!
 
 
# problem 3.9
my_string = "I love Python"
my_string[7:13] + my_string[2:6] + my_string[0]
 
# PythonloveI
 
 
# problem 3.10
my_string = "I love Python"
"P" + my_string[8:13] + " rocks!"
 
# Python rocks!
 
 
# problem 3.11
my_string = "I love Python"
my_string[2:6] + my_string[7:13] + my_string[2:6]
 
# lovePythonlove


# --------------------


# Relational Operators

# Operator             Definition                   
   ==                    Equals                     
   !=                 Does not Equal                
   <                    Less Than       
   >                  Greater Than 
   <=               Less Than or Equal To
   >=               Greater than or Equal to 

# < is not the opposite of > !!!! 

# < is the opposite of >=
   
# see below, lifted from a java tutorial site

# If x > y evaluates to false, then x <= y evaluates to true. If x > y evaluates to true, then x <= y evaluates to false.
# The negation of greater-than is less-than-or-equal. Some people who've never heard of that find it hard to believe. They think "No way. The opposite of greater than is less than!"

# But that's not true. Let's see why. Suppose I say "I am older than you". This means "My age is greater than your age". When would that be false? That is, when would I be lying? Let's assume that ages are integer values.

# Certainly, I'm lying if I'm really younger than you. But what if you and I are the same age? In that case, I'm still lying, because if we're the same age, then I can't be older than you. So I'm lying if my age is less than or equal to your age.

# and that's why > is the opposite of <= instead of < !!!! Just < does not account for equality / equivalency


# -------------------------


# = is an assignment operator

x = 73

baby = "never"

# here, the variables x and baby have been assigned to the integer value 73 and the string "never" respectively. 


# -------------------------


# Operators can be chained together

 0 < x <= 100 or 10 > x > 1
 
 
 # ------------------------
 
 
 # Hunting Bugs
 
 # EOL stands for End of Line. This means that Python hit and error at the end of the line when evaluating the string. That is why there's a carat ^ at the end of the line
 
 
 # ---------------------
 
 
 # Non-Boolean falsey and truthy
 
 # The two possible values of the boolean data type (bool) are True and False
 # 
 # A non-boolean value that evaluates to False, is called "falsey", also sometimes "falsy". Below is a list of all "falsy" values in Python. 
 
 # Sequences and Collections:
 # Empty lists []
 # Empty tuples ()
 # Empty dictionaries {}
 # Empty sets set()
 # Empty strings ""
 # Empty ranges range(0)
 
 # Numbers:
 # Zero of any numeric type.
 # Integer: 0
 # Float: 0.0
 # Complex: 0j
 
 # Constants:
 # None
 # False
 
 # A non-boolean value that evaluates to True, is called "truthy"
 
 # Everything not included in the "falsy" list above is "truthy" in Python.
 
 # Examples:
 
 bool(0)
 # False
 
 bool("")
 # False
 
 bool("hello")
 # True
 
 bool(1)
 # True
 
 bool(None)
 # False
 
 bool([])
 # False
 
 bool([1,2,3])
 # True
 

# --------------------


# Conditionals

# Conditional statements allow programs to take different paths based on different inputs 
# Conditional statements are typically represented well by flow charts, which can be a planning and organizational aid

# To create conditional statements use if, elif, and else to control the flow of a program.

# Indenting conditionals is mandatory. In Python, indentation is required or a program will not execute.

# elif comes from the contraction of else if. Many people just say el-if.

# A colon : must be used after the boolean expression and else. 

# A single if statement with no else or elsif has to evaluate to true as a boolean to execute

if <boolean expression>:
    # note the colon 
    # conditional body
    # this code only executes if the <boolean expression> evaluates as true
    # the conditional body is indented one more than the if statement


if <boolean expression>:
    # conditional body
    # the conditional body is indented one more than the if, elif, and else statements
elif <boolean expression>:
    # conditional body
    # the conditional body is indented one more than the if, elif, and else statements
else:
    # else body
    # the else body is indented one more than the if, elif, and else statements


if <boolean expression>:
    # conditional body
    # the conditional body is indented one more than the if, elif, and else statements
else:
    # else body
    # the else body is indented one more than the if, elif, and else statements



