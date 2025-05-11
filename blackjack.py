import random, sys

# constans
HEARTS = chr(9828)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''Rules:
                Try to get as close to 21 without going over.
                Kings, Queens, and Jacks are worth 10 points.
                Aces are worth 1 or 11 points.
                Cards 2 through 10 are worth their face value.
                (H)it to take another card.
                (S)stand to stop taking cards.
                On your first play, you can (D)ouble down to increase your bet
                but must hit exactly one more time efore standing.
                In case of a tie, the bet is returned to the player.
                The dealer stops hitting at 17.''')

    money = 5000
    
    # main game loop
    while True:
        if money <= 0:
            print("Your are broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # player's bet for the round
        print("Money:", money)
        bet=get_bet(money)

        # 2 cards for dealer and player
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # player actions
        print("Bet:", bet)
        # loops until player stands or busts
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            # check if player has bust
            if get_hand_value(player_hand) > 21:
                break

            # get player's move, either H, S or D
            move = get_move(player_hand, money - bet)

            # handle player actions
            if move == 'D':
                # doubling down, they can increase bet:
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print('Bet increased to {}.'.format(bet))
            print('Bet:', bet)

            if move in ('H', 'D'):
                # takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print('You drew a {} of {}.'.format(rank, suit))
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # player busted
                    continue

            if move in ('S', 'D'):
                # stops the player turn
                break

        # dealer actions
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # dealer hits
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                dealer_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    # dealer busted
                    break
                input('Press Enter to continue...')
                print(\n\n)

        # final hands
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        # weather player won, lost or tied:
        if dealer_hand > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print('You won ${}'.format(bet))
            money += bet
        elif player_value == dealer_value:
            print('It is a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print(\n\n)








