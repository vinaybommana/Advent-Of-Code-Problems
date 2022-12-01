package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// readInput from inputs/day1.txt
func ReadInput(filepath string) string {
	data, err := os.ReadFile(filepath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
	}
	return string(data)
}

func ParseInput(data string) []int {
	// split the string by "\n\n"
	var calorieCount []int
	dataSlice := strings.Split(data, "\n\n")
	for _, elfCalories := range dataSlice {
		calorieSlice := strings.Split(elfCalories, "\n")
		var count int
		for _, calorie := range calorieSlice {
			intCalorie, _ := strconv.Atoi(calorie)
			count += intCalorie
		}
		calorieCount = append(calorieCount, count)
	}
	return calorieCount
}


func main() {
	data := ReadInput("../inputs/day1.txt")
	calorieCount := ParseInput(data)
	// sort.Ints(calorieCount)
    sort.Sort(sort.Reverse(sort.IntSlice(calorieCount)))

	// part 1
	fmt.Printf("First Part: %d\n", calorieCount[0])

	// part 2
	fmt.Printf("Second Part: %d\n", calorieCount[0] + calorieCount[1] + calorieCount[2])
}
