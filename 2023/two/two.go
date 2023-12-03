package main

import (
	"bufio"
	"log"
	"os"
	"fmt"
	"regexp"
	"strconv"
	"strings"
	// "reflect"
)


type Set struct {
	green int
	red int
	blue int
}

type Game struct {
	number int
	sets []Set
}


func isGameValid(game Game) bool {
	// fmt.Println(game)
	for _, set := range game.sets {
		// 12 red cubes 13 green cubes 14 blue cubes
		if set.red > 12 || set.green > 13 || set.blue > 14 {
			// fmt.Println(set)
			return false
		}
	}
	return true
}

func ReadInput(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, err
}

func ExtractNumber(inputString string) []int {
	re := regexp.MustCompile("[0-9]+")
	matchStrings := re.FindAllString(inputString, -1)
	var returnItems []int
	for _, i := range matchStrings {
		number, err := strconv.Atoi(i)
		if err != nil {
			return nil
		}
		returnItems = append(returnItems, number)
	}
	return returnItems
}


func ParseGameDS(line string) Game {
	var game Game
	items := strings.Split(line, ":")
	game.number = ExtractNumber(items[0])[0] // assigning first item because we know only one number will be there
	sets := strings.Split(items[1], ";")
	for _, set := range sets {
		var setVariable Set
		k := strings.Split(set, ",")
		for _, l := range k {
			if strings.Contains(l, "red") {
				n := ExtractNumber(l)[0]
				setVariable.red = n
			}
			if strings.Contains(l, "green") {
				n := ExtractNumber(l)[0]
				setVariable.green = n
			}
			if strings.Contains(l, "blue") {
				n := ExtractNumber(l)[0]
				setVariable.blue = n
			}
		}
		game.sets = append(game.sets, setVariable)
	}
	return game
}


func GamePower(game Game) int {
	var maxRed, maxGreen, maxBlue int
	for _, set := range game.sets {
		if set.red > maxRed {
			maxRed = set.red
		}
		if set.green > maxGreen {
			maxGreen = set.green
		}
		if set.blue > maxBlue {
			maxBlue = set.blue
		}
	}
	return maxRed * maxGreen * maxBlue
}

func ProblemTwoPart1() int {
	lines, err := ReadInput("inputs/two.txt")
	// lines, err := ReadInput("inputs/sample_two.txt")
	if err != nil {
		log.Fatalf("ReadInput: %s", err)
	}
	// looping through all the input lines
	var sum int
	for _, line := range lines {
		game := ParseGameDS(line)
		if isGameValid(game) {
			// fmt.Println(game.number)
			sum += game.number
		}
	}
	return sum
}


func ProblemTwoPart2() int {
	lines, err := ReadInput("inputs/two.txt")
	// lines, err := ReadInput("inputs/sample_two.txt")
	if err != nil {
		log.Fatalf("ReadInput: %s", err)
	}
	// looping through all the input lines
	var sum int
	for _, line := range lines {
		game := ParseGameDS(line)
		power := GamePower(game)
		sum += power
	}
	return sum
}


func main() {
	// fmt.Println(ProblemTwoPart1())
	fmt.Println(ProblemTwoPart2())
}
