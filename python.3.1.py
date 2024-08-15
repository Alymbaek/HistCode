cars = ['tesla', 'byd', 'audi', 'mers', 'bmw']
name_cars = input("name of cars:").lower()
if name_cars in cars:
    cars.remove(name_cars)
    print(cars)
    print("ал машина сатылды")
else:
    print("jok")
