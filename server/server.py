import enet
from time import sleep
from enum import Enum
from client import Client
import pathlib
import sys
from player_queue import PlayerQueue

directory = pathlib.Path(__file__).resolve()
sys.path.append(str(directory.parent.parent))

from common import event


class Server:
    def __init__(self):
        self.__host = enet.Host(enet.Address(b"0.0.0.0", 8080), 500, 0, 0, 0)
        self.__clients = {}
        self.__instances = []
        self.__queue = PlayerQueue(4)

    def run(self):
        while True:
            enet_event = self.__host.service(1)
            if enet_event.type == enet.EVENT_TYPE_CONNECT:
                self.__clients[str(enet_event.peer.address)] = Client()
                print("Connect " + str(enet_event.peer.address))
            elif enet_event.type == enet.EVENT_TYPE_DISCONNECT:
                del self.__clients[str(enet_event.peer.address)]
                print("Disconnect " + str(enet_event.peer.address))
            elif enet_event.type == enet.EVENT_TYPE_RECEIVE:
                packet = event.Event(bytes=enet_event.packet.data)
                print("Packet " + str(enet_event.peer.address) + " " + str(packet.get_data().get_type()))
                type = packet.get_data().get_type()
                if type == event.QueueEvent.JOIN_QUEUE:
                    self.__queue.push_player(str(enet_event.peer.address))
                if type == event.QueueEvent.LEAVE_QUEUE:
                    self.__queue.remove_player(str(enet_event.peer.address))
