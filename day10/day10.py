def countJoltDifferences(numbers,jolt_differences):
    for i in range(len(numbers)-1):
        jolt_differences[str(numbers[i+1] - numbers[i])] += 1
    jolt_differences['3'] += 1
    return jolt_differences

def countAdaptersCombinations(numbers,index,total_combinations,saved_combinations):
    if len(numbers)-1 <= index:
        return total_combinations+1
    else:
        shift = 1
        if index not in saved_combinations:
            saved_combinations[index] = 0

        while (numbers[index+shift] - numbers[index]) <= 3:
            if (index+shift) in saved_combinations:
                total_combinations += saved_combinations[index+shift]
            else:
                total_combinations = countAdaptersCombinations(numbers,index+shift,total_combinations,saved_combinations)
            shift+=1
            if (index+shift) >= len(numbers):
                break
        
        saved_combinations[index] += total_combinations 

    return total_combinations

f = open("input.txt", "r")
numbers = [int(line) for line in f.readlines()]
numbers.append(0)
numbers = sorted(numbers)
jolt_differences = {'1':0,'2':0,'3':0}

jolt_differences = countJoltDifferences(numbers,jolt_differences)
combinations = countAdaptersCombinations(numbers,0,0,{})

print("First question: " + str(jolt_differences['1'] * jolt_differences['3']))
print("Second question: " + str(combinations))