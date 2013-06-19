#BlackJack

import random

###
deck = 'CA C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK DA D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK HA H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK SA S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK'.split()


def dealTwoCards():
    playerhand.append(deck[0])
    playerhand.append(deck[1])
    del deck[0]
    del deck[0]
    print('You hand is...')
    print(playerhand)
    

def dealTwoCardsComp():
    computerhand.append(deck[0])
    computerhand.append(deck[1])
    del deck[0]
    del deck[0]


def hitOrStand():
    choice=''
    hit = ''
    stand = ''
    while not (choice == 'hit' or choice == 'h' or choice == 'stand' or choice == 's'):     
        choice = input().lower()
    if choice == 'hit' or choice == 'h':
        return 'hit'
    else:
        return 'stand'
    
def dealOneCard():
        playerhand.append(deck[0])
        del deck[0]
        print('Your hand is...')
        print(playerhand)

def getCardValue(card):
    if card[1:2]== 'Q' or  card[1:2]== 'K' or  card[1:2]== 'J' or  card[1:2]== '1':
         return(10)
    elif card[1:2] == 'A':
         return (11)
    else:
         return int(card[1:2])

    
print('Welcome to BlackJack.')
playerStand = False
playerBust = False
#random.shuffle(deck)
print(deck)
playerhand=[]
computerhand=[]
cardTotal= (0)
dealTwoCards()
dealTwoCardsComp()
aceCount=(0)
for thisCard in playerhand:
    cardTotal = cardTotal + getCardValue(thisCard)
print(cardTotal)

while True:
    print('HIT or STAND?')
    choice = hitOrStand()
    print('Your choice was ' + choice)
    if choice == 'hit':
        cardTotal= (0)
        dealOneCard()
        for thisCard in playerhand:
            cardTotal = cardTotal + getCardValue(thisCard)
        print(cardTotal)
        if cardTotal > (21):
            for card in playerhand:
                if 'A' in card:
                    aceCount = aceCount + (1)
                    cardTotal = cardTotal - (10)
                    print(cardTotal)
        if cardTotal > (21):
            
            break
    else:
        playerStand = True

        break




    
    
    
