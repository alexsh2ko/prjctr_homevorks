#1. Write a program that get two int variables and swap their values. Do it in 3 different ways.

var_fst = int(input("Введіть перше число: "))
var_scd = int(input("Введіть друге число: "))

#First way
var_fst, var_scd = var_scd, var_fst

#Second way
some_var = var_fst
var_fst = var_scd
var_scd = some_var

#Third way
var_fst = var_fst + var_scd
var_scd = var_fst - var_scd
var_fst = var_fst - var_scd


'''
1. Написати програму яка отримує від користувача два числа. Вивести ці два числа в консоль.
2. В попередній програмі дописати команди для знаходження мінімальної цифри і вивести мінімум в консоль
3. Додати підтримку float значень
4. Додати функціонал по знаходженню степені числа. Перше число є базою, друге - ступенем. 
Вивести результат в консоль у форматі "а в b степені це c"
5. Написати скрипт, який отримує 2 числа від користувача через команду input. 
Провести операцію складення і множення цих значень і вивести результат найбільшої операції.
'''

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
print(f'Перше число: {num1}\nДруге число: {num2}')
#Провести та вивезти над ними всі базові арифметичні операції в print
print(f'Множення: {num1 * num2}')
print(f'Ділення: {num1 / num2}')
print(f'Ділення без залишку: {num1 // num2}')
print(f'Залишок від ділення: {num1 % num2}')
print(f'Зведення в ступінь: {num1 ** num2}')

if num1 < num2:
    print(f"Мінімальне число {num1}")
elif num1 > num2:
    print(f"Мінімальне число {num2}")
else:
    print("Ви ввели однакові числа")
num1 = float(num1)
num2 = float(num2)

print(f"{num1} в ступені {num2} це {num1 ** num2}")

num3 = int(input("Введіть число: "))
num4 = int(input("Введіть число: "))
if num3 + num4 > num3 * num4:
    print(f"Найбільший результат це сума: {num3 + num4}")
elif num3 * num4 > num3 + num4:
    print(f"Найбільший результат це множення: {num3 * num4}")

#0. How to understand that number is an integer?
#Integer це тип даних який приймає тільки цілі числа. Наприклад: 1, -9, 0, 12, 32, -1024 тощо.
'''
1. Write a program that get 2 numbers from the use. Print to the console their difference.

    Enter first number: 5

    Enter second number: 3

    Difference is 2 
'''
num5 = int(input("Enter first number: "))
num6 = int(input("Enter second number: "))
print(f"Difference is {num5 - num6}")
'''
2. Write a program that get 3 digit number from the user and reverse it.


    Enter a number: 123

    Reversed number is 321
'''
us_num = int(input('Enter a number: '))
rev_num = 0
a = (us_num % 10) * 100
us_num = us_num // 10
b = (us_num % 10) * 10
us_num = us_num // 10
rev_num = a + b + us_num
print('Reversed number is', rev_num)
'''
Explain why 0.1 + 0.2 != 0.3
Це пов'язано з переводом цих чисел у двійкову систему та округленням Python значення суми у двійковій системі
'''
#Прийняти від користувача ім'я, призвіще, вік, вивезти одним print:
name = input("Enter your name: ", )
age = input("How old are you: ", )
print("Your name is",name,"and you",age,"years old", sep = " ", end = "\n") 
#   b)By formating a string using the format function
greeting = "Your name is {} and you {} years old"
print(greeting.format(name, age))
#   c)By formating a string with f-string
print(f'Your name is {name} and you {age} years old')
#Але це завдання з наступного урока