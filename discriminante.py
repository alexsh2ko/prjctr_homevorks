import math


a = float(input("ВВедіть a: "))
b = float(input("ВВедіть b: "))
c = float(input("ВВедіть c: "))
d = 0.0
choose = int(input("Оберіть спосіб вирішення (1 - дискримінант, 2 - Вієта): "))
if choose != 1 or choose != 2:
    

def discriminant(a, b, c, choose):
    x_one = 0.0
    x_two = 0.0
      
    match choose:
        case 1:
            if a == 0 and b == 0 and c == 0:
                print("Безкінечне рішення") #Значення коренів можуть бути будь які
            elif a == 0 and b != 0 and c != 0:
                x_one = -(c / b)   
                print(x_one)
            elif a == 0 and b == 0 and c != 0:
                print("Не має рішення")  # no sol
            elif a == 0 and b != 0 and c == 0:
                x_one = 0
                print(f"Рівняння має один корінь :{x_one}")
            d = (b ** 2) - (4 * a * c)
            if d < 0:
                print("Рівняння немає дійсних коренів!")
            elif d == 0:
                x_one = x_two = - b / (2 * a)
                print(f"Рівняння має один корінь :{x_one}")
            elif d > 0:
                x_one = (- b + (d ** 0.5)) / (2 * a)
                x_two = (- b - (d ** 0.5)) / (2 * a)
                print(f"Рівняння має два корені: х1 = {round(x_one,1)}, x2 = {round(x_two,2)}") 
        case 2:
            if a == 0 and b == 0 and c == 0:
                print("Безкінечне рішення")
            elif a == 0 and b != 0 and c != 0:
                x_one = -(c / b)   
                print(x_one)
            elif a == 0 and b == 0 and c != 0:
                print("Не має рішення")  
            elif a == 0 and b != 0 and c == 0:
                x_one = 0
                print(f"Рівняння має один корінь :{x_one}")
            elif x_one * x_two == -b and x_one + x_two == c:
                for i in range(-b,c):
                    x_one * x_two == -b and x_one + x_two == c
                    
    return x_one, x_two
discriminant(a, b, c, choose)