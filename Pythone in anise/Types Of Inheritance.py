#Multiple Inheritance
class A:
    def display1(self):
        print("I am inside A class")

class B:
    def display2(self):
        print("I am inside B class")

class C(A,B):
    def display(self):
        print("I am inside C class")

ob1 = C()
ob1.display()
                        