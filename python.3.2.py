cars = ['tesla', 'mers', 'audi', 'mers', 'audi', 'audi', 'audi', ]
name_cars = input("name of cars:").lower()
if name_cars in cars:
    print(cars.count(name_cars))

else:
    print("jok")
