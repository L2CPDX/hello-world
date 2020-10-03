# first Lesson

puts "Hello World" # puts is print for Ruby with formatting
puts "goodbye"
# will print 
# Hello World
# Goodbye

print "hello" #print outputs with little/ no formatting
print "world"
# will print
# helloworld

# if needed, formatting can be manually added

print "hello\n" 	# \n -> new line
print "\tworld\n" 	# \t tab

# So use puts, not print, unless for some reason you need to use print

p 			# p prints & also tells you wht was printed 
p "hello" 	# prints "hello"
p 'goodbye' # prints 'goodbye' <- note single quote
p "42" 		# prints "42" <- p recognizes this is a string
p 42 		# prints 42 <- p recognizes this is a number



# second lesson

puts "one"
puts "tomato"
#puts "tomato" # hashtags are comments in Ruby (as opposed to // in js)
puts "two"
puts "potato"

# third Lesson

puts "hello world"
puts "butts, butts, sexy sexy butts" # Highlight a line and press ctrl + / to comment it out. Works for multiple lines.
# puts "butts, butts, sexy sexy butts"

puts '-------' 		# makes a good divider for output 

# fourth Lesson

# Section Title - Numbers 

# numbers 1

# Order of operations MATTERS. # ()/*+-
puts 6 + 4 / 2 		# -> DIVIDES / first, then ADDS + remember, ()/*+= 
puts (6 + 4) - 2 	# -> ADDS + first, then DIVIDES /
puts 1 + 1 			# prints / display the sum of 1+1, which is 2
puts 5 / 2 			# prints 2, not 2.5. It drops the decimal place
puts 5 / 2.0 		# this will return 2.5
puts 5 % 2 			# this will return the remainder. The remainder here is 1
# Modulo has 3 steps:
# S1 - 5 / 2 = 2.5
# S2 -(the number in front of the decimal) * (the divisor) | so 2 * 2 = 4
# S3 (result of prev step) - (original dividend) | so 5 - 4 = 1

# numbers 2

puts 5 == 5 	# prints true, evaluating that 5 equals 5. 
#TYPE EQUALS SIGN TWICE.
puts 3 == 5 	# prints false
puts 5 != 5 	# prints false. != means 'is not equal to"
puts 3 != 5 	# prints true. 3 is not equal to 5
puts 100 > 2 	# true. 100 is greater than 2. 
puts 100 < 2 	# false 100 is not less than 2
puts 100 >= 2 	# true
puts 100 <= 100 # true

# Booleans

puts false || false   # false 
puts true && false    # false
puts 5 > 0 || false   # true
puts !true            # false
puts 4 == 3 || 4 > 3  # true
puts !true && 1 == 0  # false

# strings

"if it's inside quotes, it gets treated like a string"
puts "if it's inside quotes, it gets treated like a string"

# counting string characters
puts "hello".length # prints 5

# indexing / indices

puts "hello"[0] # H
puts "hello"[1] # e
puts "hello"[2] # l
# and so on

# concatenation
# strings can be concatenated, or strung together

puts "hello" + "there" + "world" # hellothereworld
puts "Hello" + " " + "World" 	 # Hello World


puts "if it's inside quotes, it gets treated like a string" +", " "even if it looks like another part of coding" # if it's inside quotes, it gets treated like a string, even if it looks like another part of coding

puts "6 % 1 > 7 + 3" + " is still a string" + " even though it looks like an expression" # 6 % 1 > 7 + 3 is still a string even though it looks like an expression
puts "it puts the lotion on its skin" + ", " + "so do you feel lucky, punk?" # it puts the lotion on its skin, so do you feel lucky, punk?


# variables 

# Let's make a variable named my_num
my_num
my_num = 42
puts my_num # 42

my_num + 8 			# 50
puts my_num 		# 42 <- line 117 wasn't stored, just run, so my_num is still 42
my_num = my_num + 8 # 50 <- this stores 50 as my_num going forward
my_num += 8 		# this means the same thing as line 119

num = 12 				# variable num = 12
is_even = num % 2 == 0 	# does 12 % 2 return 0?
puts is_even 			# true

firstname = "bloo"
lastname = "springsteen"
fullname = firstname + " " + lastname
puts fullname 			# bloo springsteen

# examples

sentence = "There is no spoon"
puts sentence + "?"   # There is no spoon?

puts sentence         # There is no spoon

sentence += "."
puts sentence         # There is no spoon. <- this used += so the period is saved to the string going forward

num = 6 / 2
puts num              # 3

puts sentence[num]    # "r"

# more examples

num = 40
num + 5
puts "---1:"
puts num                   # 40

num += 2
puts "---2:"
puts num                   # 42

isEven = num % 2 == 0
puts "---3:"
puts isEven                # true

isNegative = num < 0
puts "---4:"
puts isNegative            # false

puts "---5:"
puts isEven || isNegative  # true

