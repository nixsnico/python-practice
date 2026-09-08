import random as rng
import colorama

colorama.init()

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
values = {str(i): i for i in range(2, 11)}
values.update({'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11})




class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append((rank, suit))
        rng.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.folded = False

    # New method to clear player data between rounds
    def reset_round(self):
        self.hand = []
        self.score = 0
        self.folded = False

    def calc_score(self):
        self.score = 0
        aces = 0
        for card, _ in self.hand:
            self.score += values[card]
            if card == 'Ace':
                aces += 1
        while self.score > 21 and aces > 0:
            self.score -= 10
            aces -= 1

    def show_hand(self):
        handstr = ", ".join(f"{rank} of {suit}" for rank, suit in self.hand)
        print(f"{self.name}'s hand: {handstr} (Score: {self.score})")


def play():
    print("=== Welcome to BlackJack ===")
    
    wallet = 1000;
    walletmin = 100;
    
    # Get player count once at the very start
    num_players = int(input("Enter num of players (1-5): "))
    player_list = []
    print(f"Your balance is {colorama.Fore.GREEN}${wallet}{colorama.Style.RESET_ALL}");
    
    for i in range(num_players):
        player_name = f"Player {i + 1}"
        player_list.append(Player(player_name))
        
    dealer = Player("Dealer")

    # NEW: Game Loop Starts Here
    while True:
        print("\n===============================")
        print("      STARTING A NEW ROUND     ")
        print("===============================")

        while True:
            betting = int(input("How much would you like to bet?: "))
            if betting > wallet:
                print("Balance is too low!")
                continue
            break

        wallet -= betting
        print(f"Your new balance is {colorama.Fore.GREEN}${wallet}{colorama.Style.RESET_ALL}.")
        
        # Fresh deck for the new round
        deck = Deck()
        
        # Reset all players and deal 2 cards
        for player in player_list:
            player.reset_round()
            player.hand.append(deck.deal_card())
            player.hand.append(deck.deal_card())
            player.calc_score()
            
        # Reset dealer and deal 2 cards
        dealer.reset_round()
        dealer.hand.append(deck.deal_card())
        dealer.hand.append(deck.deal_card())
        dealer.calc_score()

        # Players' turns
        for player in player_list:
            print(f"\n--- {player.name}'s Turn ---")
            while True:
                player.show_hand()
                if player.score > 21:
                    print(f"{player.name} Busted!")
                    break
                    
                action = input(f"{player.name}, choose action: Hit (H), Stay (S), Fold (F): ").strip().upper()
                
                if action == 'H':
                    new_card = deck.deal_card()
                    player.hand.append(new_card)
                    player.calc_score()
                    print(f"{player.name} draws {new_card[0]} of {new_card[1]}")
                    if player.score > 21:
                        print(f"{player.name} busted with a score of {player.score}.")
                        break
                elif action == 'S':
                    print(f"{player.name} stays with a score of {player.score}")
                    break
                elif action == 'F':
                    player.folded = True
                    print(f"{player.name} folds.")
                    break
                else:
                    print("Invalid choice. Please enter H, S, or F.")

        # Dealer's turn
        print("\n--- Dealer's Turn ---")
        dealer.show_hand()
        while dealer.score < 17:
            print("Dealer hits...")
            dealer.hand.append(deck.deal_card())
            dealer.calc_score()
            dealer.show_hand()
            
        if dealer.score > 21: 
            print("Dealer is Out/Bust!")
            
        # Round Results
        print("\n=== ROUND RESULTS ===")
        for player in player_list:
            if player.folded:
                
                print(f"{player.name}: Folded")
            elif player.score > 21:
                print(f"{player.name}: Busted ({player.score})")
                if wallet == 0:
                    wallet += 100  
                    print(f"Your balance is too low! You have been given $100 to continue playing. Your new balance is {colorama.Fore.RED}${wallet}{colorama.Style.RESET_ALL}.")

            elif dealer.score > 21 or player.score > dealer.score:
                print(f"{player.name}: Wins! ({player.score} vs Dealer's {dealer.score})")
                betting *=2
                wallet +=betting
                print(f"You win ${betting}. Your new balance is {colorama.Fore.GREEN}${wallet}{colorama.Style.RESET_ALL}.")

            elif player.score < dealer.score:
                print(f"{player.name}: Loses ({player.score} vs Dealer's {dealer.score})")
                if wallet == 0:
                    wallet += 100
                    print(f"Your balance is too low! You have been given $100 to continue playing. Your new balance is {colorama.Fore.RED}${wallet}{colorama.Style.RESET_ALL}.")
            else:
                print(f"{player.name}: Push/Tie ({player.score})")

        # NEW: Ask to play again or exit
        print("Your Current Balance is: ", colorama.Fore.GREEN + f"${wallet}{colorama.Style.RESET_ALL}")
        again = input("\nDo you want to play another round? (Y/N): ").strip().upper()
        if again != 'Y':
            print("\nThanks for playing! Goodbye!")
            break # Breaks the while loop and closes the game

if __name__ == "__main__":
    play()

