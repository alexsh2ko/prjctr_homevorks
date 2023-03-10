#PRACTICE CHAPTER 1

#1.Gues result without executing it:
'''
a) 1 >= 1 is true
b) 1 != 1 is false
c) 1 != 2 is true
'''

#2. Make all theme true:
'''
a) 3 _ 4     !=, <, <=
b) 10 _ 5    !=, <, <=
c) 42 _ '42' !=   
'''
#PRACTICE CHAPTER 2

#1.Print the text in which there will be a quote with double quote:
print('Hello "Python"!')

#2.Print the text in which there will be an apostrafe:
print('Hello my friend\'s')
print("Hello my friend's")

#3.Print one line that well be displayed on several line:
print("Hello \n my friend\'s'")

#4.Print text that doesn`t fit in one line but will be displayed in one line:
print('''Hello my 
friend'''.replace("\n",""))

#PRACTICE CHAPTER 3

#1.Create a variable with data type string. Count the lenth of this line.
var = "Hello Python,"
print(len(var))
#2.Create another variable with data type string. Output the result of the cocatenation of this two variables.
var_1 = "the most popular programming language"
print(var + var_1)
#3.Print the two previos variables, but with a space between them.
print(var + " " + var_1)
#4.Get a string frome user input. Check Is the string a palindrome 
pal = input("Is the word a palindrome? Your word: ", )
print(pal.lower() == pal.lower()[::-1])

#PRACTICE CHAPTER 4

#1.The program receive user`s name and age frome input. Then you need to display the name and age in one line in several ways:
#   a)By listing all the parametrs in the print function:
name = input("Enter your name: ", )
age = input("How old are you: ", )
print("Your name is",name,"and you",age,"years old", sep = " ", end = "\n") 
#   b)By formating a string using the format function
greeting = "Your name is {} and you {} years old"
print(greeting.format(name, age))
#   c)By formating a string with f-string
print(f'Your name is {name} and you {age} years old')

#PRACTICE CHAPTER 5

#Format string with a proper function
#1.All the letters must be writen in lowercase.
string_1 = "Animals "
print(string_1.lower())

#2.All the letter must be capitalized
string_2 = " Badger"
print(string_2.capitalize())

#3.Remove all spaces
string_3 = " HoneyPot "
#a)frome the begining of the line
print(string_3.lstrip())
#b)frome the end of the line
print(string_3.rstrip())
#c)frome both sides of the line
print(string_3.strip())
 #4.Check the value of the startwith ('Be')  function for each line.:
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEAr"
print(string_1.startswith('Be'))
print(string_2.startswith('Be'))
print(string_3.startswith('Be'))
print(string_4.startswith('Be'))

#Convert rows with methods frome prev exercise to have positive result foreach row
formated_string_1 = string_1.title()
formated_string_2 = string_2.title()
formated_string_3 = string_3.title()
formated_string_4 = string_4.title()
print(formated_string_1.startswith('Be'))
print(formated_string_2.startswith('Be'))
print(formated_string_3.startswith('Be'))
print(formated_string_4.startswith('Be'))

#5.Find and replace all letters 's' with the letters 'x' in the following line
new_string = "Somebody said something to Samantha."
new_string = new_string.replace('s','x')
new_string = new_string.replace('S','X')
print(new_string)

#6.Leave only numbers in the folowing line using onli string method
strange_string = '1,2,3,4,5,!,_6--'
strange_string_1 = "".join(c for c in strange_string if c.isdigit())
print(strange_string_1)

#7.Find a secret massage in the folowing text:
val = 'X!xeXnxiXlX XtxeXrxcXeXs Xax XsXXtXlX'
val = val.lower()
val = val.replace('x','')
print(val[::-1])