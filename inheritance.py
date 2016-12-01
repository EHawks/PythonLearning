class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


jon_snow = Parent("Snow", "Brown")
print(jon_snow.last_name)

bill_snow = Child("Snow", "Blue", 3)
print(bill_snow.number_of_toys)
