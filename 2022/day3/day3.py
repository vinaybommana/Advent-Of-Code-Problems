# input: input3.txt
import string


def read_input(filename):
    with open(filename) as o:
        input_data = o.readlines()
    return input_data


def get_priority_value(item):
    if item in string.ascii_lowercase:
        value = ord(item) - 96  # ord('a') == 97 priority should be 1
    if item in string.ascii_uppercase:
        value = ord(item) - 38  # ord('A') == 65 priority should be 27
    return value


def get_priority_item(input_line):
    # print(len(input_line) % 2 == 0) no False items in input
    first_compartment = set(input_line[0 : int(len(input_line) / 2)])
    second_compartment = set(input_line[int(len(input_line) / 2) : int(len(input_line))])

    priority_item = first_compartment.intersection(second_compartment)
    # print(len(priority_item))
    priority_item = priority_item.pop()
    return get_priority_value(priority_item)


def get_sum_of_priorities(input_data):
    sum_of_priorities = 0
    for line in input_data:
        sum_of_priorities += get_priority_item(line)

    return sum_of_priorities


# part 2
def get_sum_of_priorities_by_group(input_data):
    sum_of_priorities = 0
    # the input_data is now divided into groups of 3
    N = 3 # group count
    groups_data = [input_data[n:n+N] for n in range(0, len(input_data), N)]
    # print(len(groups_data), len(groups_data[0]))
    for group_data in groups_data:
        sum_of_priorities += get_priority_by_group(group_data)
    return sum_of_priorities


def get_priority_by_group(group_data):
    sack_a = set(group_data[0])
    sack_b = set(group_data[1])
    sack_c = set(group_data[2])
    priority_items = sack_a.intersection(sack_b)
    priority_items = priority_items.intersection(sack_c)
    item = priority_items.pop()
    return get_priority_value(item)

if __name__ == "__main__":
    input_data = read_input("input3.txt")
    input_data = [i.strip() for i in input_data if i]
    # input_data = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw",
    # ]
    # assert get_priority_item("vJrwpWtwJgWrhcsFMMfFFhFp") == 16
    # assert get_priority_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == 38
    # assert get_priority_item("PmmdzqPrVvPwwTWBwg") == 42
    # assert get_sum_of_priorities(input_data) == 157
    # assert get_sum_of_priorities_by_group(input_data) == 70
    print(get_sum_of_priorities(input_data))
    print(get_sum_of_priorities_by_group(input_data))

