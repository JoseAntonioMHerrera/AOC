def actionParser(line):
    command =  line.split(' ')
    action = command[0]
    value = int(command[1][1:])  if  command[1][:1] == '+' else int(command[1][1:]) * -1
    return {'action':action,'value':value}

def executeGame(commands,action_index,accumulator_value,executed_actions):
    if action_index >= len(commands):
        return {'end':True,'accumulator':accumulator_value}
    elif action_index in executed_actions:
        return {'end':False,'accumulator':accumulator_value}
    else:
        executed_actions[action_index] = str(commands[action_index]['action']) + " " + str(commands[action_index]['value'])
        if commands[action_index]['action'] == 'acc':
            accumulator_value += commands[action_index]['value']
            action_index+=1
        elif commands[action_index]['action'] == 'jmp':
            action_index += commands[action_index]['value']
        else:
            action_index+=1
        return executeGame(commands,action_index,accumulator_value,executed_actions)

def findTheLoop(commands,action_index,executed_actions,last_index,first_index):  
    if action_index in executed_actions:
        return {'first':first_index, 'last':last_index}
    else:
        executed_actions[action_index] = str(commands[action_index]['action']) + " " + str(commands[action_index]['value'])
        if commands[action_index]['action'] == 'jmp':
            action_index += commands[action_index]['value']
            if commands[action_index]['value'] > 0:
                if action_index > last_index:
                    last_index = action_index
            else:
                if action_index < first_index:
                    first_index = action_index
        else:
            action_index+=1
        
        if action_index > last_index:
            last_index = action_index

        return findTheLoop(commands,action_index,executed_actions,last_index,first_index)

f = open("input.txt", "r")
commands = []
for line in f.readlines():
    commands.append(actionParser(line))

accumulator_value = executeGame(commands,0,0,{})
accumulator_at_the_end = 0
index = findTheLoop(commands,0,{},0,10000)

save_action = ""
for i in range(index['first'],index['last']+1,1):
    if commands[i]['action'] == "jmp":
        commands[i]['action'] = "nop"
        save_action = "jmp"
    elif commands[i]['action'] == "nop":
        commands[i]['action'] = "jmp"
        save_action = "nop"
    if save_action !=  "":
        endGame = executeGame(commands,0,0,{})
        if(endGame['end'] == True):
            accumulator_at_the_end = endGame['accumulator']
            break
        commands[i]['action'] = save_action
        save_action = ""

print("Accumulator value part 1: " + str(accumulator_value['accumulator']))
print("Accumulator value part 2: " + str(accumulator_at_the_end))