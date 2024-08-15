
# def print_data(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}:{value}')
#
# print_data(name='Alymbek',age=16,job='Programist')





# def fenc1(x):
#     def fenc2(y):
#         return x+y
#     return fenc2
# closure = fenc1(20000)
# print(closure(120000))





# cars = ['tesla','bmw','audi','mers','tesla','bmw','audi','mers']
# def name_cars(caar):
#     if caar in cars:
#         return cars.count(caar)
#     else:
#          return 'Jok'
#
# cars_name = input('Jaz: ')
# print(name_cars(cars_name))
# print(cars)







# def numbers(r,t):
#     e = r + t
#     return sorted(e,reverse=True)
#
# print(numbers([5,7,1,4],[6,9,3,2]))




# def check_numbers(nuber):
#     if nuber % 2 != 0:
#         return 'Tak san'
#     else:
#         return 'Jup san'
#
#
#
#
# print(check_numbers(5))



# check = lambda number: print('Tak san') if number % 2 != 0 else print('Jup san')
# check(4)








#
# person = {'last_name': 'Asel', 'age': 33, 'number': 3543543}
# def check_key(dicti):
#     if dicti in person:
#         return person[dicti]
#     else:
#         return 'Jok'
#
# print(check_key('age'))




# def uran(numbers):
#     re_lest = []
#     for j in numbers:
#         if j > 0:
#             re_lest.append(j)
#         else:
#             re_lest.append(0)
#     return re_lest
#
#
# print(uran([1,2,-5,-7,-3,6,7,8,-5]))











# def unique_elements(numbers):
#     ret = set(numbers)
#     return ret
#
#
#
#
# print(unique_elements([1, 2, 2, 3, 4, 4, 5]))





# def greet(name):
#      print(f'Привет, {name}! Рад(а) тебя видеть')
# greet('Alymbek')






# def calculate_rectangle_area(width, height):
#
#
#   return width * height
#
# # Вызываем функцию с различными значениями ширины и высоты
# print(f"Площадь прямоугольника с шириной 10 и высотой 10: {calculate_rectangle_area(10, 10)}")
# print(f"Площадь прямоугольника с шириной 3 и высотой 7: {calculate_rectangle_area(3, 7)}")
# print(f"Площадь прямоугольника с шириной 8 и высотой 2: {calculate_rectangle_area(8, 2)}")








# def calculate_factorial(number):
#
#
#   if number < 0:
#     return "Факториал не определен для отрицательных чисел"
#   elif number == 0:
#     return 1
#   else:
#     factorial = 1
#     for i in range(1, number + 1):
#       factorial *= i
#     return factorial
#
# # Вызов функции с различными числами и вывод результатов
# print(f"Факториал 5: {calculate_factorial(5)}")
# print(f"Факториал 0: {calculate_factorial(0)}")
# print(f"Факториал 7: {calculate_factorial(7)}")
# print(f"Факториал -3: {calculate_factorial(-3)}")








# import random
#
# def generate_random_number(min_value, max_value):
#
#   return random.randint(min_value, max_value)
#
# random_number = generate_random_number(1, 100)
# print(random_number)











# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("Ошибка: деление на ноль!")
#         result = None
#     return result
# print(divide(8,0 ))





# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)






# def check_numbers(a, b):
#         total = a.intersection(b)
#         return total
#
# print(list(check_numbers({5, 4, 2, 10}, {5, 7, 0, 10})))


# [5, 10]



# check_numbers = lambda a,b:a.intersection(b)
#
# print(list(check_numbers({5, 4, 2, 10}, {5, 7, 0, 10})))





# class date:
#
# print('Маалымат киргизүү')
# name = input('Студенттин аты-жөнүн киргизиңиз: ')
# grupp = input('Студенттик топту киргизиңиз: ')
# lesson1 = input('Математика сабагын киргизиңиз: ')
# lesson2 = input('Тарых  сабагын киргизиңиз: ')
# lesson3 = input('Физика сабагын киргизиңиз: ')
#
#
# print('Маалымат чыгаруу ')
# print('Студенттин профили:')
# print(f'Толук Аты-жөнү: {name}')
# print(f'Топ: {grupp}')
# print('Баалар:')
# print(f'Математика: {lesson1}')
# print(f'Тарых: {lesson2}')
# print(f'Физика: {lesson3}')








class Person:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def print_info(self):
        return f'Name: {self.first_name, self.last_name}, age: {self.age}, city: {self.city}'


person1 = Person("Alymbek", 'Ibragimov', 17, 'Bishkek')
person2 = Person('Asel', 'Asanova', 43, 'Bishkek')


print(person1.print_info())





























