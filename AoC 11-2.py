

def get_gal_position(r,c):
    row_extension=0
    for i in range(r):
        if i in rows_extensions:
            row_extension +=999999
    
    col_extension=0
    for i in range(0,c):
        if i in columns_extensions:
            col_extension +=999999

    return(r+row_extension, c+col_extension)




with open('input.txt', 'r') as f:
    input = f.read().splitlines()

rows_extensions=[]
#double empty rows

for r, row in enumerate(input):
    if not('#') in row:
        rows_extensions.append(r)


columns_extensions=[]

#double empty columns
for c in range(len(input[0])):
    empty=True
    for row in input:
        if row[c] =='#': empty=False
    
    if empty: 
        columns_extensions.append(c)
    

renamed=[]
for r in range(len(input)): 
    renamed += '',

counter=1
gal_positions=[]
galaxy=1
#naming of galaxy
for r, row in enumerate(input):
    new_row=""
    for c, val in enumerate(row):
        if val == '#':
            new_row += str(counter)
            
            gal_positions.insert(counter, get_gal_position(r,c)) #galaxy position
            
            
            counter+=1
        else:
            new_row += val
    renamed[r] = new_row
"""
#create list of distances
for r, row in enumerate(input):
    while str(galaxy) in row:
        distances.insert(galaxy, (r, row.find(str(galaxy))))
        galaxy+=1
"""        
result=0
#calculate distances
for g1, galaxy1 in enumerate(gal_positions):
    x1, y1 = galaxy1
    for galn in range(g1+1, len(gal_positions)):
        xn, yn =gal_positions[galn]
        x=abs(x1-xn)
        y=abs(y1-yn)
        distance = x+y
        result += distance

        
print(result)



