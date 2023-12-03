f = open('input.txt', 'r')
list = f.readlines()
f.close()

def is_letter(tested_symbol):
    '''test symbol whether is leather except "." '''
    return not(tested_symbol.isdigit()) and tested_symbol!= "."


def find_number_in_touch_of_sym(r, s, row):   
    '''looking for symbols in touch with symbol sym=list[r][s], if symbol in touch is letter and is not "." return True'''
    for rr in range(r-1,r+1+1): #check rows r-1, r r+1
        if rr < 0 or rr > len(list)-1: continue #skip rows which are out of list

        for ss in range(s-1,s+1+1): #in each row check symbols in positions s-1, s, s+1
            if ss < 0 or ss > len(row)-1: continue #skip symbols which are out of row

            tested_symbol = list[rr][ss]
            if is_letter(tested_symbol): 
                return True   
    
    return False


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

#-----Main code-------------------------------------#
result=0

remove_EOB_in_each_row(list)


for r, row in enumerate(list):
    last_digit_of_number=-1
    for s, sym in enumerate(row):
        
        if s<= last_digit_of_number: continue #skip symbols wich are part of last all_number  
        
        if sym.isdigit(): 
            if find_number_in_touch_of_sym(r,s, row):
                first_digit_of_number = find_first_digit_of_number(row,s)
                last_digit_of_number = find_last_digit_of_number(row,s)
                all_number = row[first_digit_of_number:last_digit_of_number+1]

                result+=int(all_number)
                
        
        

print(f'{result=}')