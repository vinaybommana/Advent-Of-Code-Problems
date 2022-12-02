package main

import (
	_ "embed"
	"fmt"
	"strings"
)

var (
	//go:embed day2.txt
	data []byte
)


var OpponentsMemo = map[string]string{"A": "Rock", "B": "Paper", "C": "Scissors"}
var ScoreMemo = map[string]int{"Rock": 1, "Paper": 2, "Scissors": 3}
var FirstPartUserMemo = map[string]string{"X": "Rock", "Y": "Paper", "Z": "Scissors"}
var ResultMemo = map[string]int{"W": 6, "L": 0, "D": 3}
var SecondPartStrategy = map[string]string{"X": "L", "Y": "D", "Z": "W"}


// part 1
func GiveResult(opponentHand string, userHand string) string {
	if OpponentsMemo[opponentHand] == FirstPartUserMemo[userHand] {
		return "D"
	} else {
		if OpponentsMemo[opponentHand] == "Rock" {
			if FirstPartUserMemo[userHand] == "Paper" {
				return "W"
			} else {
				return "L"
			}
		}
		if OpponentsMemo[opponentHand] == "Paper" {
			if FirstPartUserMemo[userHand] == "Scissors" {
				return "W"
			} else {
				return "L"
			}
		}
		if OpponentsMemo[opponentHand] == "Scissors" {
			if FirstPartUserMemo[userHand] == "Rock" {
				return "W"
			} else {
				return "L"
			}
		}
	}
	return ""
}


// return the hand User should play based on strategy
func GiveHand(opponentHand string, strategy string) string {
	if strategy == "D" {
		return OpponentsMemo[opponentHand]
	} else {
		if OpponentsMemo[opponentHand] == "Rock" {
			if strategy == "W" {
				return "Paper"
			} else {  // only option is "L"
				return "Scissors"
			}
		}
		if OpponentsMemo[opponentHand] == "Paper" {
			if strategy == "W" {
				return "Scissors"
			} else {  // only option is "L"
				return "Rock"
			}
		}
		if OpponentsMemo[opponentHand] == "Scissors" {
			if strategy == "W" {
				return "Rock"
			} else {  // only option is "L"
				return "Paper"
			}
		}
	}
	return ""
}

func main() {
	inputData := string(data)
	inputDataSlice := strings.Split(inputData, "\n")
	var totalScore int
	// fmt.Println(len(inputDataSlice))
	for _, i := range inputDataSlice {
		output := strings.Split(i, " ")
		if len(output) == 2 {
			opponentChoice, userChoice := output[0], output[1]
			result := GiveResult(opponentChoice, userChoice)
			totalScore += ResultMemo[result]
			userHand := FirstPartUserMemo[userChoice]
			totalScore += ScoreMemo[userHand]
		}
	}
	fmt.Printf("First Part: %d\n", totalScore)

	// Part 2
	totalScore = 0
	for _, i := range inputDataSlice {
		output := strings.Split(i, " ")
		if len(output) == 2 {
			opponentChoice, userChoice := output[0], output[1]
			strategy := SecondPartStrategy[userChoice]
			totalScore += ResultMemo[strategy]
			userHand := GiveHand(opponentChoice, strategy)
			totalScore += ScoreMemo[userHand]
		}
	}
	fmt.Printf("Second Part: %d\n", totalScore)
}
