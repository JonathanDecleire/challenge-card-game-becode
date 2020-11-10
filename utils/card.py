class Symbol:
    """
    Class Symbol that defines the color and icon of the card
    """
    def __init__(self, color: str, icon: str):
        #self.color = ["black", "red"]
        self.icon = icon #["♥", "♦", "♣", "♠"]
        if icon == "♥" or icon == "♦":
            self.color = "red"
        else:
            self.color = "black"

    def __str__(self):
        return "icon: {}, color: {}".format(self.icon, self.color)

class Card(Symbol):
    """
    Class Card inherits from Class Symbol
    """
    def __init__(self, value: str, icon: str):
        super().__init__(icon)
        self.value = value

    # def __init__(self, color: str, icon: str, value: str):
    #     self.color = ["black", "red"]
    #     self.icon = ["♥", "♦", "♣", "♠"]
    #     self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __str__(self):
        return " value: {}, icon: {}, color: {}".format(self.value, self.icon, self.color)
