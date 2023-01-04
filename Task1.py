# Вычислить число с заданной точностью *d*
#$d =0.001, Ꞃ = 3.141

# num = float(input('Введите число: ')) 

# def fun (d:float):
#     import math
#     math.pi
#     count = 0
#     while d % 1 != 0:
#         d *= 10
#         count += 1
#     result = round(math.pi,count)
#     return result  
 
# print(fun(num))

## или

# import math
# math.pi
# #3.141592653589793
# print(str(math.pi).split('.')[0] +'.'+ str(math.pi).split('.')[1][0:2])

## т.е. через функцию

# num = float(input('Введите заданную точность: '))

# def fun (d:float):
#     import math
#     math.pi
#     count = 0
#     while d % 1 != 0:
#         d *= 10
#         count += 1
#     result = str(math.pi).split('.')[0] + '.' + str(math.pi).split('.')[1][0:count]
#     return result  
 
# print(fun(num))

## если ввести точность просто цифрой(кол-во знаков после запятой)
def input_number():
    while True:
        num = input('Введите число: ')
        try:
            number = float(num)
            return number
        except:
            print('Вы ввели не число! Попробуйте снова!')

def input_count():
    while True:
        num = input('Введите точность округления (количество знаков после запятой)')
        try:
            numbers = int(num)
            return numbers
        except:
            print('Вы ввели не число! Попробуйте снова!')    

number = input_number()
count = input_count()
print(f'{number:.{count}f}') #форматирование - перед второй f показывает количество знаков после запятой

