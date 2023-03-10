
num_of_three = input("Введить тризначне число: ", )
if len(num_of_three) > 3 or len(num_of_three) < 3:
    print("Error! Only 3 characters allowed!") 
else:
    num_of_three = int(num_of_three[::-1])
    print(num_of_three)