f=open('input.txt','r')
result = 0
wrong_games =[] 
max_numbers_of_colors = [12, 13, 14]
colors = ['red', 'green', 'blue']
#write all
for c, color in enumerate(colors): #for each color
    max_value = max_numbers_of_colors[c]
    
    f.seek(0) #go to the beginning of file
    for r, row in enumerate(f): #in each row of file
        #print(f'{r=}, {row=}')    
        while row.find(color) != -1:
           # print(row)
            pos= row.find(color)   #find color
            color_number = int(row[pos-3:pos-1].strip()) #get number which is in front of color
            row = row[pos+1:len(row)]

            if color_number > max_value: #if number is bigger than max number append game number to wrong_games
                wrong_games.append(r+1)
               
f.close() 

wrong_games = set(wrong_games) #remove duplicates


for i in range(1,r+1): #sum of rows/games which are not in wrong_games
    if i not in wrong_games:
        result += int(i)
        
print(f'number of rows:{r}')
print(f'{result=}')

