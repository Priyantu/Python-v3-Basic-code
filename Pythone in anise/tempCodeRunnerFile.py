import re
pattern = r"Red"
text1 = "My favourite colour is Red.I love blue"
text2 = re.sub(pattern,"Green",text1)
print(text2)