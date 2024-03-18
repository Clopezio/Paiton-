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
    player_bet = input("Inserisci la scommessa: ")
    if player_bet == "CHEATER":
        print("OMMADONNA! Sei un cheater! Ti diamo UN BORDELLO di Dollaroni!")
        Money += 1000  
        print("Ora hai", Money, " Dollaroni")
        return Money
    else:
        try:
            player_bet = float(player_bet)
            if player_bet > Money:
                print("Non hai abbastanza soldi per questa scommessa. Riprova.")
                return play(Money)
            elif player_bet < Money:
                print("Hai scommesso", player_bet, "Dollaroni")
            else:
                print("Hai scommesso", player_bet, "Dollaroni")
        except ValueError:
            print("Inserisci un numero valido.")
            return play(Money)
        else:
            print(" ")
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
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
        while action.lower() not in ['s', 'n']:
            print("Scelta non valida. Riprova.")
            action = input("Vuoi pescare un'altra carta? (s/n): ")

        if action.lower() == 's':
            player_hand.append(cards.pop())
        elif action.lower() == 'n':
            while dealer_sum < 17:
                dealer_hand.append(cards.pop())
                dealer_sum = sum(dealer_hand)

            print_hands(player_hand, player_sum, dealer_hand, dealer_sum, reveal_dealer=True)

            if dealer_sum > 21:
                print("Il dealer ha sballato! Hai vinto!")
                Money += player_bet
                break
            elif dealer_sum == player_sum:
                print("Pareggio!")
                break
            elif dealer_sum > player_sum:
                print("Il dealer ha vinto!")
                Money -= player_bet
                break
            else:
                print("Hai vinto!")
                Money += player_bet
                break

    print("Hai", Money, " Dollaroni")
    if Money == 0:
        print("Hai fatto banca rotta! Il gioco è finito. Eccoti 25 Dollaroni per ricominciare!")
        Money = 25

    play_again = input("Vuoi giocare ancora? (s/n): ")
    if play_again.lower() == 's':
        Money = play(Money)

    return Money

<<<<<<< HEAD:BlackJack.py
if __name__ == "__main__":
    try:
        with open('money.txt', 'r') as f:
            Money = float(f.read())
    except FileNotFoundError:
        Money = 100

    while Money > 0:
        Money = play(Money)
        with open('money.txt', 'w') as f:
            f.write(str(Money))
        if Money <= 0:
            print("Hai fatto banca rotta! Il gioco è finito.")
            break
        play_again = input("Vuoi giocare ancora? (s/n): ")
        if play_again.lower() != 's':
            break
=======
try:
    with open('soldi_blackjack.txt', 'r') as f:
        Money = float(f.read())
except FileNotFoundError:
    Money = 100

while Money > 0:
    Money = play(Money)
    with open('soldi_blackjack.txt', 'w') as f:
        f.write(str(Money))
    if Money <= 0:
        print("Hai fatto banca rotta! Il gioco è finito. Eccoti 25 Dollaroni per ricominciare!")
        Money = 25
        with open('soldi_blackjack.txt', 'w') as f:
            f.write(str(Money))
    else:
        break
>>>>>>> 27069001499eebbee901de907bca5ba92ff183da:BlackJack 1.3.py
