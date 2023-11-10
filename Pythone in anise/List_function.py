subject = ["C","C++","Java","Python","BASIC","Rubi"]
print(len(subject)) # len ফাংশনের লেন্ত বরে করার জন্য।
subject.append("TOC")
print(subject) # append এর মধ্যে থাকা ওয়াড লিস্ট এর শেষে যু্ক্ত হবে।
subject.insert(2,"MAC OS")
print(subject) # insert যে কোন তম ইনডেক্স এ কোন কিছু যুক্ত করার জন্য।
subject.remove("C++")
print(subject) # remove কোন কিছু বাদ দেওয়ার জন্য ব্যাবহার করা হয়।

mon = [30,10,20,50,80,70,90]
mon.sort()
print(mon) # sort সিরিয়ালি ছোট থেকে বড় আকারে সাজিয়ে লেখার জন্য।

mon.reverse()
print(mon) # sort সিরিয়ালি বড় থেকে ছোট আকারে সাজিয়ে লেখার জন্য।

mon.pop()
print(mon) # ১ বার pop ফাংশন ব্যাবহার এর ফলে লিস্ট এর শেষের ১ টি বাদ হয়ে যাবে। ২ বার pop ফাংশন ব্যাবহার এর ফলে লিস্ট এর শেষের ২ টি বাদ হয়ে যাবে।

sob = [10,20,20,30,40,5,60]
po = sob.index(20)
print(po) # index কোন সংখ্যা কত তম ইনডেক্স এ আছে তা দেখতে 

po = sob.count(20)
print(po) # count লিস্টে কয় বার আছে তা দেখার জন্য।#24