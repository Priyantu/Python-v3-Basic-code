# find the number of degit, number of leter, number of words(video 31)

numOfWord = 0
numOfletters = 0
numOfdigite = 0

text = input('Enter a text of number: ')

for x in text:
    x = x.lower()
    if x >='a' and x <='z':
        numOfletters = numOfletters + 1

    elif x >='0' and x <='9':
        numOfdigite = numOfdigite + 1 

    elif x ==' ':
        numOfWord = numOfWord + 1 

print("Digite: ",numOfdigite)
print("Letter: ",numOfletters)
print("Word: ",numOfWord + 1)          