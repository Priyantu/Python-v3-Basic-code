class Student: # create a cllass
    roll = ""
    gpa = ""

rohim = Student() #creat a object
print(isinstance(rohim,Student)) #chak creat object or not

rohim.roll = 101
rohim.gpa = 3.00
print(f"Rohim Roll: {rohim.roll}, GPA: {rohim.gpa}")


korim = Student()
korim.gpa = 3.00
korim.roll = 1120
print(f"Korim Roll: {korim.roll}, Korim gpa: {korim.gpa}")
