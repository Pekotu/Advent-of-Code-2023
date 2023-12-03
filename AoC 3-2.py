f = open('input.txt', 'r')
list = f.readlines()
f.close()

result=0
gears_positions = []
gear_position = []


def is_gear(tested_symbol):
    '''test symbol whether is leather except "." '''
    return not(tested_symbol.isdigit()) and tested_symbol != "." and tested_symbol == "*"

def find_number_in_touch_of_sym(r, s, row):   
    '''looking for symbols in touch with symbol sym=list[r][s], if symbol in touch is letter and is not "." return True'''
    for rr in range(r-1,r+1+1): #check rows r-1, r r+1
        if rr < 0 or rr > len(list)-1: continue #skip rows which are out of list

        for ss in range(s-1,s+1+1): #in each row check symbols in positions s-1, s, s+1
            if ss < 0 or ss > len(row)-1: continue #skip symbols which are out of row

            tested_symbol = list[rr][ss]
            if is_gear(tested_symbol):
                gear_position = [rr, ss] 
                return True, gear_position   
    gear_position = []
    return False, gear_position


def find_last_digit_of_number(row,s):
    
    while row[s].isdigit():
        s+=1
        if s > len(row)-1: break
    return s-1

def find_first_digit_of_number(row,s):
    while row[s].isdigit():
        s-=1
        if s < 0: break
    return s+1    

def remove_EOB_in_each_row(list):
    for r, row in enumerate(list):
        row = row[:-1]
        list[r]=row

def calculate_gear_ratio(gears_positions):
    result=0
    for w1, wheel1 in enumerate(gears_positions):
        
        for wheel2 in gears_positions[w1+1:]:
            if wheel1[1] == wheel2[1] and wheel1[2]==wheel2[2]:
                result+= int(wheel1[0])*int(wheel2[0]) 
                break
    return result

#-----Main code-------------------------------------#

remove_EOB_in_each_row(list)

for r, row in enumerate(list):
    last_digit_of_number=-1
    for s, sym in enumerate(row):
        
        if s<= last_digit_of_number: continue #skip symbols wich are part of last all_number  
        
        if sym.isdigit(): 
            result, gear_position = find_number_in_touch_of_sym(r,s, row)
            if result:
                first_digit_of_number = find_first_digit_of_number(row,s)
                last_digit_of_number = find_last_digit_of_number(row,s)
                all_number = row[first_digit_of_number:last_digit_of_number+1]
                gear_position.insert(0, all_number)
                gears_positions.append(gear_position)
                
result = calculate_gear_ratio(gears_positions)
print(f'{result=}')
