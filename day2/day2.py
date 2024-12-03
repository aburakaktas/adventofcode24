
def main():

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    safe_count = 0
    report_count = 1
    for line in lines:
        report = [int(x) for x in line.split()]
        # print(report)
        # print(report_count)
        report_count += 1
        
        if is_increasing(report) or is_decreasing(report):
            pass
            if check_diff(report):
                safe_count += 1
    print(safe_count)



# check difference is btw 1 to 3

def check_diff(report):
    length = len(report)

    for i in range(length-1):
        difference = abs(report[i] - report[i + 1])
        if difference > 3 or difference < 1:
            return False
    return True

# check if constantly increasing
def is_increasing(report):
    lowest = 0
    for level in report:
        if level > lowest:
            lowest = level
        else:
            return False
    return True

# check if constantly decreasing 
def is_decreasing(report):
    highest = 100
    
    for level in report:
        if level < highest:
            highest = level
        else:
            return False
        
    return True


if __name__ == "__main__":
    main()
