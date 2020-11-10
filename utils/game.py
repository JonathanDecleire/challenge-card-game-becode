from player import Player

class Board():
    """
    Class Board with its attributes and method
    """
    def __init__(self, players: str, turn_count: int, active_cards: int, history_cards: int):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    #create a method start_game()
    def start_game(self):
        """
        Method that starts the game using all classes and methods
        """
        #while loop to enter all the players names
        while True:
            player_name = input("Enter player name or 'end' if all players entered:")
            if player_name == "end":
                break
            else:
                self.players += [player.Player(player_name)]
                print("{} added to the players>".format(player_name))

        #Create an object deck
        main_deck = player.Deck()
        #Create the cards in the deck
        main_deck.fill_deck()
        #Shuffle the cards
        main_deck.shuffle()
        #Distribute all the cards to the players
        main_deck.distribute(self.players)
        #Each turn of the loop is one play of the game
        for i in range(0, int(52 / len(self.players))):
            self.active_cards = []
            for j in self.players:
                card = j.play()
                self.activate_cards += [card]
                j.cards.remove(card)
                j.turn_count += 1
            self.history_card += self.active_cards
            self.turn_count += 1
            print("turn nbr: {} \n Cards played this turn: {} \n Number of cards played in the game: {}".format(
                self.turn_count, self.activate_cards, len(self.history_card)
            ))
        print("No cards left, the end.")

    def __str__(self):
        return "Players: {}, turn: {}, cards played this turn: {}, cards played: {}".format(
        self.players, self.turn_count, self>active_cards, self.history_card
        )
