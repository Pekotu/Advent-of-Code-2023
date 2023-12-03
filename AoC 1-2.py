in_file = open("input1.txt", "r")

result = 0
cisla1 = ('one','two','three','four','five','six','seven','eight','nine')
cisla2=('1','2','3','4','5','6','7','8','9')

for r in in_file:
    index_of_first=9999999
    first=None
    index_of_last = -1
    last=None
    row_no = None
    
#find first and last digit
    for cisla in (cisla1,cisla2):
        for i, cislo in enumerate(cisla):
            index = r.find(cislo)
            #first
            if -1 < index < index_of_first:
                first=i+1
                index_of_first = index
            
            #last
            index = r.rfind(cislo)
            if index > index_of_last:
                last = i+1
                index_of_last = index

#put first and last together to get row number
    row_no =str(first)+str(last)
    
#add row number to result 
    result += int(row_no)  
    print(result)

in_file.close() 

print(f'result={result}')