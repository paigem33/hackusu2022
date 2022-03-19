from time import time, sleep


def limit_fps(start_time, target_fps):
    time_per_frame = (1000 / target_fps) / 1000
    current_time = time()
    if time() - start_time < time_per_frame:
        sleep_time = time_per_frame - (current_time - start_time)
        sleep(sleep_time)


class FpsCounter:
    def __init__(self):
        self.__frames = 0
        self.__fps = 0
        self.__start_time = time()

    def update(self):
        self.__frames += 1
        if time() - self.__start_time >= 1.0:
            self.__fps = self.__frames
            self.__frames = 0
            self.__start_time = time()

    def get_fps(self):
        return self.__fps
