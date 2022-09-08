# source: https://python.plainenglish.io/oops-implementation-of-its-four-pillars-in-python-in-reference-with-java-495091491f8d

# class vehicle:
#     def __init__(self, reg_no, color):
#         self.reg_no=reg_no
#         self.color=color
#     def getColor(self):
#         print("The color of the car is", self.color)

# def main():
#     f1=vehicle(1234, "red")
#     f1.getColor()

# if __name__=="__main__":
#     main()

# Inheritance: fourwheeler takes vehicle and adds torque and gear_box
# class vehicle:
#     def __init__(self, reg_id, num_wheels, color):
#         self.reg_id=reg_id
#         self.num_wheels=num_wheels
#         self.color=color
#     def getDetails(self):
#         print(f'Registration Number is: {self.reg_id}')
#         print(f'Number of Wheels: {self.num_wheels}')
#         print(f'Color: {self.color}')

# class fourwheeler(vehicle):
#     def __init__(self, reg_id, num_wheels, color, torque, gear_box):
#         super().__init__(reg_id, num_wheels, color)
#         self.torque=torque
#         self.gear_box=gear_box
#     def getDetails(self):
#         super().getDetails()
#         print(f'Torque: {self.torque}')
#         print(f'Gear Box: {self.gear_box}')

# def main():
#     f1=fourwheeler(1234, 4, "gray", 345, 'automatic')
#     f1.getDetails()

# if __name__ == "__main__":
#     main()

# my inheritance example:
# class coffee:
#     def __init__(self, region, weight):
#         self.region=region
#         self.weight=weight
#     def details(self):
#         print(f'Region: {self.region}')
#         print(f'Weight: {self.weight}')

# class sumatra(coffee):
#     def __init__(self, region, weight, roast):
#         super().__init__(region, weight)
#         self.roast=roast
#     def details(self):
#         super().details()
#         print(f'Roast: {self.roast}')

# def main():
#     bean1=sumatra('Sumatra', 100, 'Dark')
#     bean1.details()

# if __name__ == "__main__":
#     main()

# Encapsulation is the bundling of methods with data on which methods operate
class vehicle:
    def setter(self, name, speed):
        self.__name=name
        self.__speed=speed
    def getter(self):
        print(f'{self.__name}, {self.__speed}')

def main():
    v=vehicle()
    v.setter('car', 150)
    v.getter()

if __name__ == "__main__":
    main()