import random

def make_cards(rank,suit):


     card_rank = list(range(2,15))
     card_suit = ("Club", "Diamond", "Heart", "Spade")
    

     name = str(rank) + " of " + str(suit)
     if rank >=10:
        sh = str(rank) + suit[0]
        if rank == 11:
            sh = "J" + suit[0]
            name ="Jack of" + str(suit)
        if rank == 12:
            sh = "Q" + suit[0]
            name ="Queen of" + str(suit)
        if rank == 13:
            sh = "K" + suit[0]
            name ="King of" + str(suit)
        if rank == 14:
            sh = "A" + suit[0]
            name ="Ace of" + str(suit)
     else:
        sh = " " + str(rank) + suit[0]



     if suit == "Heart" or suit == "Diamond":
         return rank,suit,name,'\033[31m'+ sh +'\033[37m'
     if suit == "Club" or suit == "Spade":
        return rank,suit,name,'\033[31m'+sh+'\033[37m'

def make_deck():
     deck =[]
     index = 2 
     while index <=14:
         deck.append(make_cards(index,"Heart"))
         deck.append(make_cards(index,"Diamond"))
         deck.append(make_cards(index,"Club"))
         deck.append(make_cards(index,"Spade"))
         index+=1
     return deck

def shuffle(deck):
   for index in range(len(deck)-1):
       j = random.randint(index,len(deck)-1)
       temp = deck[index]
       deck[index] = deck[j]
       deck[j] = temp 

def draw(deck,hand):
    if len(deck) == 0:
        return None
    else:
        drawn = deck[0]
        hand.append(deck.pop(0))
        return drawn

def deal_one_hand(deck,number):
    hand = []
    # for _ in range(number):
    #     draw(deck,hand)
    # # hand = 
    # hand = [range(number(draw(deck,hand)))]

    return [draw(deck,hand) for _ in range(number)]
    

def main():
    rank,suit,name,sh = make_cards(7,"Heart")
    print(sh)
    game_deck = make_deck()
    print(len(game_deck))
    game_hand = deal_one_hand(game_deck,4)
    print(game_hand)


if __name__ == "__main__":
    main()
      

