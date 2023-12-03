in_file = open("input1.txt", "r")

result = 0

for r in in_file:
 
    print(r)
    first=None
    last=None
    row_no = None

    for i in r:
        je_cislo=i.isdigit()
        if i.isdigit() and first == None:
            first = i
            last = i
        elif i.isdigit():
            last = i 

    row_no =str(first)+str(last)
    print(row_no)
    result += int(row_no)  
    print(result)

in_file.close() 

print(f'result={result}')