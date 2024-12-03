import re

pattern = r"mul\((\d+),(\d+)\)"

with open('input.txt', 'r') as file:
    text = file.read()

matches = re.findall(pattern, text, flags=re.DOTALL)

total = 0
for x , y in matches:
    total += int(x) * int(y)

print(total)