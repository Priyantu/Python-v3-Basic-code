class Phone:
     def __init__(self):
          print("I am in Phone class")

class Samsang(Phone):
     '''
     def __init__(self):
          print("I am in Phone class")
     '''      

     def __init__(self):
          super().__init__()  
          print("I am in Samsang class") 

S = Samsang()            