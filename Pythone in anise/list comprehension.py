num = [1,2,3,4,5]
'''
Normal 

result = list(map(lambda x: x*x,num))
print(result)
'''
# comprehensive

result = [x*x for x in num]
print(result)