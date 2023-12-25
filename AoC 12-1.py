from itertools import product
import re

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

input_data=[]
for row in input:
    input_data.append(row.split(' ')) 

result = 0    

def get_symbols(numbers):
    symbols=['.']
    for number in list(dict.fromkeys(numbers.split(','))):
        symbols.append(int(number)*'#')
        #symbols.append('.' + (int(number)*'#'))
    
    return symbols

def numbers_order(str, numbers):
    numbers=numbers.split(',')
    n=0
    ss=0
    for s, sym in enumerate(str):
        if s<=ss and sym=='#': continue

        if sym == '#':
            ss=s
            while ss<len(str) and str[ss] =='#':
                ss+=1
                
            
            if ss - s != int(numbers[n]):
                return False
            
            n+=1
            if n>=len(numbers):    
                return True
            

def test(per, reg_test):

    res = re.search(reg_test, per)
    """
    if res!= None: 
        print(per +" - " + str(res))   
        #
    """
    return res

def test2(per, reg_test, crosses):

    res = re.search(reg_test, per)
    no_cross = per.count('#')
    if res != None and no_cross == crosses:
        print(per +" - ok - " + reg_test)    
        print()
        return True
    return False


for rrr, row in enumerate(input_data):
    print('row-row-row')
    print(str(rrr) + ' - '+ row[0] + ' ' + row[1])
    #symbols=get_symbols(row[1])
    symbols=['.', '#']
    all_per = list(product(symbols, repeat=len(row[0])))
    
    all_per2 = [''.join(per) for per in all_per]

    reg_test1=''
    for s in row[0]:
        if s=='.' or s=='#':
            reg_test1 += '\\'+s 
        
        if s=='?':
            reg_test1 += '[.#]'

    crosses=0
    reg_test2='(^|\\.)'
    for n, num in enumerate(row[1].split(",")):
        #reg_test2 += int(num)*'#'+'{1}' 
        crosses+=int(num)
        reg_test2 += '#{'+ str(num) +'}' 
        if n< len(row): 
            reg_test2 += '\\.+'
        else:
            reg_test2 += '(\\.+|$)'
    
    per_counter=0
    for per in all_per2:
        if test(per, reg_test1):
            
            if test2(per, reg_test2, crosses):    
                per_counter +=1

    result+= per_counter
print(result)