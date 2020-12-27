f = open("input.txt", "r")
complements = {int(s):2020-int(s) for s in f.read().split()}
for k,v in complements.items():
    if v in complements:
        print("The answer is: " + str(k*v)
#PART TWO
f = open("input.txt", "r")
complements = {int(s):2020-int(s) for s in f.read().split()}
for k,v in complements.items():
    complements_2 = {v - k: k for k in complements.keys()}
    if '0' in complements_2:
        k_2 = complements_2['0']
        print("The answer is " + str(k*v*k_2)
