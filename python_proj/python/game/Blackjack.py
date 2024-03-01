import random

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_score(self, hand):
        score = sum(self.card_value(card) for card in hand)
        if score > 21 and self.has_ace(hand):
            score -= 10
        return score

    def card_value(self, card):
        rank = card['rank']
        if rank in ['King', 'Queen', 'Jack']:
            return 10
        elif rank == 'Ace':
            return 11
        else:
            return int(rank)

    def has_ace(self, hand):
        return any(card['rank'] == 'Ace' for card in hand)

    def display_hands(self, player_turn=True):
        if player_turn:
            print(f"Your cards: {self.player_hand}, current score: {self.calculate_score(self.player_hand)}")
        else:
            print(f"Dealer's first card: {self.dealer_hand[0]}")

    def play_game(self):
        for _ in range(2):
            self.deal_card(self.player_hand)
            self.deal_card(self.dealer_hand)

        game_over = False
        while not game_over:
            self.display_hands()
            player_score = self.calculate_score(self.player_hand)
            dealer_score = self.calculate_score(self.dealer_hand)

            if player_score == 21 or dealer_score == 21 or player_score > 21:
                game_over = True
            else:
                user_choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
                if user_choice == 'y':
                    self.deal_card(self.player_hand)
                else:
                    game_over = True

        # Dealer's turn
        while dealer_score < 17:
            self.deal_card(self.dealer_hand)
            dealer_score = self.calculate_score(self.dealer_hand)

        self.display_hands(player_turn=False)
        self.display_winner(player_score, dealer_score)

    def display_winner(self, player_score, dealer_score):
        if player_score > 21:
            print("You went over. You lose!")
        elif dealer_score > 21:
            print("Dealer went over. You win!")
        elif player_score == dealer_score:
            print("It's a draw!")
        elif player_score == 21:
            print("Blackjack! You win!")
        elif dealer_score == 21:
            print("Dealer has a Blackjack. You lose!")
        elif player_score > dealer_score:
            print("You win!")
        else:
            print("You lose!")

# Run the game
if __name__ == "__main__":
    blackjack_game = Blackjack()
    blackjack_game.play_game()
