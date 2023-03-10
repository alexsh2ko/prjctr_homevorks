# Practice block 1:
'''
1. Create an outer function that will accept two parameters, a and b
2. Create an inner function inside an outer function that will calculate the addition of a and b
3. At last, an outer function will add 5 into addition and return it
'''

print((f"\nouter function\n").upper())
a = 0
b = 0
def outer(a: int, b: int):
    try:
        a = int(input("Введіть 'a': "))
    except ValueError:
        print((f"Ви ввели не число, повторіть введення").upper())
        a = int(input("Введіть 'a': "))
    try:
        b = int(input("Введіть 'b': "))
    except ValueError:
        print((f"Ви ввели не число, повторіть введення").upper())
        b = int(input("Введіть 'b': "))
    sum_ab = 0
    def addition(sum_ab):
        sum_ab = a + b
        return sum_ab
    sum_ab = addition(sum_ab) + 5
    return sum_ab
print(outer(a, b))

# Practice block 2

'''
1.  Write a program that asks user to enter an integer and convert it to int. 
    If the user enters something that is not an integer, program should catch an error and ask the user to enter an integer again. 
    if user inputs an integer, program should print this number and quit w/o any error.
'''
print((f"\noutput on display user input\n").upper())
try:
    us_inp = int(input("Введіть число: "))
except ValueError:
    print((f"Ви ввели не число, повторіть введення").upper())
    us_inp = int(input("Введіть число: "))
print(us_inp)

'''
2.  Write a program that asks the user to input a string and an integer n. 
    Then display the character at index n in the string. 
    You should handle an error properly and display proper error message.
'''
print((f"\noutput on display symbol user index input\n").upper())
try:
    n = int(input("Введіть індекс символа: "))
except ValueError:
    print((f"Ви ввели не число, повторіть введення").upper())
    n = int(input("Введіть число: "))

try:
    us_text = input("Введіть текст: ")
except IndexError:
    print("Помилка, ви ввели нодостатьню кількість символів")
    us_text = input("Введіть текст: ")
print(f'Ваш символ: {us_text[n - 1]}')

# Practice block 3
'''
1. Write a function that simulate a dice roll and returns the result from 1 to 6.
'''
print((f"\ndice roll\n").upper())
import random
def diceroll():
    roll = random.randint(1,6)
    return random.randint(1,6)
print(f'Одиночне кидання: {diceroll()}\n')
'''
2. Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value
'''
sum_roll_1 = 0
sum_roll_2 = 0
sum_roll_3 = 0
sum_roll_4 = 0
sum_roll_5 = 0 
sum_roll_6 = 0
for i in range(10000):
    result = diceroll()
    if result == 1:
        sum_roll_1 += 1
    elif result == 2:
        sum_roll_2 += 1
    elif result == 3:
        sum_roll_3 += 1
    elif result == 4:
        sum_roll_4 += 1
    elif result==5:
        sum_roll_5 += 1
    elif result==6:
        sum_roll_6 += 1
print((f'статистика на 10000 кидань:\n').upper())
print(f"Одиничка випала {sum_roll_1} разів\nДвійка випала {sum_roll_2} разів\nТрійка випала {sum_roll_3} разів\nЧетвірка випала {sum_roll_4} разів\nП'ятірка випала {sum_roll_5} разів\nШостка випала {sum_roll_6} разів\n")
print(sum_roll_1 + sum_roll_2 + sum_roll_3 + sum_roll_4 + sum_roll_5 + sum_roll_6)
print((f'статистика на 10000 кидань:\n').upper())
print(f"Одиничка випала {sum_roll_1} разів\nДвійка випала {sum_roll_2} разів\nТрійка випала {sum_roll_3} разів\nЧетвірка випала {sum_roll_4} разів\nП'ятірка випала {sum_roll_5} разів\nШостка випала {sum_roll_6} разів\n")
#print(sum_roll_1 + sum_roll_2 + sum_roll_3 + sum_roll_4 + sum_roll_5 + sum_roll_6)

