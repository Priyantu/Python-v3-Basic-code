from collections import deque

bank = deque(['Anis','Korim','Bijoy'])
print(bank)

bank.popleft()
print(bank)

bank.popleft()

bank.popleft()

if not bank:   #it works Stack was full empty
    print("No person left")