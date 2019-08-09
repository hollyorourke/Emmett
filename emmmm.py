#Emmett game
#There are 6 rounds of 4, 6, 8, 10, 15 and 20 cards each. The aim is to get as few points as possible.
#You may look at two of the cards you are dealt
#On your go you pick up either a card from the deck or the card at the top of the discard pile and choose whether to swap it with one of your cards
#All number cards are worth their value and J,Q,K and joker are worth 10
#Exactly the same card counts as equal
#4 of the same number gives 0 points
#8 of the same number resets your score to 0
#4 jokers gives -20 points
#If all your cards are in order you get 0 points
#In rounds 15 and 20 if you have the cards A-K in order in any position you get 0 points for those cards
#If you want to end the round, knock, then the other 2 players get one more turn

deck0 = ['Ah','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ac','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','As','2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks']

jokers = ['joker1','joker2','joker3','joker4']
deck = deck0 * 8 + jokers
#print(deck)

rounds = [4,6,8,10,15,20]
import random
i = 0
while i < 6:

    number_of_cards = rounds[i]
    print('Round ' + str(i + 1) + ': ' + str(number_of_cards) + ' cards')
        


    #shuffle deck
    random.shuffle(deck)
    print(deck)


    my_dealt_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    dealt_cards_2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    dealt_cards_3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    #deals cards to all players
    n = 0
    while n < number_of_cards:
        my_dealt_cards[n] = deck[n]

        n += 1

    while n < 2*number_of_cards:
        dealt_cards_2[n] = deck[n]

        n += 1

    while n < 3*number_of_cards:
        dealt_cards_3[n] = deck[n]

        n += 1


    #print(my_dealt_cards)
    #print(dealt_cards_2)
    #print(dealt_cards_3)
    print('You may look at 2 cards ')
    m = 0
    card_looked_at = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



    #select two cards to look at
    while m < 2:
        while True:
            card_looked_at[m] = int(input('Pick card 1,..,' +str(number_of_cards) + ' to look at '))
            if card_looked_at[m] in range(1, (number_of_cards + 1)):
                print('Please pick a card in the range')
            else:
                print('Your card is', my_dealt_cards[card_looked_at[m] - 1])
                break
        m += 1

    #start the game
    next_move = input('What is your next move? Type "d" to pick up a card from the deck or "p" to pick up a card from the pile. If you want to knock type "k" .')
    while True:
        if next_move not in ('d','p','k'):
            print('Not a valid answer')
        else:
            break
        
        
    #while next_move != 'k':
        
        
    i += 1

    
