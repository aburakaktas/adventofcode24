def main():
    grid = []

    with open("input.txt", "r") as file:
        for line in file:
            temp = []
            for letter in line.strip():
                temp.append(letter)
            grid.append(temp)

    length_x = len(grid[0])
    length_y = len(grid)

    directions = [
        (0, 1),  # right
        (0, -1), # left
        (1, 0),  # down
        (-1, 0), # up
        (1, 1),  # down-right
        (-1, -1), # up-left
        (1, -1), # down-left
        (-1, 1), # up-right
    ]

    xmas_count = 0
    for i in range(length_y):
        for j in range(length_x):
            if grid[i][j] == 'X':
                # first letter is X
                for dx, dy in directions:
                    word = ""
                    for k in range(4):
                        new_i = i + k * dx
                        new_j = j + k * dy

                        # check if we don't go over grid
                        if boundary_check(new_i, new_j, length_x, length_y):
                            word += grid[new_i][new_j]
                        else:
                            # no need to continue this direction if we go out of the grid
                            break
                    if word == "XMAS":
                        xmas_count += 1
                    

    print(xmas_count)

def boundary_check(i, j, length_x, length_y):
    if 0 <= i < length_y and 0 <= j < length_x:
        return True
    return False



if __name__ == "__main__":
    main()