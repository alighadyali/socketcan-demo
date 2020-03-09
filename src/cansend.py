import nclib
import can_cmds
import threading
import time
import motor

ip = "127.0.0.1"
port = 29536


def main(args):
    # nc = nclib.Netcat((ip, 29536), udp=False, verbose=False)
    # nc.recv()
    # nc.send(b'< open vcan0 >')
    # nc.recv_until(b'>')
    # nc.send(b'< send 123 0 >')
    # packet = dict(can_id='0xff', length=1, b1=11, b2=22, b3=33, b4=44)
    # packet['b1']=44
    # canbus = can_cmds.CanBus(ip, 29536)
    # canbus.write(packet)
    # canbus.test()
    m.simulate()


if __name__ == "__main__":
    m = motor.Motor('0xcc')
    m.init()

    while True:
        main(m)
        time.sleep(1)
