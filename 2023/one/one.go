package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strings"
	"strconv"
	"fmt"
)


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

func ProblemOnePart1() int {
	lines, err := ReadInput("inputs/one.txt")
	if err != nil {
		log.Fatalf("ReadInput: %s", err)
	}
	var sum int
	for _, line := range lines {
		re := regexp.MustCompile("[0-9]+")
		numbers := re.FindAllString(line,-1)
		number := strings.Join(numbers[:], "")
		n := string(number[0]) + string(number[len(number)-1])
		i, _ := strconv.Atoi(n)
		sum += i
	}
	return sum
}

func ProblemOnePart2() int {
	numberMap := make(map[string]string)
	numberMap["one"] = "o1e"
	numberMap["two"] = "t2o"
	numberMap["three"] = "th3ee"
	numberMap["four"] = "f4ur"
	numberMap["five"] = "f5ve"
	numberMap["six"] = "s6x"
	numberMap["seven"] = "se7en"
	numberMap["eight"] = "ei8ht"
	numberMap["nine"] = "n9ne"
	numberMap["zero"] = "z0ro"
	lines, err := ReadInput("inputs/one.txt")
	if err != nil {
		log.Fatalf("ReadInput: %s", err)
	}
	var sum int
	for _, line := range lines {
		for i, j := range numberMap {
			var newLine string
			if strings.Contains(line, i) {
				newLine = strings.Replace(line, i, j, -1)
			    line = newLine
			}
		}
		re := regexp.MustCompile("[0-9]+")
		numbers := re.FindAllString(line,-1)
		number := strings.Join(numbers[:], "")
		n := string(number[0]) + string(number[len(number)-1])
		i, _ := strconv.Atoi(n)
		sum += i
	}
	return sum
}

func main() {
	fmt.Println(ProblemOnePart2())
}
