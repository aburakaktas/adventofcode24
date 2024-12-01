with open('input.txt', 'r') as file:
    lines = file.readlines()

left = []
right = []
for line in lines:
    temp = line.split()
    left.append(int(temp[0]))
    right.append(int(temp[1]))

left_sorted = sorted(left)
right_sorted = sorted(right)
lenght = len(left_sorted)

sum = 0
for i in range(lenght):
    difference = abs(left_sorted[i] - right_sorted[i])
    sum += difference
print(sum)