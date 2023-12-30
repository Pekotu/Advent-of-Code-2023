import numpy as np



#--------------------------------------------------


def convert_to_array(data):
    list_char = []
    data = data.split('\n')
    for s, str in enumerate(data):
            sub_list_char = [char for char in str]
            list_char.append(sub_list_char)
            arr = np.array(list_char)
    #print(arr)
    return arr

#--------------------------------------------------

def find_mirror_line(arr,):
    rows = np.shape(arr)[0]
    for col in range(np.shape(arr)[1]):
        #print(arr)
        #print('\n')
        test_arr = np.delete(arr,col,1)
        #print(test_arr)

        for r in range(1,rows):
            row0 = test_arr[r-1,:]
            row1 = test_arr[r,:]
            if np.array_equal(row0, row1):
                flag = check_all_pairs(test_arr,r-1, rows)
                if flag: flag=repair_column(arr, col, r-1, rows)
                if flag: return r 
    return -1        
                    
#--------------------------------------------------                 
def check_all_pairs(arr,m, rows):
    
    for t in range(1,rows):
        down = m-t ; up =  m+t+1
        if down < 0 or up >= rows: return True 
        arr_down = arr[down,:]
        arr_up=arr[up,:]

        arr_comparison = np.array_equal(arr[down,:], arr[up,:])
        #print(arr_comparison)

        if not(np.array_equal(arr[down,:], arr[up,:])):
            return False #it is not complete mirror

#--------------------------------------------------
def repair_column(arr,col,m, rows):
    # if column contain exactly one mirror 
    # difference it correct >>> return True  
    column = arr[:,col]
    
    dif=0
    for i in range(m+1):
        if m-i < 0 or m+1+i == rows: break 
        
        if column[m-i] != column[m+1+i]:
            dif+=1
            if dif > 1: return False
    if dif == 1:
        return True
    else:
        return False
    

#--------------Main------------------------------------
with open('input.txt', "r") as f:
    inputs = f.read().split('\n\n')

results = 0
list_char=[]
for data in inputs:
    arr = convert_to_array(data)    
    
    result = find_mirror_line(arr)
    
    if result ==-1:
            arr = arr.transpose()
            result = find_mirror_line(arr)
            if result > 0: results+=result
            #print(f'{result=}')
    else:
        #print(f'{result*100=}')    
        results+= result*100        
    
    

    print(f'{results=}')
