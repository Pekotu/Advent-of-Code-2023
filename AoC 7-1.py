import operator 

def load_file(file):
    with open(file, 'r') as f:
        input_list = f.read().splitlines()
    return input_list

def get_list_of_hands(input_list):
    hands =[]
    for row in input_list:
        hands.append(row.split())
    return hands


def get_hands_type_and_strength(hands, cards):
        
    for h, hand in enumerate(hands):
        number_of_cards_in_hand=""
        cards_in_hand = ""
        for c,card in enumerate(hand[0]): #count how much times is each card typ in hand
            hand.append(cards[card])
            
            if hand[0][0:c+1].count(card)==1: 
                number_of_cards_in_hand += str(hand[0].count(card))

        if number_of_cards_in_hand.count("5")==1:#evaluate hand strength
            hand.insert(2,"07")
        
        elif number_of_cards_in_hand.count("4")==1:
            hand.insert(2,"06")
        
        elif number_of_cards_in_hand.count("3")==1 and number_of_cards_in_hand.count("2")==1:
            hand.insert(2,"05")

        elif number_of_cards_in_hand.count("3")==1:
            hand.insert(2,"04")

        elif number_of_cards_in_hand.count("2")==2:
            hand.insert(2,"03")
        
        elif number_of_cards_in_hand.count("2")==1:
            hand.insert(2,"02")

        elif number_of_cards_in_hand.count("1")==5:
            hand.insert(2,"01")

       
    sorted_hand = sorted(hands, key=operator.itemgetter(2,3,4,5,6,7)) #sort hands by hand's strength
    
    return sorted_hand


    
           

def Convert_to_dict(cards):
    dict={}
    cards.reverse()
    for c, card in enumerate(cards):
        dict[card] = str(c+1).zfill(2)
    return dict



#----hlavní kod----------------
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards = Convert_to_dict(cards)

input_list = load_file("input.txt")
hands = get_list_of_hands(input_list)
hands = get_hands_type_and_strength(hands, cards)

result = 0
for h, hand in enumerate(hands):
    #res=h`+1 * int(hand[1])
    result += (h+1) * int(hand[1])

print(result)
