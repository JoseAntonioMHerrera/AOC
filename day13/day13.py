import functools
import operator

def readSteps(f):
    lines = f.readlines()
    prediction = int(lines.pop(0))
    buses = lines[0].split(',')
    shift_timestamps = []
    timestamps = []
    index=0
    for bus in buses:
        if bus != 'x':
            shift_timestamps.append([int(bus),index])
            timestamps.append(int(bus))
        index+=1
    return [prediction,timestamps,shift_timestamps]

def getInverses(Ni,modulus,remainders):
    inverses = []
    for i in range(len(Ni)):
        scalar = 1
        while int(Ni[i]*scalar % modulus[i]) != 1:
            scalar+=1
        inverses.append(scalar)

    return inverses

def getFirstTimestamp(timestamps):
    modulus = [ts[0] for ts in timestamps]
    remainders = [(timestamps[i][0] - timestamps[i][1])%timestamps[i][0] for i in range(len(timestamps))]
    N = functools.reduce(operator.mul, modulus)
    Ni = [functools.reduce(operator.mul, set(modulus) - set([current_modulus])) for current_modulus in modulus]
    inverses = getInverses(Ni,modulus,remainders)
    mult_Ni_inverses_remainders = [inverses[i]*Ni[i]*remainders[i] for i in range(len(Ni))]
    solution = sum(mult_Ni_inverses_remainders) % N
    return solution
                
                    
def getFirstBus(prediction,timestamps):
    found = -1
    scalar = 2
    timestamps = sorted(timestamps)
    while found < 0:
        for ts in timestamps:
            next_ts = ts*scalar
            if (next_ts - prediction) > 0:
                found = (next_ts - prediction)*ts
                break
        scalar+=1
    return found


f = open("input.txt","r")

data = readSteps(f)
firstBus = getFirstBus(data[0],data[1])
firstTimestamp = getFirstTimestamp(data[2])

print("Question 1: " + str(firstBus))
print("Question 2: " + str(firstTimestamp))