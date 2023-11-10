#Sub class
class Phone:
    def call(self):
        print("You can call")

    def massage(self):
        print("You can massage")

#Super class
class Samsang(Phone):#Inheritence
    #call
    #massage
    def photo(self):
        print("You can take photo")

s = Samsang()
s.massage()
s.call()
s.photo()
#print(issubclass(Samsang,Phone)) #সাব ক্লাস কিনা চেক করার জন্য

