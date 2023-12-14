with open('input.txt','r') as f:
    input_list = f.read().split('\n')


def cal_dif():
    dif=()
    for i in range(0,len(changes[-1])-1):
        dif+= (changes[-1][i+1] - changes[-1][i],)
    changes.append(dif)               
    return

def test_0_changes():
    for val in changes[-1]:
        if val:
            return True
    return False     

def get_new_value():
    new_val = 0
    for i in reversed(range(len(changes)-1)):
       new_val = changes[i][-1] + new_val
    return new_val



#--------main code
changes=[]
result=0
for line in input_list:
    changes=[]    
    changes.append(tuple(map(int, line.split(" "))))
    
    while changes==[] or test_0_changes():
        cal_dif()

    result += get_new_value()


print(result)
