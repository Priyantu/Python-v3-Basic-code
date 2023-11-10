class Student: # create a cllass
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rohim = Student(110,3.75) #creat a object
rohim.display()

korim = Student(120,3.80)
korim.display()