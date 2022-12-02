# day 2 advent of code
# A - Rock  - X - 1
# B - Paper - Y - 2
# C - Scissors - Z - 3
# win - 6
# lose - 0
# draw - 3


opponents_formula = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}


user_formula = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

score_memo = {
    "W": 6,
    "L": 0,
    "D": 3,
}

user_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def elect(opponent, user):
    # opponent, user = input_line.split(" ")
    opponent_card = opponents_formula.get(opponent, "")
    user_card = user_formula.get(user, "")
    if opponent_card == user_card:
        return "D"
    if user_card == "Rock":
        if opponent_card == "Scissors":
            return "W"
        return "L"
    if user_card == "Scissors":
        if opponent_card == "Paper":
            return "W"
        return "L"
    if user_card == "Paper":
        if opponent_card == "Rock":
            return "W"
        return "L"

def give_winner_score(input_data):
    uscore = 0
    for round in input_data:  # ['OPPONENT USER']
        opponent, user = round.split(" ")
        if user:
            uscore += int(user_score.get(user, 0))
        round_output = elect(opponent, user)
        if round_output:
            uscore += score_memo.get(round_output, 0)
    return uscore


def read_input(filename):
    with open(filename) as o:
        output = o.readlines()
    if output:
        output = [i.strip() for i in output if i]
        return output

if __name__ == "__main__":
    input_data = read_input("../inputs/day2.txt")
    print(give_winner_score(input_data))