puts "---6:"
puts isEven && isNegative  # false

puts "---7:"
puts isEven && !isNegative # true

# Methods

# Defining a method
def sayMessage
	puts "I like butts!"
	puts "sexy, sexy butts!"
end							# this won't print anything! It just tells Ruby what sayMessage is

# Call this Method to make it run
sayMessage

puts "before" 		# before
sayMessage			# I like butts! sexy, sexy butts!
puts "after"		# after

# prints as
# before
# I like butts!
# sexy, sexy butts!
# after

def say_helo(person)
	puts "Say hello," + " " + person + "."
end

say_hello("Dave") 	#  Say hello, Dave.

# LMAO time for math!

def calc_average (num1, num2)
	sum = num1 + num2 
	avg = sum / 2.0
	return avg 				# return lets you keep the data in the variable, as puts just prints it with formatting
end

puts calc_average(5, 10) 	# 7.5

result = calc_average(5,10)
puts result + 1 			# 8.5

# Hey, I wrote this!

def average_of_three(num1, num2, num3)
  avg = (num1 + num2 + num3) / 3.0     # (ADD + the 3 numbers), then DIVIDE / by 3.0
  return avg
end

puts average_of_three(3, 7, 8)   # 6.0
puts average_of_three(2, 5, 17)  # 8.0
puts average_of_three(2, 8, 1)   # 3.666666

# Fun with Methods

def goodbye(name)
  return "Say,"+ " " + "Bye" + " " + name + "."
end

puts goodbye("Dave")   		# Say, Bye Dave.
puts goodbye("Beyonce")  	# Say, Bye Beyonce.

# Conditionals

# if
# else
# elsif


num = 8

if num > 0 
	puts "positive"			# positive <- if num is greater than 0
elsif num < 0
	puts "negative"			# negative <- if num is less than 0
else 
	puts "It's a zero!"		# It's a zero <- if num is neither greater than nor less than 0
end


# Method: Check if a number is divisible by 5
def is_div_by_5(number)
  if number % 5 == 0		# Is this number divisible by 5?
      puts "wooooo"
    else 
      puts "naaaaahhhh"
    end    
end


puts is_div_by_5(10) # wooooo <- true
puts is_div_by_5(40) # wooooo <- true
puts is_div_by_5(42) # naaaaahhhh <- false
puts is_div_by_5(8)  # naaaaahhhh <- false

# Oh noes! They're giving us problems to solve with the explanation after!
#
#Write a method either_only(number) that takes in a number and returns true if the number is divisible by either 3 or 5, but not both. The method should return false otherwise:

def either_only(number)
	if (number % 3 == 0 && number % 5 != 0 || number % 3 != 0 && number % 5 == 0) 	# if number is divisible by 3 but not divisible by 5, or if number is not divisible by 3 but divisible by 5, return true
      return true
    else
      return false
    end
  end

puts either_only(9)  # true
puts either_only(20) # true
puts either_only(7)  # false
puts either_only(15) # false
puts either_only(30) # false

#
# Write a method larger_number(num1, num2) that takes in two numbers and returns the larger of the two numbers:

def larger_number(num1, num2)
  if num1 > num2				# if num1 is greater than num2
    return num1					# print and save that number
  else 							
    return num2					# If not, print and save the other number	
  end
end

puts larger_number(42, 28)   # 42
puts larger_number(99, 100)  # 100

#
# Write a method longer_string(str1, str2) that takes in two strings and returns the longer of the two strings. In the case of a tie, the method should return the first string:

def longer_string(str1, str2)
	if str1.length >= str2.length
      return str1
    else
      return str2
	end
end

puts longer_string("app", "academy") # academy
puts longer_string("summer", "fall") # summer
puts longer_string("hello", "world") # hello

#
# Write a method number_check(num) that takes in a number and returns a string. The method should return the string 'positive' if the num is positive, 'negative' if the num is negative, and 'zero' if the num is zero:


def number_check(num)
	if num > 0
     return "positive" 
    elsif num < 0
     return "negative"
    else
      return "zero"
    end      
end

puts number_check(5)    # positive
puts number_check(-2)   # negative
puts number_check(0)    # zero

#
# Write a method word_check(word) that takes in a word and returns a string. The method should return the string "long" if the word is longer than 6 characters, "short" if it is less than 6 characters, and "medium" if it is exactly 6 characters long:

def word_check(word)
  if word.length > 6
    return "long"
  elsif word.length < 6
    return "short"
  else
    return "medium"
  end
end

puts word_check("contraption") # long
puts word_check("fruit")       # short
puts word_check("puzzle")      # medium


# Loops

# while should evaluate to false eventually. Otherwise infinite loops can occur.

def printChars(str)			# create method printChars. Method printChars uses str.
	i = 0					# start count at 0 (index 0)

	while i < str.length	# if the cont is lower then the length of str
 		puts str[i]			# print string incrementally by character

 	i += 1 					# increment / iterate by 1
 end

 printChars("cats")			# call method printChars with string 'cats'

