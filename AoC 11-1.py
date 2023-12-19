with open('input.txt', 'r') as f:
    input = f.read().splitlines()


#double empty rows
extended=[]
for row in input:
    if '#' in row:
        extended.append(row)
    else:
        extended.append(row)
        extended.append(row)
input = extended.copy()

extended=[]
for r in range(len(input)): 
    extended += '',

#double empty columns
for c in range(len(input[0])):
    empty=True
    for row in input:
        if row[c] =='#': empty=False
    
    if empty: 
        for r, row in enumerate(input):
            extended[r] += row[c]+row[c]
    else:
        for r, row in enumerate(input):
            extended[r] += row[c]
print(f'{len(extended)=}')
print(f'{len(extended[0])=}')


renamed=[]
for r in range(len(extended)): 
    renamed += '',

counter=1
distances=[]
galaxy=1
#naming of galaxy
for r, row in enumerate(extended):
    new_row=""
    for c, val in enumerate(row):
        if val == '#':
            new_row += str(counter)
            distances.insert(counter, (r, c)) #galaxy position
            counter+=1
        else:
            new_row += val
    renamed[r] = new_row
"""
#create list of distances
for r, row in enumerate(extended):
    while str(galaxy) in row:
        distances.insert(galaxy, (r, row.find(str(galaxy))))
        galaxy+=1
"""        
result=0
#calculate distances
for g1, galaxy1 in enumerate(distances):
    x1, y1 = galaxy1
    for galn in range(g1+1, len(distances)):
        xn, yn =distances[galn]
        x=abs(x1-xn)
        y=abs(y1-yn)
        distance = x+y
        result += distance

        
print(result)



