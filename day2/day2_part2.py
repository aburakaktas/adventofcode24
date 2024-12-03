
def main():

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    safe_count = 0
    for line in lines:
        report = [int(x) for x in line.split()]
        if process_report(report):
            safe_count += 1
            print("first logic", report)
        else:
            life = 1
            length = len(report)
            for i in range(length):
                temp = report[:i] + report[i+1:]
                if life == 1 and process_report(temp):
                    life = 0
                    safe_count += 1
                    print("second logic", temp)

    print(safe_count)








def process_report(report):
    return (is_increasing(report) or is_decreasing(report)) and check_diff(report)


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
