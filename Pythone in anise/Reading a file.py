# video number 46
file = open("student.txt","r")
#print(file.readable())
text = file.read()#ফাইলে থাকা লেখা পড়ার জন্য
print(text)
size = len(text)#সাইজ দেখার জন্য
print(size)

text = file.readlines()[1] #যে কোন একটি লাইন প্রিন্ট করার জন্য
file.close()