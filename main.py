# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


class Circle:
    def __init__(self, radius, x, y, point_name):
        self.radius = radius
        self.x = x
        self.y = y
        self.point_name = point_name

    def input_attributes(self):
        self.y = float(input("Faka ipoyint ka Y  :"))
        self.x = float(input("Faka ipoyint ka X  :"))
        self.point_name = input("Faka igama lepoyint :")
        self.radius = float(input("Faka iradiyasi  :"))

    def calculate_Area(self):
        Area = 3.14*self.radius*self.radius
        return Area

    def calculate_perimeter(self):
        perimeter = 2*3.14*self.radius
        return perimeter


    def checking_point(self):
        x_origin = 0
        y_origin = 0
        distance = math.sqrt((self.x - x_origin) ** 2 + (self.y - y_origin) ** 2)
        if distance > self.radius:
            point = "ingaphandle kwesekile"
        else:
            point = "ingaphakathi kwesekile"
        return point


    def output_results(self, perimeter, area, check):
            print("Iperimitha yalesekile ngu  :", perimeter,"meters")
            print(" ieriya yalesekile ngu  :", area,"meters")
            print("le point", (self.x, self.y), " ", check)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Circle(0.0, 0.0, "", 0.0)
    obj.input_attributes()
    area = obj.calculate_Area()
    perimeter = obj.calculate_perimeter()
    check = obj.checking_point()
    obj.output_results(perimeter, area, check)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
