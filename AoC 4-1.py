#f=open('testinput.txt', 'r')
f=open('input.txt', 'r')

winning_no = []
my_no=[]
result = 0

for row in f:
    card_result=0
    # for test: winning_no = row[8:22].split()
    winning_no = row[10:39].split()
    print(winning_no)
    my_no = row[42:-1].split()
    print(my_no)
    for number in winning_no:
        if number in my_no:
            if card_result==0:
                card_result=1
            else:
                card_result*=2
    result += card_result
print(f'{result=}')
