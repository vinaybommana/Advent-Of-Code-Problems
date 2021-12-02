package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func problem2(input_data []string) int {
	aim := 0
	hz_position := 0
	depth := 0
	for _, item := range input_data {
		values := strings.Split(item, " ")
		if len(values) > 1 {
			// fmt.Println(values)
			flag, value := values[0], values[1]
			v, err := strconv.Atoi(value)
			if err != nil {
				fmt.Println("Error converting value to int")
			}
			if flag == "forward" {
				hz_position += v // first instruction
				depth += aim * v
			} else if flag == "down" {
				aim += v
			} else if flag == "up" {
				aim -= v
			}
			// fmt.Println(values, hz_position, aim, depth)
		}
	}
	return depth * hz_position
}

func main() {
	data, err := ioutil.ReadFile("../../inputs/input2.txt")
	if err != nil {
		fmt.Println("Error reading input data")
	}
	input_data := strings.Split(string(data), "\n")
	fmt.Println(problem2(input_data))
}
