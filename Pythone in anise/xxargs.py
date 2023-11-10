#xargs
'''def add(*numbers):
    print(numbers)

add(10,10)    
add(10,20,30)'''

def add(*numbers):
    sum = 0
    for num in numbers:
       sum = sum + num
    print(sum)   

add(10,10)    
add(10,20,30)