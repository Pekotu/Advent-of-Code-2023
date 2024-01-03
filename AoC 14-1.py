import numpy as np

with open('input.txt','r') as f:
    input = f.read().split('\n')

input_list=[]
for r in input:
    r_list = [c for c in r]
    input_list.append(r_list)

arr = np.array(input_list)

rows, columns = np.shape(arr)
results=0

for col in arr.T:
    
    fall=0
    for r, row in enumerate(col):
        if row == '#': fall =0 
        if row == '.': fall+=1
        if row=='O': 
            results += rows-r+fall
    
print(results)
