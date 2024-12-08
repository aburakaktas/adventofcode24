def main():

    rules = {}
    pages = []
    with open("input.txt", "r") as file:
        is_second_part = 0
        for line in file:
            if line.strip() == "":
                is_second_part = 1
                continue

            if is_second_part == 0:
                tmp_key_value = line.strip().split("|")
                rule_key = int(tmp_key_value[0])
                rule_value = int(tmp_key_value[1])

                if rule_key in rules:
                    rules[rule_key].append(rule_value)
                else:
                    rules[rule_key] = []
                    rules[rule_key].append(rule_value)
            else:
                pages.append(list(map(int, line.strip().split(","))))

    middle_totals = 0
    for page in pages:
        middle_index = int(len(page) / 2)
        if check_rule(page, rules):
            middle_totals += page[middle_index]

    print(middle_totals)


# tells if a page passes the rule
def check_rule(page, rules):
    # reverse the list
    reversed_page = list(reversed(page))
    page_length = len(reversed_page)
    for i in range(page_length):
        # find the current banned list
        try:
            current_banned_list = rules[reversed_page[i]]
        except KeyError:
            # print("no banned list found for", reversed_page[i])
            continue

        for j in range(i + 1, page_length):
            if reversed_page[j] in current_banned_list:
                return False
    return True


if __name__ == "__main__":
    main()
