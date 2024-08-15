# def get_values():
#     try:
#         x,y = map(int,input().split())
#         return x,y
#     except ValueError as d:
#         print(d)
#         return 0,0
#     finally:
#         print('finally выполняется до return')
# x,y = get_values()
# print(x,y)


# ter = [4, 5, 2, 7, 8]
# def heta(numbers):
#     new_number = []
#     for n in numbers:
#         n *= numbers.index(n)
#         new_number.append(n)
#     return new_number
#
# print(heta([1,5,4,3,7,6,7,8,9]))
#
#

# def change_number(number):
#     new_list = []
#     for i in number:
#         if i % 5 == 0:
#             new_list.append(i*5)
#         elif i % 3==0:
#             new_list.append(i * 3)
#         else:
#             new_list.append(i)
#     return new_list
#
# print(change_number([5, 2, 7, 6, 10, 0, 12]))


'''''
class Product:
    def __init__(self,name,price,description,category,year):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.year = year

    def show(self):
        return f'{self.name},{self.price}.{self.description},{self.category},{self.year}'

product1 = Product('Nike boots', 4000, 'mykty', 'shoes', 2020)
product2 = Product('Adidas boots', 3500, 'hjfjs', 'cros', 2023)
print(product1.show())

class Computer(Product):


    def show(self):
        return f'{self.name},{self.price},{self.description},{self.category},{self.year},{self.model}'

computer1 =Computer('Asus', 69000, 'Ынгайлуу', 'Laptop', 2023, 'S Pro')
computer2 =Computer('IPhone', 89000, 'Сапатуу', 'Phone', 2024, '15 Pro')
print(computer1.show())


'''


class Shape:
    def __init__(self, a):
        self.a = a

    def perimetr(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a,)
        self.b = b

    def perimetr(self):
        ret = self.a + self.b
        return f'{ret * 2}sm'

rec1 = Rectangle(4, 5)
print(rec1.perimetr())  #18 sm

class Triangle(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a,b)
        self.c = c

    def perimetr(self):
            return f'{self.a * self.b * self.c}sm'

tr1 = Triangle(4, 5, 2)
print(tr1.perimetr())




























