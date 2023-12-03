f=open('input.txt','r')
result = 0

colors = ['red', 'green', 'blue']
max_colors = [0, 0, 0]
    
for r, row in enumerate(f): #in each row of file
    row_backup = row
    for c, color in enumerate(colors): #for each color
        row = row_backup
        while row.find(color) != -1: #while color is in row
            pos= row.find(color) #find color position in row
            color_number = int(row[pos-3:pos-1].strip()) #get number which is in front of color
            
            if color_number>max_colors[c]: #if color_number is > then max_color then replace max_colors
                max_colors[c]=color_number

            row = row[pos+1:len(row)] #cut row from color to the end of row
    
    result += max_colors[0]*max_colors[1]*max_colors[2] #get max color number
    max_colors=[0,0,0] #reset max color number

f.close()
print(f'{result=}')
