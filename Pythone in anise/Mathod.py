class Student: # create a cllass
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rohim = Student() #creat a object
rohim.set_value(110,2.40)
rohim.display()

korim = Student()
korim.set_value(120,2.75)
korim.display()