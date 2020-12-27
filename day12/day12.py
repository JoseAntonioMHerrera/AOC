import numpy as np

def readSteps(f):
    steps = [[line[:1],int(line[1:])] for line in f.readlines()]
    return steps

# FIRST PART
def getNewDirection(step,cardinals,turns,current_direction_index):
    number_of_turns = int(step[1] / 90)
    
    new_direction_index = int((current_direction_index + number_of_turns*turns[step[0]]) % len(cardinals))

    return new_direction_index

def executeSteps(steps):
    directions = {'N':['y',1,[0,1]],'E':['x',1,[1,0]],'S':['y',-1,[0,-1]],'W':['x',-1,[-1,0]]}
    cardinals = ['N','E','S','W']
    turns = {'R':1,'L':-1}
    current_direction_index = 1
    start = {'x':0,'y':0}
    for step in steps:
        if step[0] == 'R' or step[0] == 'L':
            current_direction_index = getNewDirection(step,cardinals,turns,current_direction_index)
        elif step[0] == 'F':
            axis = directions[cardinals[current_direction_index]][0]
            sign = directions[cardinals[current_direction_index]][1]
            start[axis] += step[1]*sign
        else:
            start['x'] += step[1]*directions[step[0]][2][0]
            start['y'] += step[1]*directions[step[0]][2][1]
 
    return abs(start['x']) + abs(start['y'])
# ---------------------------------------------
# SECOND PART

def getNewDirection2(step,cardinals,turns,waypoint,directions):
    number_of_turns = int(step[1] / 90)
    if number_of_turns != 0:
        print("Waypoint previo a  giro de " + str(step[1]) +" grados hacia " + step[0] + ": ("+ str(waypoint['x'][0])+ " y "+ str(waypoint['y'][0])+ ")" )
        waypoint['x'][0] = np.remainder((waypoint['x'][0] + number_of_turns*turns[step[0]]),len(cardinals))
        waypoint['y'][0] = np.remainder((waypoint['y'][0] + number_of_turns*turns[step[0]]),len(cardinals))
        if np.remainder(waypoint['x'][0],2) == 0:
            aux_x = waypoint['x'].copy()
            waypoint['x'] = waypoint['y'].copy()
            waypoint['y'] = aux_x
        if (waypoint['x'][1] > 0 and directions[cardinals[waypoint['x'][0]]][1] < 0) or (waypoint['x'][1] < 0 and directions[cardinals[waypoint['x'][0]]][1] > 0):
            if waypoint['x'][1] > 0:
                waypoint['x'][1] *= -1
            else:
                waypoint['x'][1] = abs(waypoint['x'][1])
        if (waypoint['y'][1] > 0 and directions[cardinals[waypoint['y'][0]]][1] < 0) or (waypoint['y'][1] < 0 and directions[cardinals[waypoint['y'][0]]][1] > 0):
            if waypoint['y'][1] > 0:
                waypoint['y'][1] *= -1
            else:
                waypoint['y'][1] = abs(waypoint['y'][1])
        print("Waypoint posterior: ("+ str(waypoint['x'][0])+ " y "+ str(waypoint['y'][0]) )
    return waypoint 

def executeSteps2(steps):
    directions = {'N':['y',1,[0,1]],'E':['x',1,[1,0]],'S':['y',-1,[0,-1]],'W':['x',-1,[-1,0]]}
    cardinals = ['N','E','S','W']
    turns = {'R':1,'L':-1}
    waypoint = {'x':[1,10],'y':[0,1]}
    start = {'x':0,'y':0}
    for step in steps:
        print(step[0])
        if step[0] == 'F':
            start['x'] += waypoint['x'][1]*step[1]
            start['y'] += waypoint['y'][1]*step[1]
        elif step[0] == 'L' or step[0] == 'R':
             waypoint = getNewDirection2(step,cardinals,turns,waypoint,directions)
        else:
            waypoint['x'][1] +=  directions[step[0]][2][0]*step[1]
            waypoint['y'][1] +=  directions[step[0]][2][1]*step[1]
        print("*****************")   
        print(str(start['x']) + "-" + str(start['y']))
        print("---")
        print(str(waypoint['x'][0]) + "-" + str(waypoint['x'][1]))
        print(str(waypoint['y'][0]) + "-" + str(waypoint['y'][1]))
        print("*****************")
    return abs(start['x']) + abs(start['y'])
#------------------------------------------

f = open('input.txt','r')
steps = readSteps(f)

m_distance = executeSteps(steps)
m_distance_2 = executeSteps2(steps)

print("Question 1: " + str(m_distance))
print("Question 2: " + str(m_distance_2))
#101860