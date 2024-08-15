# print('Start')
# for u in range(1,11):
#     print(u * 10)
# print('Stop')
import random

# r = 0
# s = int(input('san: '))
# print('Start')
# print(s)
# while s != -1:
#         print(s)
#         s -= 1
#         r += s
# print('Stop')
# print(f'sum {r}')



# numbers = [3, 43, -54, -64, 7]
# new_list = numbers[1]
# for m in numbers[1:]:
#     if m < -1:
#         new_list = [m]
#         print(new_list)





# r = 0
# one = int(input('1 san: '))
# two = int(input('2 san: '))
# for i in range(one,two+1):
#     r += i
# print(f'sum== {r}')







#
# numbers = [4, 6, 2, 6, 7, 3, 1]
# new_number = []
# for w in numbers:
#     if w % 2 != 0:
#         new_number.append(w)
# print(new_number)







#
# one = int(input('1 san: '))
# two = int(input('2 san: '))
# r = 0
# for w in range(one, two+1):
#     r += w
# print(f'sum== {r}')






# r = input('jaz: ')
# r1 = input('jaz: ')
# if r1 in r.split()[-1]:
#     print('Palindrom ')
# else:
#     print('Palindrom emes')





# q = 0
# while True:
#   r = int(input('san: '))
#   q += r
#   if r == 0:
#       print(f'sum: {q}')














# while True:
#     w1 = int(input('san: '))
#     w2 = int(input('san: '))
#     q = input('* - + /')
#     if q == '*':
#         print(w1 * w2)
#     elif q == '-':
#         print(w1 - w2)
#     elif q == '+':
#         print(w1 + w2)
#     elif q == '/':
#         print(w1 / w2)
#     else:
#         print('Error')


# r1 = int(input('san: '))
# r2 = int(input('san: '))
# q = 0
# for k in range(r1,r2,10):
#     print(k)
#     q +=k
# print(f'sum: {q}')







# w = int(input('san: '))
# for l in range(1,11):
#     print(f'{w} * {l} = {w*l}')







# numbers = [4, 6, 2, 6, 7, 3, 1]
# # new_number = numbers[0]
# # for u in numbers[1:]:
# #     if u % 2 == 0:
# #      print(f'{new_number} + {u} = {new_number + u}')


# [num * idx for idx, num in enumerate(lst)]








class Shape:
    def __init__(self,a):
        self.a = a
    def perimetr(self):
        pass
class Rectangle(Shape):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b

    def perimetr(self):
        sum = self.a + self.b
        return f'{sum*2}sm'

rec1 = Rectangle(4,5)
print(rec1.perimetr())
class Triangle(Rectangle):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c

    def perimetr(self):
        return f'{self.a * self.b * self.c}sm'

tr1 = Triangle(4,5,2)
print(tr1.perimetr())
























































