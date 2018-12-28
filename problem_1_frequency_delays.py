# problem one


def get_lines_from_input_file(filename):
    rows = []
    with open(filename) as f:
        for line in f:
            rows.append(line)

    return rows


def find_answers(rows):
    answer = 0
    for element in rows:
        operator = element[0]
        value = element[1:]
        if operator == "+":
            answer += int(value)
        elif operator == "-":
            answer -= int(value)
        else:
            print(operator, value)
    return answer


def main():
    print(find_answers(get_lines_from_input_file('input_1.txt')))


if __name__ == "__main__":
    main()
