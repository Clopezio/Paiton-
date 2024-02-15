import random

def print_hands(player_hand, player_sum, dealer_hand, dealer_sum, reveal_dealer=False):
    print("Tua mano:", player_hand, "(Somma:", player_sum, ")")
    if reveal_dealer:
        print("Mano del dealer:", dealer_hand, "(Somma:", dealer_sum, ")")
    else:
        print("Mano del dealer:", [dealer_hand[0], "*"])

def play(Money):
    print("Benvenuto nel gioco Blackjack!")
    print("Il gioco consiste nel fare 21 senza sballare.")
    print("Buona fortuna!\n")

    print("Hai", Money, " Dollaroni")
    player_bet = float(input("Inserisci la scommessa: "))
    if player_bet > Money:
        print("Non hai abbastanza soldi per questa scommessa. Riprova.")
        return Money

    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4
    random.shuffle(cards)

    player_hand = [cards.pop(), cards.pop()]
    dealer_hand = [cards.pop(), cards.pop()]

    while True:
        player_sum = sum(player_hand)
        dealer_sum = sum(dealer_hand)

        print_hands(player_hand, player_sum, dealer_hand, dealer_sum)

        if player_sum == 21:
            print("Hai fatto 21! Hai vinto!")
            Money += player_bet
            break
        elif player_sum > 21:
            print("Hai sballato! Hai perso!")
            Money -= player_bet
            break

        action = input("Vuoi pescare un'altra carta? (s/n): ")
        if action.lower() == 's':
            player_hand.append(cards.pop())
        else:
            while dealer_sum < 17:
                dealer_hand.append(cards.pop())
                dealer_sum = sum(dealer_hand)

            print_hands(player_hand, player_sum, dealer_hand, dealer_sum, reveal_dealer=True)

            if dealer_sum > 21:
                print("Il dealer ha sballato! Hai vinto!")
                print("Hai vinto", player_bet, "euro!")
                Money += player_bet
            elif dealer_sum == player_sum:
                print("Pareggio!")
            elif dealer_sum > player_sum:
                print("Il dealer ha vinto!")
                Money -= player_bet
            else:
                print("Hai vinto!") 
                print("Hai vinto", player_bet, "euro!")
                Money += player_bet
            break

    print("Ora hai", Money, "euro!")
    return Money

if __name__ == "__main__":
    Money = 100
    while Money > 0:
        Money = play(Money)
        if Money <= 0:
            print("Hai fatto banca rotta! Il gioco è finito.")
            break
        play_again = input("Vuoi giocare ancora? (s/n): ")
        if play_again.lower() != 's':
            break