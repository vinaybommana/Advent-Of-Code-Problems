# day 5
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

import re

test_input_stack = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

input_stack = [
    ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
    ['D', 'Q', 'L'],
    ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
    ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
    ['V', 'G', 'L', 'F', 'Z', 'S'],
    ['D', 'G', 'N', 'P'],
    ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
    ['C', 'P', 'D', 'M', 'S'],
    ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C'],
]


def read_input(filename):
    with open(filename) as o:
        input_data = o.readlines()
    return input_data


def execute_instruction_9000(input_line, input_stack):
    # print("Enter input stack: ")
    # print(input_stack)
    # print(input_line)
    crate_count, from_crate, to_crate = re.findall(r'\d+', input_line)
    # print(crate_count, from_crate, to_crate)
    crate_count = int(crate_count)
    from_crate = int(from_crate) - 1
    to_crate = int(to_crate) - 1
    from_crate_stack = input_stack[from_crate]
    to_crate_stack = input_stack[to_crate]
    for _ in range(crate_count):
        # print(i)
        item = from_crate_stack.pop()
        to_crate_stack.append(item)
    # print("After instruction:")
    # print(input_stack)
    return input_stack


# part 2
def execute_instruction_9001(input_line, input_stack):
    # print("Enter input stack: ")
    # print(input_stack)
    # print(input_line)
    crate_count, from_crate, to_crate = re.findall(r'\d+', input_line)
    # print(crate_count, from_crate, to_crate)
    crate_count = int(crate_count)
    from_crate = int(from_crate) - 1
    to_crate = int(to_crate) - 1
    from_crate_stack = input_stack[from_crate]
    to_crate_stack = input_stack[to_crate]
    items = []
    for _ in range(crate_count):
        # print(i)
        items.append(from_crate_stack.pop())
    items = items[::-1]
    to_crate_stack += items
    # print("After instruction:")
    # print(input_stack)
    return input_stack


def parse_instructions(input_data, input_stack, execute_instruction):
    for input_line in input_data:
        input_stack = execute_instruction(input_line, input_stack)
    
    elves_message = ''
    for stack in input_stack:
        elves_message += stack.pop()
    return elves_message


if __name__ == "__main__":
    test_input_data = read_input("test_input.txt")
    input_data = read_input("input5.txt")
    # assert parse_instructions(test_input_data, test_input_stack) == "CMZ"
    assert parse_instructions(test_input_data, test_input_stack, execute_instruction_9001) == "MCD"
    # print(parse_instructions_9000(input_data, input_stack))
    print(parse_instructions(input_data, input_stack, execute_instruction_9001))