# prints as:
# c
# a
# t
# s

# Things to remember:

i = 0 						# define where you want counter to start

i += 1 						# this increments += by 1 

# the string hello returns 4 on the index, not 5. 0 is counted as the first character.

# Loop Challenge: Solve the following 

# Write a method count_e(word) that takes in a string word and returns the number of e's in the word

# Prep Material method:

def count_e(word)
  count = 0

  i = 0
  while i < word.length
    char = word[i]

    if char == "e"
      count += 1
    end

    i += 1
  end

  return count
end

puts count_e("movie") # => 1
puts count_e("excellent") # => 3
  

# My Method

def count_e(word)
	 
  i = 0							# start count at 0
  
  result = 0 					# start result at 0 
  								# (in this case, result counts incidences of e)
  
  while i < word.length			# while the count is less than the length of word 
   	if word[i] == "e" 			# if the index number of word matches string e,
    	result += 1				# increment result (ierate result conter by 1)
    end
     i += 1						# iterate index (by 1)
  end
  return result
end

puts count_e("movie") 		# 1
puts count_e("excellent") 	# 3
puts count_e("edifice") 	# 2

# this also works, but there's a reason you define a variable separately

# Write a method count_a(word) that takes in a string word and returns the number of a's in the word. The method should count both lowercase (a) and uppercase (A)

# My Method:

def count_a(word)

  i = 0							
  
  wCase = 0
  								
  while i < word.length			 
   	if word[i] == "A"			# this is clunkier and more lines
    	wCase += 1      		# of code than it needs to be
    elsif word[i] = "a"			# a better way is below
    	wCase += 1
    end
     i += 1						
  
 end
	return wCase
end

puts count_a("application")  # 2
puts count_a("bike")         # 0
puts count_a("Arthur")       # 1
puts count_a("Aardvark")     # 3


# Correct Method:

def count_a(word)

  i = 0							# start count at 0
  
  wCase = 0
  								
  while i < word.length			 
   	if word[i] == "A" || word[i] == "a"  # Use that OR || comparison!
      wCase += 1      
    end
     i += 1						
  
 end
	return wCase
end

puts count_a("application")  # 2
puts count_a("bike")         # 0
puts count_a("Arthur")       # 1
puts count_a("Aardvark")     # 3

# Write a method, count_vowels(word), that takes in a string word and returns the number of vowels in the word. Vowels are the letters a, e, i, o, u:

def count_vowels(word)
    i = 0
  	vowels = 0
  
  while i < word.length
     chr = word[i]
    
    if chr == "a" || chr == "e" || chr == "i" || chr == "o" || chr == "u"
      vowels += 1
    end
    
    i += 1 
  end
  return vowels

end

puts count_vowels("bootcamp")  # 3
puts count_vowels("apple")     # 2
puts count_vowels("pizza")     # 2

# Loop order matters.

# Write a method sum_nums(max) that takes in a number max and returns the sum of all numbers from 1 up to and including max:

def sum_nums(max)
  sum = 0

  i = 1
  while i <= max
    sum += i 				  # !! IMPORTANT -> += to i !!

    i += 1
  end

  return sum
end

puts sum_nums(4) 	# 10
puts sum_nums(5) 	# 15


# This is the same problem as line 510, expanded with output to show the loops

def sum_nums(max)
  sum = 0
  
  i = 1
  while i <= max
    sum += i
    puts "------"
	print sum 
    print "\ssum\s"
    i += 1
    puts "\n"
  	print i
    puts "\si"
  end

    puts "--~~--"
  return sum
end

puts sum_nums(4)  	# 10
puts sum_nums(5)  	# 15

# output
# ------
# 1 sum 
# 2 i
# ------
# 3 sum 
# 3 i
# ------
# 6 sum 
# 4 i
# ------
# 10 sum 
# 5 i
# --~~--
# 10
# ------
# 1 sum 
# 2 i
# ------
# 3 sum 
# 3 i
# ------
# 6 sum 
# 4 i
# ------
# 10 sum 
# 5 i
# ------
# 15 sum 
# 6 i
# --~~--
# 15

#
#
#
# Write a method factorial(num) that takes in a number num and returns the product of all numbers from 1 up to and including num:

def factorial(num)
  sum = 1
  
  i = 1

  while i <= num
    sum *= i 				 # sum = sum * i 
    
    i += 1
  end 
  
  return sum
end

puts factorial(3) # 6, because 1 * 2 * 3 = 6
puts factorial(5) # 120, because 1 * 2 * 3 * 4 * 5 = 120

#
# Write a method reverse(word) that takes in a string word and returns the word with its letters in reverse order:

def 


end

puts reverse("cat")          # tac
puts reverse("programming")  # gimmargorp
puts reverse("bootcamp")     # pmactoob

#
# 
