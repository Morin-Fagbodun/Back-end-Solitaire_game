import cards
import random

def deal_hand():
    game_deck = cards.make_deck()
    single_hand = cards.deal_one_hand(game_deck,4)
    return single_hand
  
def discard(hand,number_of_cards):

    if number_of_cards != 2 or number_of_cards !=4 or number_of_cards<4:
        return hand
    if number_of_cards == 4 or number_of_cards == 2:
       length = len(hand) 
       if number_of_cards >= length:
           return []

    return hand[:length-number_of_cards]  

def play_round(deck,hand):
    while len(deck) < 4:
        cards.draw(deck,hand)
    # print(len(hand))
    if deck != []:
        cards.draw(deck,hand)
        return deck,hand
    while hand < 4:
        card_1 =  hand[0]
        card_2 = hand[1] 
        card_3 = hand[2]
        card_4  = hand[3]
        if card_1[0] == card_4[0]:
            discard(hand,4)
        if card_1[0] != card_4[0] and card_2[1] == card_3[1]:
            hand.pop(card_2,card_3)


def main():
    game_deck = cards.make_deck()
    game_hand = deal_hand()
    # print(len(game_hand))
    
    while game_deck < []:
        play_round(game_deck,game_hand)
    else:
        print("Game Ended", len(game_hand))


    # hand, deck = play_round(hand,deck)


if __name__ == "__main__":
    main()

    