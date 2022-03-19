class PlayerQueue:
    def __init__(self, players_per_game):
        self.__players = []
        self.__players_per_game = players_per_game

    def push_player(self, id):
        if not self.has_player(id):
            self.__players.append(id)

    def remove_player(self, id):
        self.__players.remove(id)

    def can_start(self):
        return len(self.__players) >= self.__players_per_game

    def start_game(self):
        players = self.__players[:self.__players_per_game]
        self.__players = self.__players[self.__players_per_game:]
        return players

    def has_player(self, id):
        return id in self.__players
