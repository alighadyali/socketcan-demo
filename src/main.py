import nclib
import utility
import threading
import time
import devices


def main(args):
    args.simulate()


if __name__ == "__main__":
    motor = devices.Motor('0xDE')
    delorean = devices.TimeMachine('0xAD')
    gyroscope = devices.Gyroscope('0xBE')
    gps = devices.Gps('0xEF')
    driver = devices.Driver(motor, delorean, gyroscope, gps)

    while True:
        main(driver)
        time.sleep(1)
