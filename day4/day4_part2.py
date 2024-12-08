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
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1),  # down-right
    ]

    xmas_count = 0
    for i in range(length_y):
        for j in range(length_x):
            if grid[i][j] == "A":
                # first letter is A

                # check all 4 corners
                word = ""
                for x, y in directions:
                    new_i = i + x
                    new_j = j + y

                    # check if we don't go over grid
                    if boundary_check(new_i, new_j, length_x, length_y):
                        word += grid[new_i][new_j]
                    else:
                        # no need to continue this direction if we go out of the grid
                        break
                if word == "MSMS" or word == "SMSM" or word == "SSMM" or word == "MMSS":
                    xmas_count += 1

    print(xmas_count)


def boundary_check(i, j, length_x, length_y):
    if 0 <= i < length_y and 0 <= j < length_x:
        return True
    return False


if __name__ == "__main__":
    main()