'''
3. Simulate an election for two candidates. Program should take amount of regions and rating for 1st candidate in each region (in percentage). Program should run election in every region. In every region, program should ask 10 000 voters. Candidate count as a winner if he gains more than 50% of all votes. Program should print the result of t2. Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value
he election for each region and the winner

    Example:

    Enter number of regions: 2 

    Enter rating for 1st candidate in each region: 34, 56

    Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate

    Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate

    Result: 2nd candidate won with 10900 votes and 54.5% of all votes
'''
print((f'\nan election for two candidates:\n').upper())
iter = 1
sum_voce_fst = 0
sum_voce_scd = 0
final_rait_fst = 0
final_rait_scd = 0
try:
    n = int(input("Введіть килькість регіонів: "))
except ValueError:
    print("Неправильне введення!")
    n = int(input("Введіть килькість регіонів: "))
if n <= 0:
    print("Неправильне введення!")
    n = int(input("Введіть килькість регіонів: "))
def voice(rait_fst):
    rait_fst = rait_fst * 100
    rait_fst = round(rait_fst,0)
    rait_fst = int(rait_fst)
    return rait_fst
while iter <= n:
    try:
        rait_fst = float(input(f"Введіть рейтинг кандидата у {iter} регіоні [**. **]: "))
    except ValueError:
        print("Неправильне введення!")
        rait_fst = float(input(f"Введіть рейтинг кандидата у {iter} регіоні [**. **]: "))
    if rait_fst < 0:
        print("Неправильне введення! Ваше значення - негативне!")
        rait_fst = float(input(f"Введіть рейтинг кандидата у {iter} регіоні [**. **]: "))
    elif rait_fst >= 100:
        print("Неправильне введення! Ваше значення не може перевищувати 100!")
        rait_fst = float(input(f"Введіть рейтинг кандидата у {iter} регіоні [**. **]: "))
    voice(rait_fst)
    print(f"Регіон {iter}: {voice(rait_fst)} голосів за 1 кандидата, {10000 - voice(rait_fst)} голосів за 2 кандидата")
    iter += 1
    sum_voce_fst += voice(rait_fst)
    sum_voce_scd += (10000 - voice(rait_fst))
final_rait_fst = (sum_voce_fst / (sum_voce_fst + sum_voce_scd)) * 100
final_rait_fst = round(final_rait_fst,1)
final_rait_scd = (sum_voce_scd / (sum_voce_fst + sum_voce_scd)) * 100
final_rait_scd = round(final_rait_scd,1)
if final_rait_fst > final_rait_scd:
    print(f"\n1й кандидат переміг з {sum_voce_fst} голосів і це {final_rait_fst} від всіх голосів\n")
elif final_rait_fst > final_rait_scd:
    print(f"\nКількість голосів однакова, повинен відбутися другий тур голосування!\n")
else:
    print(f"\n2й кандидат переміг з {sum_voce_scd} голосів і це {final_rait_scd} від всіх голосів\n")

    # Practice block 4
'''
1. Create a tuple with your first name, last name, and age.
2. Print your last name using indexing.
3. Create three variables in one line that extracted from tuple that you created in step 1.
4. Print your name letter by letter from this tuple
5. Create a new tuple that contains all info from the first tuple but remove first letter from all strings
6. Create a tuple with two values. First one is (1, 2), second one is (3, 4).
7. Create a program that calculates the sum of all values in the tuple and print it to the console.    
'''
my_tuple = ('Alex', 'Vanzha', 36)
print(my_tuple[1])
fst_name, scd_name, age = my_tuple[0], my_tuple[1], my_tuple[2]
for i in range (len(fst_name)):
    print(fst_name[i])
fst_name = fst_name[1:]
scd_name = scd_name[1:]
new_tuple = fst_name, scd_name, age
print(new_tuple)
two_val_tuple = (1, 2) ,(3, 4)
sum_val_tup = two_val_tuple[0][0] + two_val_tuple[0][1] + two_val_tuple[1][0] + two_val_tuple[1][1]
print(sum_val_tup)