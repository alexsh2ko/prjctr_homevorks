'''
1. Figure out the result of the following expressions:

    a) (1 <= 1) and (1 != 1) #reslt was False

    b) not (1 != 2) #reslt was False

    c) ("good" != "bad") or False  #reslt was True

    d) ("good" != "Good") and not (1 == 1)  #reslt was False
'''
'''
2. Make all of them True by adding parentheses:

    a) False == not (True)

    b) (True and False) == (True and False)

    c) not (True and "A" == "B")
'''

'''
3. Get a positive number from user input. Find all factors of this number.
 Example:
    - If the number is 6, the factors are: 1, 2, 3, 6
    - If the number is 10, the factors are: 1, 2, 5, 10
'''
print((f'\nGet a positive number from user input. Find all factors of this number:  \n').upper()) #вивід назви блоку програми
num = int(input("Enter your number: ", )) #цілочисельне введення від користувача
if num < 0:
    print("Your number is negative!") #перевірка на предмет негативного введення
elif num > 0: #якщо значення позитивне
    i = 1 
    print(f"- If the number is {num}, the factors are", end=": ")   #заміна переносу строки на символ ":"
    while i < num:
        if num % i == 0:    #перевірка цілочисельного ділення без залишку
            print(i, end=", ")  #вивід послідовності факторів без переносу на наступний рядок, з комою в кінці
        i+=1 
    print(num)  #вивід в туж строку числа, бо воно само на себе ділитсья без залишку   
else:
    print("Your number is 'Zero'")  #вочевидь якщо число не позитивне і не негативне, то це нуль
    '''
4. Write a Python program to check a triangle is equilateral, isosceles or scalene. Get all three sides from user input.

    Note :
    1. An equilateral triangle is a triangle in which all three sides are equal.
    2. A scalene triangle is a triangle that has three unequal sides.
    3. An isosceles triangle is a triangle with (at least) two equal sides.
'''
print((f'\nCheck a triangle is equilateral, isosceles or scalene\n').upper())   #назва наступного блоку програми
a = int(input("Enter first side of triangle: "))    #Ввід першої сторони трикутникка
b = int(input("Enter second side of triangle: "))   #Ввід другої сторони трикутникка
c = int(input("Enter third side of triangle: ",))   #Ввід треттьої сторони трикутникка
if a <= 0 or b <= 0 or c <= 0:  #перевірка на предмет негативного введення
    print("***INVALID NUMBER!***")
elif (a ** 2 + b ** 2 == c ** 2) or (c ** 2 + b ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):     #перевірка на прямокутність трикутника, використовуючи теорему Піфагора
    print("Your triangle is scalene, but it has one right angle")
elif a == b and b == c:     #перевірка на рівносторонність трикутника
    print("Your triangle is equilateral")
elif (a == b and b != c) or (b == c and c!=a) or (c == a and a != b): #перевірка на рівнобедренність трикутника
    print("Your triangle is isosceles")
else:
    print("Your triangle is scalene")   #Якщо жодна з умов не виконана, вочевидь трикутник скалярний
'''
5. Write a Python program to get next day of a given date. Get day, month and year from the user input.
Expected Output:
'''
print((f'\nNext day after user input: \n').upper())     #назва наступного блоку програми
year = int(input("Input a year: "))     #Введення користувачем року
if (year % 400 == 0):      #перевірка на те, чи є він високосним, згідно з помилкою яку враховує грегоріанський календар
    leap_year = True    
elif (year % 100 == 0):     #кожен рік який ділится без залишку на 4 є високосним
    leap_year = False       #не є високосний рік, якщо він без залишку ділиться на 100
elif (year % 4 == 0):       #про те рік є високосний, якщо він без залишку ділиться водночас на 100 і на 400
    leap_year = True
else:
    leap_year = False
month = int(input("Input a month [1-12]: ")) #Введення користувачем місяця із вказівкою діапазону значеннь
if month <= 0 or month > 12:    #перевірка на предмет негативного введення, та допустимого діапазону значень
    print("Wrong input!")
elif month in (1, 3, 5, 7, 8, 10, 12):  #місяці в яких 31 день
    month_length = 31
    day = int(input("Input a day [1-31]: "))    #Введення користувачем дня із вказівкою діапазону значеннь
    if day <= 0 or day > 31:    #перевірка на предмет негативного введення, та допустимого діапазону значень
        print("Wrong input!")
elif month == 2:    #лютий - самий цікавий місяць
    if leap_year:   #перевірка, якщо рік високосний, лютий містить 29 днів
        month_length = 29
        day = int(input("Input a day [1-29]: "))    #Введення користувачем дня із вказівкою діапазону значеннь
        if day <= 0 or day > 29:    #перевірка на предмет негативного введення, та допустимого діапазону значень
            print("Wrong input!")
    else:
        month_length = 28   #В інших випадках в лютому 28 днів
        day = int(input("Input a day [1-28]: "))    #Введення користувачем дня із вказівкою діапазону значеннь
        if day <= 0 or day > 28:    #перевірка на предмет негативного введення, та допустимого діапазону значень
            print("Wrong input!")
else:   #В інших випадках в залишку місяців 30 днів
    month_length = 30
    day = int(input("Input a day [1-30]: "))    #Введення користувачем дня із вказівкою діапазону значеннь
    if day <= 0 or day > 30:    #перевірка на предмет негативного введення, та допустимого діапазону значень
            print("Wrong input!")
if day < month_length:  #якщо день не останній в місяці до дати додаеться один день
    day += 1
else:
    day = 1 #якщо день останній в місяці, то він приймає значення 1
    if month == 12: #якщо місяць останній в році, то він приймає значення 1 і до року додається 1 
        month = 1
        year += 1
    else:
        month += 1  #В інших випадках да значення місяця додається 1
print(f"\nThe next date is [yyyy-mm-dd] {year}-{month}-{day}.") #Вивід дати наступного дня у форматі рік-місяц-день
'''
6. Write a program that takes number as its input and doubles that number few times in a loop. Number of iterations and initial number should be taken from user input. You should display each result on a separate line. Here is some sample output:

    Input:
    initial number: 2
    number of iterations: 5

    Output:
    4
    8
    16
    32
    64

'''
print((f'\nLoop of double user input: \n').upper())     #назва наступного блоку програми
init_num = int(input("Enter initial number: ", ))       #введення користувачем якогось числа
iter = int(input("Enter number of iterations: ", ))     #введення кількості ітерацій
print('Output: ')
for i in range(iter):   #ітерація значеннь з послідуючим множенням на 2
    init_num *= 2
    print(init_num) # Послідовний вивід
'''
7. Write a program that asks the user to enter a number, and then keeps asking for numbers until the user enters the number 0. 
Once the user enters 0, the program should print the sum of all the numbers entered by the user.
'''
print((f'\nSum number of user input, until user enter "0": \n').upper())    #назва наступного блоку програми
n = 0   #змінна в яку послідовно буде додаватись числа, які буде вводити користувач
while True: #цикл буде виконуватись до того, як користувач введе 0
    some_num = int(input("Enter a number: "))   #введення користувачем якогось числа
    if some_num == 0:     #якщо користувач введе 0, цикл припинется з виведенням суми чисел, які користувач вводи до нуля
        print(f'Sum of your number = {n}')
        break;
    n = n + some_num
    