# input4.txt

def read_input(filename):
    with open(filename) as o:
        input_data = o.readlines()
    return input_data


def parse_input_line(input_line):
    first_bound, second_bound = input_line.split(",")
    fb_x, fb_y = first_bound.split("-")
    sb_x, sb_y = second_bound.split("-")

    fb_x = int(fb_x)
    fb_y = int(fb_y)
    sb_x = int(sb_x)
    sb_y = int(sb_y)
    return fb_x, fb_y, sb_x, sb_y


def check_full_bounds(input_line):
    fb_x, fb_y, sb_x, sb_y = parse_input_line(input_line)

    # check if second_bound is fully in first_bound
    if (sb_x >= fb_x) and (sb_y <= fb_y):
        return True
    if (fb_x >= sb_x) and (fb_y <= sb_y):
        return True
    return False


def check_bound_pairs(input_data, check_function):
    fully_included_pairs = 0
    for input_line in input_data:
        if check_function(input_line):
            fully_included_pairs += 1
    return fully_included_pairs


# part 2
def check_overlapping_bounds(input_line):
    fb_x, fb_y, sb_x, sb_y = parse_input_line(input_line)

    if check_full_bounds(input_line):
        return True
    if sb_x >= fb_x and sb_x <= fb_y:
        return True
    if fb_x >= sb_x and fb_x <= sb_y:
        return True
    return False


if __name__ == "__main__":
    input_data = read_input("input4.txt")
    test_input_data = read_input("test_input.txt")
    assert check_bound_pairs(test_input_data, check_full_bounds) == 2
    assert check_bound_pairs(test_input_data, check_overlapping_bounds) == 4
    # print(check_bound_pairs(test_input_data, check_overlapping_bounds))
    print(check_bound_pairs(input_data))
    print(check_bound_pairs(input_data, check_overlapping_bounds))
