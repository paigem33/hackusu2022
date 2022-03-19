import random
class Boneyard:
    """
    Group of dominos that decks are dealt from and players draw from
    """
    def __init__(self, domino_set):
        """
        Creates a randomized list of dominos
        Parameters:
            list of domino objects
        """
        self.__dominos = domino_set
        random.shuffle(self.__dominos)

    def pop(self):
        """
        Returns the last domino in the list
        """
        return self.__dominos[-1]
        
        

