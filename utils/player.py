from random import shuffle
from card import Card

class Player:
    """
    Class Player which sets up the attributes of each player
    """
    def __init__(self, name: str, cards: str, turn_count: int, number_of_cards: int, history: str):
        turn_count = 0
        number_of_cards = 0
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = len(self.cards)
        self.history = []

    #create a method play()
    def play(self):
        number = int(input("You have {} left, choose the index for the card to be played:".format(
            len(self.cards)
        )))
        card = self.cards[number]
        self.history += [card]
        print(self.name, self.turn_count, "Played: ", card.value, card.symbol)
        return card


    def __str__(self):
        return "hand: {}, turn counter: {}, name: {}, number of cards: {}, cards played: {}".format(
        self.cards, self.turn_count, self.name, self.number_of_cards, self.history
        )


class Deck:
    """
    Creating a complete deck of cards
    """
    def __init__(self, cards: str):
        self.cards = []

    #create a fill_deck() method
    def fill_deck(self):
        for i in ["♥", "♦", "♣", "♠"]:
            for j in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                deck_card = card.Card(j, i)
                self.cards += [deck_card]

    #create a shuffle() method to shuffle the cards
    def shuffle(self):
        shuffle(self.cards)

    #create a distribute() method to distribute the 52 cards of the deck to the players
    def distribute(self, list_of_players: list):
        for i in list_of_players:
            for j in range(0, number_of_cards):
                i.cards += [self.cards[0]]
                self.cards.remove(self.cards[0])


    def __str__(self):
        return "Cards in deck: {}".format(self.cards)
