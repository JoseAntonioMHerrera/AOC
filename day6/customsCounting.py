f = open("input.txt", "r")
lines = f.readlines()
print(len(lines))
sumOfYes = 0
groupChoices = ""
for line in lines:
	if(line[0] == '\n'):
		sumOfYes += len(set(groupChoices))
		groupChoices = ""
	else:
		groupChoices+= line.strip('\n')

print("The number of Yes are: " + str(sumOfYes))


sumOfConsensusYes = 0
listOfYes = []

for line in lines:
	if(line[0] == '\n'):
		sumOfConsensusYes += len(set.intersection(*listOfYes))
		listOfYes = []
	else:
		listOfYes.append(set(line.strip('\n')))

print("The number of comun answers are: " + str(sumOfConsensusYes))