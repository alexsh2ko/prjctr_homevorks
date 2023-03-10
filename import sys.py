# Task 1. Even or odd. Прийняти від користувача число, вивезти чи even/odd
num = int(input('Введіть якесь число: ', ))
if num % 2 == 0:
    print("even")
else:
    print('odd')
# Task 2. When provided with a number between 0-9, return it in words. Input :: 1 Output :: "One".
numer = input('Введіть число від 0 до 9: ', ).rstrip()
match numer:
    case '0':
        print('Zero')
    case '1':
        print('One')
    case '2':
        print('Two')
    case '3':
        print('Three')
    case '4':
        print('Four')
    case '5':
        print('Five')
    case '6':
        print('Fix')
    case '7':
        print('Seven')
    case '8':
        print('Eight')
    case '9':
        print("Nine")                
    

# Task 3. Прийняти від користувача два числа і отримати дію над цими числами. Реалізувати +,-, /, *, //, ** 
fst = int(input('ВВедіть перше число: ', ))
scd = int(input('ВВедіть друге число: ', ))
des = input("Введыть дію(+,-,/,*,**): ")
'''
Explain:
   user_input = 6
   user_second_input = 10
   des = '+'
Result:
    print(user_input + user_second_input = 16(result))    
'''
match des:
    case '+':
        print(fst + scd)
    case '-':
        print(fst - scd)
    case '/':
        print(fst / scd if scd != 0)
    case '*':
        print(fst * scd)
    case '**':
        print(fst ** scd)
    case '//':
        print(fst // scd)
# Task 4. Прийняти від користувача name, surname. Вивезти ініціали. 
name = input("Введіть ім'я: ", )
surname = input("Введіть прізвище: ", )
init = f"{name}[0]. {surname}[0]"
print(f"'name: '{Name}, 'Surname: '{surname}, 'Init: '{init}")