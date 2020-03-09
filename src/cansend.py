import nclib
import can_cmds

ip = "127.0.0.1"
port = 29536


def main():
    print("Hello World")
    # nc = nclib.Netcat((ip, 29536), udp=False, verbose=False)
    # nc.recv()
    # nc.send(b'< open vcan0 >')
    # nc.recv_until(b'>')
    # nc.send(b'< send 123 0 >')
    canbus = can_cmds.CanBus(ip, 29536)
    canbus.writer()
    
   


if __name__ == "__main__":
    main()