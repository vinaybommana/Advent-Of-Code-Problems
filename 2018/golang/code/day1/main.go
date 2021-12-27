package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

func problem1(inputData []string) int {
	var outputValue int

	for _, item := range inputData {
		v, err := strconv.Atoi(item)
		if err != nil {
			log.Fatal("Error converting inputData item to int")
		}
		outputValue += v
	}
	return outputValue
}

func problem2(inputData []string) int {
	var outputValue int
	i := 0
	while true {
		if i >= len(inputData) {
			i = 0
		}
		
	}
	return outputValue
}

func init() {
	log.SetOutput(os.Stdout)
}

func main() {
	data, err := ioutil.ReadFile("../../inputs/input1.txt")
	if err != nil {
		log.Fatal("Error reading input data")
	}
	inputData := strings.Split(string(data), "\n")

	fmt.Println(problem1(inputData))
}
