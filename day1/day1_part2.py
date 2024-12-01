with open('input.txt', 'r') as file:
    lines = file.readlines()

left = []
right = []
for line in lines:
    temp = line.split()
    left.append(int(temp[0]))
    right.append(int(temp[1]))

length = len(left)
result = 0
for i in range(length):
    count = right.count(left[i])
    similarity_score = left[i] * count
    result += similarity_score

print(result)