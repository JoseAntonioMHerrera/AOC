import sys

def scanPreamble(file,preamble_size):
    preamble = [int(next(file)) for i in range(preamble_size)]
    return preamble
# You can make the contiguous sum along the search of the incorrect value, for each partial sum store it in a dictionary 
# and then
# for the second part just 
def scanTargetNumber(numbers,preamble,preamble_size):
    found = False
    low_index = 0
    high_index = preamble_size

    for nextNumber in numbers:
        for scannedNumber in preamble[low_index:high_index]:
            predecesors = set(preamble[low_index:high_index]) - set([scannedNumber])
            if (int(nextNumber) - int(scannedNumber)) in predecesors:
                preamble.append(int(nextNumber))
                found = True
                break
        if not found:
            return nextNumber
        found = False
        low_index += 1
        high_index += 1
    
    return -1 

def scanContiguousSum(target,numbersArray):
    low_index = 0
    high_index = 0
    lowest_number = sys.maxsize
    highest_number = -1
    sum = 0
    while sum != target:
        sum += numbersArray[high_index]
        high_index += 1
        
        if numbersArray[high_index] < lowest_number:
            lowest_number = numbersArray[high_index]
        
        if numbersArray[high_index] > highest_number:
            highest_number = numbersArray[high_index]
        
        if sum > target:
            low_index += 1
            high_index = low_index
            highest_number = -1
            lowest_number = sys.maxsize
            sum = 0
    
    if sum == target:
        return lowest_number + highest_number
    else:
        return -1

f = open("input.txt", "r")
preamble_size = 25
preamble= scanPreamble(f,preamble_size)
numbers = f.readlines()
target = scanTargetNumber(numbers,preamble,preamble_size)
numbersArray = []
f = open("input.txt", "r")
for line in f.readlines():
    numbersArray.append(int(line))
secondTarget = scanContiguousSum(int(target),numbersArray)

print("Error number part 1: " + str(target))
print("Xmax number part 2: " + str(secondTarget))