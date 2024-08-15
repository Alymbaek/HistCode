
'''''
class Products:
    def __init__(self,name,razmer,tysy,Sena):
        self.name = name
        self.razmer = razmer
        self.tysy = tysy
        self.Sena = Sena

    def produkt(self):
            return f'Продукт: {self.name}, Размер: {self.razmer}, Свет: {self.tysy}, Цена: {self.Sena}'

pro1 = Products('Nake', '42', 'Белый', 6900)
pro2 = Products('Adidas', '41', 'Серий', 5900)
pro3 = Products('Polo', '44', 'Малочный', 7000)
print(pro1.produkt())
print(pro2.produkt())
print(pro3.produkt())
'''


class House:
    def __init__(self,street,number):
        self.street = street
        self.number = number
    def kocho(self):
        return f'Дом на улице {self.street} под номером {self.number} построен'

House1 = House('Абдыкадыров',204)
House2 = House('Юсупа Адбыразманова', 170)
House3 = House('Куренкеева', 29)
print(House1.kocho())
print(House2.kocho())
print(House3.kocho())





































