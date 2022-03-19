import pickle


class Event:
    def __init__(self, data=None, bytes=None):
        if bytes is not None:
            other = pickle.loads(bytes)
            self.__data = other.__data
        else:
            self.__data = data

    def to_bytes(self):
        return pickle.dumps(self)

    def get_data(self):
        return self.__data


class QueueEvent:
    JOIN_QUEUE = 0
    LEAVE_QUEUE = 1

    def __init__(self, type):
        self.__type = type

    def get_type(self):
        return self.__type


class InstanceEvent:
    INSTANCE_START = 2
    INSTANCE_PASS = 3
    INSTANCE_ADD_DOMINO = 4
    INSTANCE_DRAW_DOMINO = 5
    INSTANCE_CLIENT_TURN = 6  # Tells which client turn it is. If it's the client's turn, let them know valid positons and the state of the game. Update from previous player.
    INSTANCE_GAME_FINISHED = 7
    INSTANCE_CLIENT_LEAVE = 8

    def __init__(self, type, data):
        self.__type = type
        self.__data = data

    def get_type(self):
        return self.__type

    def get_data(self):
        return self.__data
