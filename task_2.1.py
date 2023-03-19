# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    a = list(map(int, arr.split()))
    b = sorted(a)[0]
    return b

def maximum(arr):
    a = list(map(int, arr.split()))
    c = sorted(a)[-1]
    return c

arr = input('Введите целые числа (через пробел): ')
    
print('min =', minimum(arr), ',' , 'max =', maximum(arr))