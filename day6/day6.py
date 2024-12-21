def main():
    grid = read_input("input.txt")

    y, x = find_start(grid)

    while True:
        grid, y, x = go_up_until_hit(grid, y, x)
        if y is None or x is None:
            print("Guard has left the grid.")
            break

        grid, y, x = go_right_until_hit(grid, y, x)
        if y is None or x is None:
            print("Guard has left the grid.")
            break

        grid, y, x = go_down_until_hit(grid, y, x)
        if y is None or x is None:
            print("Guard has left the grid.")
            break

        grid, y, x = go_left_until_hit(grid, y, x)
        if y is None or x is None:
            print("Guard has left the grid.")
            break

    print(calculate_path_count(grid))


def go_left_until_hit(grid, y, x):
    while not check_if_out_of_grid(grid, y, x):
        if grid[y][x] == "#":
            return [grid, y, x + 1]
        grid[y][x] = "x"
        x -= 1
    print("Leaving the grid at:", y, x)
    return [grid, None, None]


def go_down_until_hit(grid, y, x):
    while not check_if_out_of_grid(grid, y, x):
        if grid[y][x] == "#":
            return [grid, y - 1, x]
        grid[y][x] = "x"
        y += 1
    print("Leaving the grid at:", y, x)
    return [grid, None, None]


def go_right_until_hit(grid, y, x):
    while not check_if_out_of_grid(grid, y, x):
        if grid[y][x] == "#":
            return [grid, y, x - 1]
        grid[y][x] = "x"
        x += 1
    print("Leaving the grid at:", y, x)
    return [grid, None, None]


def go_up_until_hit(grid, y, x):
    while not check_if_out_of_grid(grid, y, x):
        if grid[y][x] == "#":
            return [grid, y + 1, x]
        grid[y][x] = "x"
        y -= 1
    print("Leaving the grid at:", y, x)
    return [grid, None, None]


# determine the start point coordinate of the guard
def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i, j


def check_if_out_of_grid(grid, y, x):
    return not (0 <= y < len(grid) and 0 <= x < len(grid[0]))


def nice_print(grid):
    for line in grid:
        print("".join(line))


def read_input(file_name):
    grid = []
    with open(file_name, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def calculate_path_count(grid):
    return sum(1 for row in grid for cell in row if cell == "x")


if __name__ == "__main__":
    main()
