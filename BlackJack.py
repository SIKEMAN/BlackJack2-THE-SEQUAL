#BlackJack

import random


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


def compDealOneCard():
    computerhand.append(deck[0])
    del deck[0]

def getCardValue(card):
    if card[1:2]== 'Q' or  card[1:2]== 'K' or  card[1:2]== 'J' or  card[1:2]== '1':
         return(10)
    elif card[1:2] == 'A':
         return (11)
    else:
         return int(card[1:2])

def computerLogic(deck,compCardTotal):
    if compCardTotal < 17:
        computerhand.append(deck[0])
        del deck[0]
    else:
        return stand


# Main Program
playAgain = 'y'
while playAgain == 'y':
    
    print('Welcome to BlackJack.')
    playerStand = False
    playerBust = False
    computerStand = False
    computerBust = False
    random.shuffle(deck)
    playerhand=[]
    computerhand=[]
    cardTotal= (0)
    compCardTotal = (0)
    aceCount = (0)
    dealTwoCards()
    dealTwoCardsComp()


    for thisCard in playerhand:
        cardTotal = cardTotal + getCardValue(thisCard)
    print(cardTotal)

    while playerBust == False:
        print('hit or stand?')
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
                        aceCount = aceCount + 1
               while aceCount > 0:
                   cardTotal = cardTotal - (10)
                   aceCount = aceCount - (1)
                   print(cardTotal)
               
                   if cardTotal <= (21):                  
                       break
            if cardTotal > (21):
                playerBust = True
                print('You busted!')
                print('Computer wins!')
                break
        else:
            playerStand = True
            break

    #Computer Turn

    for thatCard in computerhand:
        compCardTotal = compCardTotal + getCardValue(thatCard)


    if compCardTotal > (21):
        aceCount = (0)
        for card in computerhand:
            if 'A' in card:
                aceCount = aceCount + 1
        while aceCount > 0:
            compCardTotal = compCardTotal - (10)
            aceCount = aceCount - (1)
            if compCardTotal <= (21):
                print('Subtracting aces')
                print(computerhand)
                print(compCardTotal)
                break



    while computerBust == False:
        if playerBust == True:
            break

        print()       
        print('Computer turn...')
        print(computerhand)
        print(compCardTotal)
        if compCardTotal < (17):
            print('Computer takes a card.')
            compDealOneCard()
            print(computerhand)
            compCardTotal = (0)
            for thatCard in computerhand:    # Count with Aces = 11
                compCardTotal = compCardTotal + getCardValue(thatCard)                    
            #print('Total before Aces ' + str(compCardTotal))
            if compCardTotal > (21):
                aceCount = (0)
                for card in computerhand:
                    if 'A' in card:
                        aceCount = aceCount + 1
                while aceCount > 0:
                    compCardTotal = compCardTotal - (10)
                    aceCount = aceCount - (1)
                    if compCardTotal <= (21):
                        #print(computerhand)
                        #print(compCardTotal)
                        break

            if compCardTotal > (21):
                computerBust = True
                print()
                print('Computer busted!')
                print('Computer had ' + str(compCardTotal))
                print()
                print('You win!')
                break
            

        else:
            print('Computer Stood!')
            print(computerhand)
            computerStand = True
            break

    if playerStand == True and computerStand == True:
        if (cardTotal) == (compCardTotal):
            print('You tied with the computer.')

        elif (cardTotal) < (compCardTotal):
            print('Computer won!')
                
        else:
            print()
            print('YOU WIN!!!')
            
    print()
    print('Play again? (y/n)')
    playAgain = input()
    




    
    
    
