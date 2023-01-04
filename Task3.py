# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности
# [1,1,2,3,4,4,] -> [2,3] (можно встроенным методом)


# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# # [new_lst.append(i) for i in lst if i not in new_lst]
# # print(f"Список из неповторяющихся элементов: {new_lst}")
# for i in lst:
#     if i  not in new_lst:
#         new_lst.append(i)
# print(f"Список из неповторяющихся элементов: {new_lst}")      

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")  
# lst = [1,5,1,2,4,3,4,4,]
# new_lst = []
# for i in range(len(lst)):
#     if lst[i] in lst[i+1:] and lst[i] not in new_lst:
#         new_lst.append(lst[i])
# print(f"Список из повторяющихся элементов: {new_lst}")  
# lst_dif = list(set(lst).difference(set(new_lst)))
# print(f"Список иcключающий повторяющиеся элементы: {lst_dif}") # [2, 3, 5] !!! 


# lst = [1,5,1,2,4,3,4,4,]
# i = 0
# while i < len(lst):
#     if lst[i] in lst[i+1:]:
#         del lst[i]
        
#     else:    
#         i += 1
# print(lst)  #[5, 1, 2, 3, 4] 
# 

# lst = [1,5,1,2,4,3,4,4,]
# my_list = []
# for i in range(len(lst)):
#     if lst.count(i) == 1:  # [2, 3, 5] !!! т.е. если элемент встречается один раз
#         my_list.append(i)
# print(my_list)   
# 
# lst = [1,5,1,2,4,3,4,4,]
# my_list = []     
# for elem in lst:
#     if lst.count(elem) == 1:  # [5,2,3] !!! т.е. если элемент встречается один раз
#         my_list.append(elem)
# print(my_list)  

lst = [1,5,1,2,4,3,4,4,]
new_list = [elem for elem in lst if lst.count(elem) == 1 ] #генератор списка
print(new_list) #[5, 2, 3]

