# number1 = (4, 6, 3, 7, 4)
# number2 = (5, 4, 2, 5, 3)
# n1 = number1 + number2
# n1 = set(n1)
# print(sorted(n1,reverse=True))

# word1 = input('soz jaz kozu: ')
# word2 = input('soz jaz kozu: ')
# wor1 = sorted(word1)
# wor2 = sorted(word2)
# if wor2 == wor1:
#     print('anagramma')
# else:
#     print('anagramma emes')



# number = int(input('san jaz: '))
# if number % 2 == 0:
#     print('Jup san')
# else:
#     print('Tak san')






cars = {'car_name': 'mers', 'model': 'AMG', 'price': 50000}
car = input('write a key: ')
if car in cars:
    print(cars[car])
else:
    print('Error')
