import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.insert(0, card)

    def add_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self):
        return self.hand.pop()

    def is_empty(self):
        return len(self.hand) == 0

def play_war():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Deal cards to players
    for _ in range(len(deck.cards) // 2):
        player1.add_card(deck.deal_card())
        player2.add_card(deck.deal_card())

    round_num = 0
    while not player1.is_empty() and not player2.is_empty():
        round_num += 1
        print(f"Round {round_num}:")
        card1 = player1.play_card()
        card2 = player2.play_card()
        print(f"{player1.name} plays {card1}, {player2.name} plays {card2}")

        if card1.rank > card2.rank:
            print(f"{player1.name} wins the round!")
            player1.add_cards([card1, card2])
        elif card1.rank < card2.rank:
            print(f"{player2.name} wins the round!")
            player2.add_cards([card1, card2])
        else:
            print("War!")
            war_cards = [card1, card2]
            for _ in range(3):
                war_cards.append(player1.play_card())
                war_cards.append(player2.play_card())
            card1_war = player1.play_card()
            card2_war = player2.play_card()
            print(f"{player1.name} plays {card1_war}, {player2.name} plays {card2_war}")
            if card1_war.rank > card2_war.rank:
                print(f"{player1.name} wins the war!")
                player1.add_cards(war_cards)
            elif card1_war.rank < card2_war.rank:
                print(f"{player2.name} wins the war!")
                player2.add_cards(war_cards)
            else:
                print("Another war!")

    if player1.is_empty():
        print(f"{player2.name} wins the game!")
    else:
        print(f"{player1.name} wins the game!")

play_war()