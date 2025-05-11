import random
import sys

# constans
HEARTS = chr(9828)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"


def main():
    print("""Rules:
                Try to get as close to 21 without going over.
                Kings, Queens, and Jacks are worth 10 points.
                Aces are worth 1 or 11 points.
                Cards 2 through 10 are worth their face value.
                (H)it to take another card.
                (S)stand to stop taking cards.
                On your first play, you can (D)ouble down to increase your bet
                but must hit exactly one more time efore standing.
                In case of a tie, the bet is returned to the player.
                The dealer stops hitting at 17.""")

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
        bet = get_bet(money)

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
            if move == "D":
                # doubling down, they can increase bet:
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print("Bet increased to {}.".format(bet))
            print("Bet:", bet)

            if move in ("H", "D"):
                # takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print("You drew a {} of {}.".format(rank, suit))
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # player busted
                    continue

            if move in ("S", "D"):
                # stops the player turn
                break

        # dealer actions
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # dealer hits
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    # dealer busted
                    break
                input("Press Enter to continue...")
                print("\n\n")

        # final hands
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        # weather player won, lost or tied:
        if dealer_value > 21:
            print("Dealer busts! You win ${}!".format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print("You won ${}".format(bet))
            money += bet
        elif player_value == dealer_value:
            print("It is a tie, the bet is returned to you.")

        input("Press Enter to continue...")
        print("\n\n")


def get_bet(max_bet):
    # how much player want to bet this round
    while True:
        print("How much do you want to bet? (1-{}, or QUIT)".format(max_bet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    # return a list of tuples for 52 cards (rank, suit)
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
        random.shuffle(deck)
        return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    # show player and dealer hands, hide dealer's 1st card if show_dealer_hand is False
    print()
    if show_dealer_hand:
        print("DEALER:", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")
        # hide dealer's 1st card
        display_cards([BACKSIDE] + dealer_hand[1:])

    # show player's cards
    print("PLAYER:", get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            number_of_aces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += "___ "  # top of the card
        if card == BACKSIDE:
            # back of the card
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "| ##| "
        else:
            # front of the card
            rank, suit = card  # card is tuple ds
            rows[1] += "|{} | ".format(rank.ljust(2))
            rows[2] += "| {} | ".format(suit)
            rows[3] += "| {}| ".format(rank.rjust(2, "_"))

    # print each row on the screen
    for row in rows:
        print(row)


def get_move(player_hand, money):
    while True:
        moves = ["(H)it, (S)tand"]

        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # get players move
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()
