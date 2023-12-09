import numpy

with open('test_input.txt') as f:
    lines = f.read().splitlines()

for l, line in enumerate(lines):
    line = line.split(' ')[1:]
    i=0
    while i< len(line):
        if not line[i].isdigit():
            line.pop(i)
        else:
            i+=1
    
    lines[l] = line

races= tuple(zip(lines[0], lines[1]))

list_wins=[]

for race in races:
   distance = int(race[1])
   time = int(race[0])
   wins=0
      
   for speed in range(1,time):
        if time-speed > distance/speed:
            wins+=1

    list_wins.append(wins)

result=numpy.proud(wins)

print(result)