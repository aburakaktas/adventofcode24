import re

pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

with open('input.txt', 'r') as file:
    text = file.read()

matches = re.findall(pattern, text, flags=re.DOTALL)

flag = 1
muls = []
for item in matches:
    if flag == 1:
        if item[:3] == 'mul':
            muls.append(item)
        if item == "don't()":
            flag = 0
    if flag == 0:
        if item == "do()":
            flag = 1

pattern2 = r"mul\((\d*),(\d*)\)"

total = 0
for item in muls:
    matches = re.findall(pattern2, item)
    for x,y in matches:
        total += int(x) * int(y)

print(total)