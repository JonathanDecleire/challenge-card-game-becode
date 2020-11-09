class Symbol:
    """
    Class Symbol that defines the color and icon of the card
    """
    def __init__(self, color: str, icon: str):
        self.color = ["black", "red"]
        self.icon = ["♥", "♦", "♣", "♠"]

    def __str__(self):
        return " A {self.color} {self.icon}".format(self=self)

class Card(Symbol):
    """
    Class Card inherits from Class Symbol
    """
    def __init__(self, color: str, icon: str, value: str):
        self.color = ["black", "red"]
        self.icon = ["♥", "♦", "♣", "♠"]
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __str__(self):
        return " A {self.color} {self.icon} {self.value}".format(self=self)
