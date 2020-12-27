import numpy as np

MOVEMENT = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def readSits(file):
    lines_of_sits = [list(line.rstrip()) for line in f.readlines()]
    sits = np.array(lines_of_sits,dtype=object)
    return sits

def checkCurrentState(sits,row,sit):
    back = True if row - 1 >= 0 else False
    left = True if sit - 1 >= 0 else False
    right = True if sit + 1 <= len(sits[0]) - 1 else False
    front = True if row + 1 <= len(sits) -1 else False

    contiguous_sits_state = np.array([[[back,left],[back,back],[back,right]],[[left,left],
        [False,False],[right,right]],[[front,left],[front,front],[front,right]]])

    occupied_sits = 0
    row_sit = row - 1
    column_sit = sit - 1

    for cont_row in contiguous_sits_state:
        for cont_sit in cont_row:
            if cont_sit[0] and cont_sit[1]:
                if sits[row_sit][column_sit] == '#':
                    occupied_sits += 1
            column_sit += 1

        column_sit = sit - 1
        row_sit += 1

    return occupied_sits

def checkCurrentState2(sits,row,sit):
    global MOVEMENT
    vertical = [0,len(sits)-1]
    horizontal = [0,len(sits[0])-1]
    occupied_sits = 0
    occupied = False
    for i in range(8):
        next_row = row + MOVEMENT[i][0]
        next_col = sit + MOVEMENT[i][1]
        while (next_row >= vertical[0] and next_row <= vertical[1] and next_col >= horizontal[0] and next_col <= horizontal[1]) and not occupied:
            if sits[next_row][next_col] == "#":
                occupied_sits += 1
                occupied = True
            elif sits[next_row][next_col] == "L":
                occupied = True
            else:
                next_row += MOVEMENT[i][0]
                next_col += MOVEMENT[i][1]
        occupied = False
    return occupied_sits

def predictSitMovements(sits):
    change = True
    count_occupied = 0
    rounds = 0
    while change:
        count_occupied = 0
        change = False
        current_state_sits = sits.copy()
        for row in range(len(sits)):
            for sit in range(len(sits[0])):
                if sits[row][sit] != '.':
                    occupied_sits = checkCurrentState2(current_state_sits,row,sit)
                    if occupied_sits >= 5 and sits[row][sit] == '#':
                        sits[row][sit] = 'L'
                        change = True
                    elif occupied_sits == 0 and sits[row][sit] == 'L':
                        sits[row][sit] = '#'
                        change = True
                if sits[row][sit] == '#':
                    count_occupied += 1
        rounds+=1
    return count_occupied

f = open("input.txt","r")

sits = readSits(f)

occupied_sits = predictSitMovements(sits)

print("Question {1,2}: " + str(occupied_sits))