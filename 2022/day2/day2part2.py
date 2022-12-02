from day2 import read_input, score_memo, opponents_formula

strategy_guide_memo = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

round_memo = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}


def select_hand(opponent, user):
    strategy = strategy_guide_memo.get(user, "")
    opponents_hand = opponents_formula.get(opponent, "")
    if strategy == "D":
        return opponents_hand
    if strategy == "W":
        # need to win here
        if opponents_hand == "Rock":
            return "Paper"
        if opponents_hand == "Paper":
            return "Scissors"
        if opponents_hand == "Scissors":
            return "Rock"
    if strategy == "L":
        # need to loose
        if opponents_hand == "Rock":
            return "Scissors"
        if opponents_hand == "Scissors":
            return "Paper"
        if opponents_hand == "Paper":
            return "Rock"
    return ""

def give_score(input_data):
    uscore = 0
    for line in input_data:
        opponent, user = line.split(" ")
        uscore += score_memo.get(strategy_guide_memo[user], 0)
        hand = select_hand(opponent, user)
        uscore += round_memo.get(hand, 0)
    return uscore


if __name__ == "__main__":
    input_data = read_input("../inputs/day2.txt")
    print(give_score(input_data))
