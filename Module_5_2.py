"""
Домашнее задание по уроку "Специальные методы классов"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс House
Создайте инициализатор для класса House, который будет задавать атрибут этажности
self.numberOfFloors = 0
Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут
 numberOfFloors на параметр floors и выводить в консоль numberOfFloors
Полученный код напишите в ответ к домашнему заданию

"""
class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors
        print(f"Количество этажей в доме: {self.number_of_floors}")