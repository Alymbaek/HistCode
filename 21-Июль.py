# def greet(name):
#     print(f"Привет, {name}!")
# greet('Alymbek')





# numbers = [4, 5, 2, 5, 0, 5]
# def rane(numbers):
#
#     if new_number in numbers:
#         print('Bar')
#     else:
#         print('Jok')
# new_number = int(input('сан жаз: '))
# print(rane([4, 5, 2, 5, 0, 5]))








# cars = ['tesla', 'byd', 'audi', 'mers', 'bmw']
#
# def tron(cars):
#     if car in cars:
#         cars.remove(car)
#         return cars
#     else:
#         print('no')
# car = input('name of car: ')
# print(tron(['tesla', 'byd', 'audi', 'mers', 'bmw']))







# cars = ['tesla', 'byd', 'audi', 'mers', 'bmw']
# def tron(cars):
#     if cars[i] in cars:
#         cars.pop(i)
#         return cars
#     else:
#         print('no')
# i = int(input('index of car: '))
# print(tron(['tesla', 'byd', 'audi', 'mers', 'bmw']))












# cars = ['tesla', 'mers', 'audi', 'mers', 'audi', 'audi', 'audi', ]
#
# def tru(cars):
#     if r in cars:
#         return cars.index(r)
#
#
# r = input('jaz: ')
# print(tru(['tesla', 'mers', 'audi', 'mers', 'audi', 'audi', 'audi', ]))












# def bet(der):
#     if i in der:
#         return der.count(i)
#
# i = input('jaz: ')
# print(bet(['tesla', 'mers', 'audi', 'mers', 'audi', 'audi', 'audi', ]))









# def tuy(rena):
#     return len(name.split()[-1])
#
# name = input('jaz: ')
# print(tuy(name))






# numbers = [2,7,8,11]
# pero = 9
# venom = {}
# for index, number in enumerate(numbers):
#     fer = pero - number
#     if fer in venom:
#         print(venom[fer], index)
#         break
#     else:
#         venom[number] = index
''''
def print_data(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

print_data(name='Alymbek',age=16,job='Programist')
'''


# def calculate_average(numbers):
#     if numbers:
#         sum_number = sum(numbers)
#         rezult = sum_number / len(numbers)
#         return rezult
#
# print(calculate_average([1, 2, 3, 4, 5,6,]))


# def is_prime(nmber):
#     if nmber % 2 == 0:
#         return 'True'
#     else:
#         return 'False'
# print(is_prime(12))





def unique_elements(numbers):
    new_number = []
    for i in numbers:
        if i in new_number:
            continue
        else:
             new_number.append(i)
    return new_number

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))




















































