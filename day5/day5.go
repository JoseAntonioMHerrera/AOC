package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open(`C:\Users\ImpII\Desktop\day5\input.txt`)
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	var lowerHalfRow = 0
	var upperHalfRow = 127
	var lowerHalfColumn = 0
	var upperHalfColumn = 7
	var lastRowLetter = ' '
	var lastColumnLetter = ' '
	var row = 0
	var column = 0
	var currentID = 0
	var currentHighestID = 0
	var currentLowestID = 1000
	var sumOfSitsID = 0
	var numberOfSits = 0

	for scanner.Scan() {
		numberOfSits++nj
		var sitID = []rune(scanner.Text())
		for i := 0; i < len(sitID); i++ {
			switch sitID[i] {
			case 'F':
				upperHalfRow = upperHalfRow - ((upperHalfRow - lowerHalfRow) / 2) - 1
				lastRowLetter = 'F'
			case 'B':
				lowerHalfRow = lowerHalfRow + ((upperHalfRow - lowerHalfRow) / 2) + 1
				lastRowLetter = 'B'
			case 'R':
				lowerHalfColumn = lowerHalfColumn + ((upperHalfColumn - lowerHalfColumn) / 2) + 1
				lastColumnLetter = 'R'
			case 'L':
				upperHalfColumn = upperHalfColumn - ((upperHalfColumn - lowerHalfColumn) / 2) - 1
				lastColumnLetter = 'L'
			}
		}
		if lastRowLetter == 'F' {
			row = upperHalfRow
		} else {
			row = lowerHalfRow
		}

		if lastColumnLetter == 'R' {
			column = lowerHalfColumn
		} else {
			column = lowerHalfColumn
		}

		currentID = (row*8 + column)

		sumOfSitsID += currentID

		if currentHighestID < currentID {
			currentHighestID = currentID
		}
		if currentLowestID > currentID {
			currentLowestID = currentID
		}
		lowerHalfRow = 0
		upperHalfRow = 127
		lowerHalfColumn = 0
		upperHalfColumn = 7
	}

	var theoreticalSumOfIDSits = (((numberOfSits + 1) * (currentLowestID + currentHighestID)) / 2)
	var differenceActualAndTheoretical = theoreticalSumOfIDSits - sumOfSitsID

	fmt.Println("The highest sit ID is:", currentHighestID)
	fmt.Println("The lowest sit ID is:", currentLowestID)
	fmt.Println("The number of sits are:", numberOfSits)
	fmt.Println("The sum of ID sits is: ", sumOfSitsID)
	fmt.Println("The theoretical sum of ID sits is: ", theoreticalSumOfIDSits)
	fmt.Println("Our ID sit is: ", differenceActualAndTheoretical)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
