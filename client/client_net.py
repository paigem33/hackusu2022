import enet
import pathlib
import sys

directory = pathlib.Path(__file__).resolve()
sys.path.append(str(directory.parent.parent))

from common import event


class ClientNet:
    def __init__(self):
        self.__connect()
        self.__events = []

    def update(self):
        while True:
            self.__sock.send(0, enet.Packet(event.Event(event.QueueEvent(event.QueueEvent.JOIN_QUEUE)).to_bytes()))
            enet_event = self.__host.service(1)
            if enet_event.type == enet.EVENT_TYPE_NONE:
                break
            elif enet_event.type == enet.EVENT_TYPE_RECEIVE:
                self.__events.append(enet_event.Event(bytes=enet_event.packet.data))

    def poll(self):
        self.__events.pop(0)

    def __connect(self):
        self.__host = enet.Host(None, 1, 0, 0, 0)
        self.__sock = self.__host.connect(enet.Address(b"localhost", 8080), 1)
        event = self.__host.service(5000)
        if event.type != enet.EVENT_TYPE_CONNECT:
            raise "Failed to connect to server!"
        else:
            print("Connected to server!")
