class Deck:
    """
    Creates a players' hand of dominos
    """
    def __init__(self):
        """
        Creates an empty hand (list) of dominos
        """
        self.__dominos = []
    
    def add_domino(self, domino):
        """
        Adds a domino to the hand (list)
        Parameters:
            domino object
        """
        self.__dominos.append(domino)

    def remove_domino(self, index):
        """
        Remove a domino from the hand (list) by index
        Parameters:
            index of the domino to remove 
        """
        self.__dominos.pop(index)

