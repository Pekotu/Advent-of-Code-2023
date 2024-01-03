import numpy as np
import time
import copy
#--------------------------------------

def rotate_arr(arr):
    return np.rot90(arr, k=-1)
#--------------------------------------

def get_free_space(arr):
    global free_spaces, sides_rows_columns
    for side in range(4):
        #print(arr)
        rows, columns = np.shape(arr)
        sides_rows_columns.append((rows, columns))
        for c, col in enumerate(arr.T):
            #print(col)
            start=0
            end=0
            count=0
            col_list=[]
            for r, val in enumerate(col):
                
                if val != '#' and r<rows-1:
                    if count==0: start=r
                    count+=1
                
                elif val=='#':
                    if count>0: 
                        if r == rows-1: 
                            end=r+1
                        else:
                            end=r        
                        count=0
                        col_list.append((start, end))
                
                elif r==rows-1:
                    if count==0: start=r; end=r+1
                    else: end=r+1

                    col_list.append((start, end))
            
            free_spaces[side].append(col_list)
            #print(col_list)
        arr = rotate_arr(arr)
    
#--------------------------------------


def set_start_end(col, s, e):
    if s==e==0:
        e=col.tolist().find('#')
        if e==-1: e=rows
        
    else:
        s=e+1
        e=col.tolist()
#--------------------------------------

def stones_load(arr):
    
    result_sum =0
    result = 0
    rows, columns = arr.shape
    for r in range(rows):
        result= np.count_nonzero(arr[r,:]=="O")*(rows-r)
        result_sum += result
        #print(arr[r,:], result)
    #print(result_sum)
    return result_sum    

#-----------------------------------------
def find_same_result(arr, results):
    for i in range(len(results)-1,0,-1):
        
        if np.array_equal(results[i],arr):
            return i
    return -1

#--------main---------------------
with open('input.txt','r') as f:
    input = f.read().split('\n')

input_list=[]
for r in input:
    r_list = [c for c in r]
    input_list.append(r_list)

arr = np.array(input_list)


free_spaces=[[],[],[],[]]
sides_rows_columns=[]
result_no = 0
results=[]
time_rotate, time_data2, time_data, time_data2, time_sort=0,0,0,0,0
flag = False
get_free_space(arr)

cycles = 1000000000
for cycle in range(cycles):
#------------------------------------------------------
    if flag: break
    for side in range(4):
        if flag: break
        
        rows, columns = sides_rows_columns[side]
      
        for c in range(columns):
            if flag: break
            #print(arr[:,c])
            for start, end in free_spaces[side][c]:
                if (np.where(arr[:,c][start:end]=='O'))[0].size != 0: 
                   
                    arr[:,c][start:end] = np.sort(arr[:,c][start:end])[::-1]
                       
        if side==3:             
            arr=rotate_arr(arr)
            print(arr)
            if cycle > 0: 
                first_result = find_same_result(arr, results)
                if first_result > -1:
                    lop=cycle-first_result

                    cycles_of_lop=(cycles-first_result)//lop    
                    last_lop = first_result + cycles_of_lop* lop
                    additional_cycles = cycles-last_lop
                    final_result= results[first_result+additional_cycles-1]    
                    final_load = stones_load(final_result)
                    flag = True
                    break    
            
            results.append(copy.deepcopy(arr))
            final_load = stones_load(arr)
            
            print(f'{cycle=} {side=} {final_load=}')
            print('----------------- \n')
        else:
            arr=rotate_arr(arr)
            
        
print(arr, '\n')
print(f'{final_load=}')