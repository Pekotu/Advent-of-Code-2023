with open("input.txt", 'r') as f:
    input = f.read().split('\n')


def get_box_number(code):
    box_no = 0
    for c in code:
            if c== '-' or c == '=': return box_no
            box_no = (box_no+ord(c))*17%256
    
#--------------------------------------------

def get_label(code):
    if code.find("=") >-1: 
         return code.replace("=", " ")
    else:
         return code[:-1]    

#--------------------------------------------

def add_to_box(box, lable):
    global boxes
    lab= lable[:lable.find(" ")+1]
    l=len(lab)
    for i, lens in enumerate(boxes[box]):
        if lab == lens[:l]:
            boxes[box][i] = lable
            return
    boxes[box].append(lable)
#-----------------------------------------
def remove_from_box(box, lable):
    global boxes
    lable+=" "
    l=len(lable)
    for i, lens in enumerate(boxes[box]):
        if lable == lens[:l]:
            boxes[box].pop(i)
    return

#-----------Main---------------------------------

box_no = 0
boxes=[]
for i in range(256):
    boxes.append([])

for r in input:
    r = r.split(",")
    for code in r:
        
        box = get_box_number(code)
        lable = get_label(code)
        
        if code.find('=')>-1: 
            add_to_box(box, lable)
        
        else: remove_from_box(box, lable)
        
focal_power = 0

for box_no, box in enumerate(boxes):
    for lable_no, lable in enumerate(box):
        focal = int(lable[lable.find(" ")+1:])
        focal_power += ((box_no+1) * (lable_no+1) * focal)
        
        
print(focal_power)
