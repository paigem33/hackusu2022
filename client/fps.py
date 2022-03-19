from time import time, sleep


def limit_fps(start_time, target_fps):
    """
    Limits this single frame based off of our target fps
    Parameters:
        start_time (int) Time from when the frame started
        target_fps (int) Target fps
    """
    time_per_frame = (1000 / target_fps) / 1000
    current_time = time()
    if time() - start_time < time_per_frame:
        sleep_time = time_per_frame - (current_time - start_time)
        sleep(sleep_time)


class FpsCounter:
    """
    Counts frames per second
    """
    def __init__(self):
        """
        Createa a new counter
        """
        self.__frames = 0
        self.__fps = 0
        self.__start_time = time()

    def update(self):
        """
        Adds a frame and checks to see if a second has passed, if it has, update the fps and restart.
        """
        self.__frames += 1
        if time() - self.__start_time >= 1.0:
            self.__fps = self.__frames
            self.__frames = 0
            self.__start_time = time()

    def get_fps(self):
        """
        Returns the calulated fps. This will be zero unitl one second has passed
        """
        return self.__fps
