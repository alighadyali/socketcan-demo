import nclib
import can_cmds
import random
from datetime import datetime


class Motor:

    def __init__(self, can_id):
        self.can_id = can_id
        self.speeds = None
        self.temp = None
        self.rpm = None
        self.index = 0
        self.counter = 0
        self.changeDataCounter = 0
        self.loop = 0

    def init(self):
        random.seed(datetime.now())
        self.speeds = random.sample(range(1, 100), 5)
        self.speeds.sort()
        self.temp = random.sample(range(1, 75), 5)
        self.temp.sort()
        self.rpm = random.sample(range(0, 4000), 5)
        self.rpm.sort()

    def simulate(self):
        # if (self.counter <= 5):
        #     print("speed={} temp={} rpm={}".format(self.speeds[self.index],
        #                                            self.temp[self.index],
        #                                            self.rpm[self.index]))
        #     self.changeDataCounter += 1
        #     self.counter += 1
        #     # if (self.changeDataCounter % 6 == 0):
        #     #     # self.index += 1
        #     #     self.counter += 1
        # else:
        #     if (self.changeDataCounter % 6 == 0):
        #         print("the 6")
        #         if()
        #         self.index += 1
        #     self.counter = 0
        #     self.changeDataCounter = 0
        #     # self.index = 0
        #     # self.init()
        if (self.counter < 5):
            print(self.index)
            self.counter += 1
        else:
            if (self.index < 5):
                self.index += 1
            else:
                self.index = 0
            self.counter = 0
            self.loop += 1
            print(self.loop)
