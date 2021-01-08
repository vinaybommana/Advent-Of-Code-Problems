import copy
test_input = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

def read_input8(filename: str):
    with open(filename) as f:
        return f.read()


def parse_input(_input):
    _dict = {}
    _input = _input.split("\n")
    _input = [i for i in _input if i]
    for index, line in enumerate(_input):
        line = line.split(" ")
        _dict[index] = {"op":line[0], "value":line[1]}
    return _dict


def console_game(acc_value=0, input_dict: dict = {}):
    """
    console game stops if keys of given dictionary is repeated
    """
    keys_travelled = []
    counter = 0
    while counter not in keys_travelled:
        # add counter value to keys_travelled
        keys_travelled.append(counter)

        # add value to acc_value
        # print(acc_value, keys_travelled, input_dict[counter]['op'])
        # update the counter
        if input_dict[counter]['op'] != 'jmp':
            if input_dict[counter]['op'] == 'acc':
                acc_value += int(input_dict[counter]['value'])
            counter += 1
        else:
            counter = counter + int(input_dict[counter]['value'])
    return acc_value


def loop_through(acc_value=0, input_dict:dict={}):
    keys_travelled = []
    counter = 0
    final_counter = max(input_dict.keys())
    is_not_infinite_loop = False

    while True:
        if counter in keys_travelled:
            # print("infinite loop occured")
            break
        else:
            keys_travelled.append(counter)
            # print(counter, acc_value, input_dict[counter]['op'])
            if input_dict[counter]['op'] != 'jmp':
                if input_dict[counter]['op'] == 'acc':
                    acc_value += int(input_dict[counter]['value'])
                counter += 1
            else:
                counter = counter + int(input_dict[counter]['value'])
        if counter > final_counter:
            is_not_infinite_loop = True
            # print(is_not_infinite_loop)
            break
        # print(keys_travelled)

    if is_not_infinite_loop:
        return acc_value
    else:
        return False
     


def console_game_part2(input_dict: dict = {}):
    """
    take into account all the jmp in the given input_dict
    # prepare jmp dictionary
    # loop through every jmp key and change the jmp key to nop and validate
    # if infinite loop occurs break from the loop
    # if last statement of the input is completed
    # return the acc_value
    """
    jmp_dictionary = {key: value for key, value in input_dict.items() if value['op']=='jmp'}
    # print(jmp_dictionary)

    for key, value in jmp_dictionary.items():
        # deepcopy ensures input_dict is not changed
        changed_dictionary = copy.deepcopy(input_dict)
        changed_dictionary[key]['op'] = 'nop'

        # print(changed_dictionary)
        value = loop_through(0, changed_dictionary)
        if value is not False:
            return value
        

