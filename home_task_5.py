#Practice section 1:

'''
1. Write a program that caluculate Fibonacci series. 
The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. 
Number of iterations should be taken from user input.
'''
print((f'\nFibonacci series\n').upper()) #Послідовність Фібоначчі починається з двох одиниць
num1 = 1
num2 = 1
 
n = int(input("Послідовність Фібоначі з кількістю ітерацій: ")) #Введення користувачем кількості ітерацій цілим числом
if n <= 0:
    print("Введдіть число більше нуля!")
else:
    print(num1, num2, end=' ') #Початок послідовності з двох одиниць
 
for i in range(2, n): #Кожен крок ітерації сумма попередніх чисел
    num1 = num2
    num2 = num1 + num2
    print(num2, end=' ') #Виведення результату ітерації в строку

#Practice section 2:

#1. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
print((f"\n\nNumber divisible by 3 fro 0 to 100\n").upper()) #Назва наступного блоку
for i in range(0,100): 
    if i % 3 == 0:  #умова при якій число без залишку ділеться на 3
        print(i, end=' ') #Виведення результату ітерації в строку

'''
2. Get a number from user input and iterate from 0 to that number. 
    
    1. Print 'foo' if the number is divisible by 3. 
    2. Print 'bar' if the number is divisible by 5. 
    3. Print 'foobar' if the number is divisible by both 3 and 5.
'''
print(f"\n\nFOOBAR\n")  #Назва наступного блоку
us_num = int(input(f"Введіть число: \n")) #Ввод користувачем числа типу integer
for j in range(0,us_num + 1):
    print(j, end = ' ') #Виведення результату ітерації в строку
def foobar(us_num) -> int:  #назва функції з очікуваним введенням числа типу integer
    if us_num < 0:
        print("Введдіть число більше нуля, або нуль!")
    elif us_num % 3 == 0 and us_num % 5 == 0: #Перевірка кратності 3 та 5 одночасно, на першому місті
        print(f"\nfoobar")
    elif us_num % 3 == 0:   #Перевірка кратності 3, якщо ця умова була перевірена раніше, то перше умова не перевірялась би
        print(f'\nfoo')
    elif us_num % 5 == 0:   #Перевірка кратності 5, якщо ця умова була перевірена раніше, то перше умова не перевірялась би
        print(f'\nbar')
    else:
        print(f'\nNone')    #Якщо жодна з умов не виконана
    return " "
print(foobar(us_num))

#Practice block 3:
'''
1. Write a function called square() with one argument of int type and returns the value of that number raised to the second power.
'''
print((f'square function\n').upper())   #Назва наступного блоку
some_num = int(input('Введіть якесь число: '))  #Ввод користувачем числа типу integer
def square(some_num) -> int:    #назва функції з очікуваним введенням числа типу integer
    some_num = some_num ** 2    #ведення числа у квадрат
    return some_num     #Функція повертає значеня змінної some_num
print(f"Ваше число в квадраті дорівнює: {square(some_num)}") #Вивід результату виконання функції

'''
2. Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit. 
It should take a number as an argument from user input and return a number to the console.
'''
print((f'\nFrome celsius to fahrenheit\n').upper()) #Назва наступного блоку
deg_in_cels = int(input('Введіть температуру в градусах Цельсія: '))   #Ввод користувачем температури в градусах Цельсія
deg_in_fahr = 0
def cels_to_fahr(deg_in_cels) -> int:   #назва функції з очікуваним введенням числа типу integer
    deg_in_fahr = (deg_in_cels * 9 / 5) + 32    #формула переходу від градусів Целсія до Фаренгейта
    return deg_in_fahr  #Функція повертає значеня змінної deg_in_fahr
print(f'Ваша температура в градусах Фаренгейт: {cels_to_fahr(deg_in_cels)}')

'''
3. Write a function that implement case swapping. It should return the same result as swapcase() method. 
Your function should accept one str argument and convert all lower case values to upper case and vice versa.
'''
print((f'\nSwaping case\n').upper())    #Назва наступного блоку
some_text = input(f"Input your text: \n")   #Введення користувачем текста
def like_swap(some_text) -> str:    #назва функції з очікуваним введенням типу string
    mod_text = ''   #назва пустої зміної до якої буде записан видозмінений текст
    for x in some_text: #Ітерація строки, яку ввів користувач
        if x.isupper(): #Перевірка умови, якщо символ має верхній регістр
            mod_text += x.lower()   #Якщо True, то символ змінюється в нижній регістр, та додається до нашої змінної
        else:
            mod_text += x.upper()   #Якщо False, то символ змінюється в верхній регістр, та додається до нашої змінної
    return mod_text     #Функція повертає значеня змінної mod_text
print(like_swap(some_text)) #Вивід результату виконання функції