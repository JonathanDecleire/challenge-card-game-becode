class Symbol:
    """
    Class Symbol that defines the color and icon of the card
    """
    def __init__(self, color: str, icon: str):
        self.color = [black, red]
        self.icon = [♥, ♦, ♣, ♠]

    def __str__(self):
        return " A {self.color} {self.icon}".format(self=self)
