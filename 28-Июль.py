
''''
class Product:
    def __init__(self,name, price, description, category, year):
        self.name = name
        self.price = price
        self.description = description
        self.category= category
        self.year = year
    def market(self):
        return f'Название Бренда: {self.name}, Цена: {self.price}, Описания: {self.description}, Категория: {self.category}, Год Произведение: {self.year}'

produktion = Product('Nake Boots', 4000, 'У нас Качественые Бренды', 'Lx', 2022 )
print(produktion.market())


class Brend(Product):
    def __init__(self, name, price, description, category, year, razmer):
        super().__init__(name, price, description, category, year)
        self.razmer = razmer

    def recta(self):
      return f'Название Бренда: {self.name}, Цена: {self.price}, Описания: {self.description}, Категория: {self.category}, Год Произведение: {self.year}, Размер: {self.razmer}'


produktion1 = Brend('Loro Piana', 7900, 'У нас Качественые Бренды', '', 2023, 40)
print(produktion1.recta())



#
# numbers = [1,3,4,5,7,8,9]
# new_list = []
# san = int(input('San jaz: '))
# for number in numbers:
#     kemitindi = san - number
#     if kemitindi in new_list:
#         print(kemitindi,number)
#     else:
#         new_list.append(number)












# def calculate_average(numbers):
#     if numbers:
#         sum_numbers = sum(numbers)
#         total = sum_numbers / len(numbers)
#         return total
# print(calculate_average([1,2,3,4,5]))









# def is_prime(number):
#     if number % 2 == 0:
#         return 'True'
#     else:
#         return 'False'
#
# print(is_prime(8))

'''




























































