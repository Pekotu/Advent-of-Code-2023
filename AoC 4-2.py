#f=open('testinput.txt', 'r') #for test
f=open('input.txt', 'r')
cards = f.readlines()
f.close
count_of_card = len(cards)
number_of_cards = [0]

for i in range(count_of_card):
    number_of_cards.append(1)

winning_no = []
my_no=[]
result = 0

def calculate_cards(card, number_of_pairs):
    for repeat in range(number_of_cards[card]):
        for i in range(number_of_pairs):
            number_of_cards[card+i+1] += 1 
    return

#------------main code--------------------------
for r, row in enumerate(cards):
   
    #winning_no = row[8:22].split() #for test: 
    winning_no = row[10:39].split() #final
    #print(winning_no)
    
    #my_no = row[25:-1].split() #for test
    my_no = row[42:-1].split() #final
    #print(my_no)
    number_of_pairs=0
    
    for number in winning_no:
        if number in my_no:
            number_of_pairs += 1 

    calculate_cards(r+1, number_of_pairs)            

for i in range(len(number_of_cards)):
    result += number_of_cards[i]

print(f'{result=}')
