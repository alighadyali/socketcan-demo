import utility
import random
from datetime import datetime
from utility import Writer, Formatter


class Driver:

    def __init__(self, motor, timeMachine, gyroscope, gps):
        self.index = 0
        self.counter = 0
        self.motor = motor
        self.motor.init()
        self.motor.makeBytes(self.counter)
        self.timeMachine = timeMachine
        self.timeMachine.init()
        self.timeMachine.makeBytes(self.counter)
        self.gyroscope = gyroscope
        self.gyroscope.init()
        self.gyroscope.makeBytes(self.counter)
        self.gps = gps
        self.gps.init()
        self.gps.makeBytes(self.counter)
        self.ip = "127.0.0.1"
        self.port = 29536
        self.writer = Writer(self.ip, self.port)

    def simulate(self):
        if (self.counter < 6):
            self.motor.printData(self.index)
            self.writer.write(self.motor.data)
            self.timeMachine.printData(self.index)
            self.writer.write(self.timeMachine.data)
            self.gyroscope.printData(self.index)
            self.writer.write(self.gyroscope.data)
            self.gps.printData(self.index)
            self.writer.write(self.gps.data)
            self.counter += 1
        else:
            if (self.counter == 6 and self.index < 4):
                self.index += 1
                self.counter = 0
                # make bytes at new index
                self.motor.makeBytes(self.index)
                self.timeMachine.makeBytes(self.index)
                self.gyroscope.makeBytes(self.index)
                self.gps.makeBytes(self.index)
                # print("next idx")
                # print(self.index)
            else:
                self.index = 0
                self.counter = 0
                # re initialize data
                self.motor.init()
                self.timeMachine.init()
                self.gyroscope.init()
                self.gps.init()
                # print("new data")


class Motor:

    def __init__(self, can_id):
        self.can_id = can_id
        self.speeds = None
        self.temp = None
        self.rpm = None
        self.length = 4
        self.data = None

    def init(self):
        random.seed(datetime.now())
        self.speeds = random.sample(range(1, 100), 5)
        self.speeds.sort()
        self.temp = random.sample(range(1, 75), 5)
        self.temp.sort()
        self.rpm = random.sample(range(0, 4000), 5)
        self.rpm.sort()
        self.printDataArray()

    def makeBytes(self, index):
        self.data = Formatter().beginFrame(
            self.can_id) + Formatter().prepareInt8as1Bytes(
                self.length) + Formatter().prepareInt8as1Bytes(
                    self.speeds[index]) + Formatter().prepareInt8as1Bytes(
                        self.temp[index]) + Formatter().prepareInt16as2Bytes(
                            self.rpm[index]) + Formatter().endFrame()
        # print(self.data)

    def printDataArray(self):
        print("speed={} temp={} rpm={}".format(self.speeds, self.temp,
                                               self.rpm))

    def printData(self, index):
        print("speed={} temp={} rpm={}".format(self.speeds[index],
                                               self.temp[index],
                                               self.rpm[index]))


class TimeMachine:

    def __init__(self, can_id):
        self.can_id = can_id
        self.times = None
        self.fluxCap = None
        self.data = None
        self.length = 8

    def init(self):
        random.seed(datetime.now())
        self.times = random.sample(range(-2147483648, 501595200), 5)
        self.times.sort()
        self.fluxCap = random.sample(range(0, 1200000000), 5)
        self.fluxCap.sort(reverse=True)
        self.printDataArray()

    def makeBytes(self, index):
        self.data = Formatter().beginFrame(
            self.can_id) + Formatter().prepareInt8as1Bytes(
                self.length) + Formatter().prepareInt32as4Bytes(
                    self.times[index]) + Formatter().prepareInt32as4Bytes(
                        self.fluxCap[index]) + Formatter().endFrame()

    def printDataArray(self):
        print("time={} fluxcap={}".format(self.times, self.fluxCap))

    def printData(self, index):
        print("time={} fluxcap={}".format(self.times[index],
                                          self.fluxCap[index]))


class Gyroscope:

    def __init__(self, can_id):
        self.can_id = can_id
        self.yaw = None
        self.pitch = None
        self.data = None
        self.length = 8

    def init(self):
        random.seed(datetime.now())
        yaw = random.sample(range(1000, 9000), 5)
        self.yaw = [x / 1000 for x in yaw]
        pitch = random.sample(range(1000, 20000), 5)
        self.pitch = [x / 1000 for x in pitch]
        self.pitch.sort()
        self.printDataArray()

    def makeBytes(self, index):
        self.data = Formatter().beginFrame(
            self.can_id) + Formatter().prepareInt8as1Bytes(
                self.length) + Formatter().prepareFloat32as4Bytes(
                    self.yaw[index]) + Formatter().prepareFloat32as4Bytes(
                        self.pitch[index]) + Formatter().endFrame()

    def printDataArray(self):
        print("yaw={} pitch={}".format(self.yaw, self.pitch))

    def printData(self, index):
        print("yaw={} pitch={}".format(self.yaw[index], self.pitch[index]))


class Gps:

    def __init__(self, can_id):
        self.can_id = can_id
        self.lattitudes = None
        self.longitudes = None
        self.data = None
        self.length = 8

    def init(self):
        random.seed(datetime.now())
        lat = random.sample(range(400000, 600000), 5)
        self.lattitudes = [x / 10000 for x in lat]
        self.lattitudes.sort()
        lon = random.sample(range(1230000, 1250000), 5)
        self.longitudes = [x / -10000 for x in lon]
        self.longitudes.sort(reverse=True)
        print(self.lattitudes)
        print(self.longitudes) 
        # pitch = random.sample(range(1000, 20000), 5)
        # self.pitch = [x / 1000 for x in pitch]
        # self.pitch.sort()
        # self.printDataArray()

    def makeBytes(self, index):
        self.data = Formatter().beginFrame(self.can_id) + Formatter(
        ).prepareInt8as1Bytes(self.length) + Formatter().prepareFloat32as4Bytes(
            self.lattitudes[index]) + Formatter().prepareFloat32as4Bytes(
                self.longitudes[index]) + Formatter().endFrame()

    def printDataArray(self):
        print("lat={} lon={}".format(self.lattitudes, self.longitudes))

    def printData(self, index):
        print("lat={} lon={}".format(self.lattitudes[index],
                                     self.longitudes[index]))
