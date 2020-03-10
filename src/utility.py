# class student:
#     def __init__(self, n, a):
#         self.full_name = n
#         self.age = a

#     def get_age(self):
#         return self.age
import nclib
from bitstring import BitArray
import math
import binascii
import struct

class Writer:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def write(self, data):
        print(data)
        nc = nclib.Netcat((self.ip, self.port), udp=False, verbose=False)
        nc.recv()
        nc.send(b'< open vcan0 >')
        nc.send(data)
        nc.shutdown()

class Formatter:
    def formatCanID(self, can_id):
        return can_id.encode() + b' '

    def beginFrame(self, can_id):
        return b'< send ' + can_id.encode() + b' '

    def endFrame(self):
        return b' >'

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #
    # Given an 8-bit signed integer number, produce a hexidecimal byte
    # string object that represents a 1-byte signed integer in a
    # format that is compatible with the byte string to be sent over
    # CAN using nclib.Netcat.
    #

    def prepareInt8as1Bytes(self, i):
        """Converts i to a hex encoded('utf-8') byte string with
           a b' ' appended to the end."""
        word = BitArray(int=i, length=8)
        b = word[0:8].hex.encode('utf-8') + b' '
        return b

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Given a 16-bit signed integer number, produce a hexidecimal byte
    # string object that represents a 2-byte signed integer in a
    # format that is compatible with the byte string to be sent over
    # CAN using nclib.Netcat.
    #
    def prepareInt16as2Bytes(self, i):
        word = BitArray(int=i, length=16)
        lb = word[0:8].hex.encode('utf-8') + b' '
        ub = word[8:16].hex.encode('utf-8') + b' '
        return ub + lb

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Given a 16-bit unsigned integer number, produce a hexidecimal
    # byte string object that represents a 2-byte unsigned integer in
    # a format that is compatible with the byte string to be sent over
    # CAN using nclib.Netcat.
    #
    def prepareUInt16as2Bytes(self, i):
        word = BitArray(uint=i, length=16)
        lb = word[0:8].hex.encode('utf-8') + b' '
        ub = word[8:16].hex.encode('utf-8') + b' '
        return ub + lb

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Given a 32-bit integer number, produce a hexidecimal byte string
    # object that represents a 4-byte integer in a format that is
    # compatible with the byte string to be sent over CAN using
    # nclib.Netcat.
    #
    def prepareInt32as4Bytes(self, i):
        word = BitArray(int=i, length=32)
        b0 = word[0:8].hex.encode('utf-8') + b' '
        b1 = word[8:16].hex.encode('utf-8') + b' '
        b2 = word[16:24].hex.encode('utf-8') + b' '
        b3 = word[24:32].hex.encode('utf-8') + b' '
        return b3 + b2 + b1 + b0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Given a 32-bit IEEE float number, produce a hexidecimal byte
    # string object that represents a 4-byte HValue. An HValue is
    # understood on the the embedded system to be a 2-byte integer and
    # a 2-byte fractional representation of a 32-bit floating point
    # number.
    #
    def prepareFloatasHValue(self, x):
        HValue = math.modf(x)
        i = int(HValue[1])
        f = int(HValue[0] * 10000)
        w1 = self.prepareInt16as2Bytes(i)
        w0 = self.prepareInt16as2Bytes(f)
        return w1 + w0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Given a 32-bit IEEE float number, produce a hexadecimal byte
    # string object that represents the floating point number and is
    # in a format that is compatible with the byte string to be sent
    # over CAN using nclib.Netcat.
    #
    # Given: 123.4567, returns: b'd5 e9 f6 42 '
    #
    # This matches the ordering of the data bytes required by the
    # C2000 embedded system.
    #
    def prepareFloat32as4Bytes(self, x):
        word = struct.pack('!f', x)
        wordBytes = binascii.hexlify(word)
        wordStr = wordBytes.decode(encoding='utf-8', errors='strict')
        b0 = wordStr[:2].encode('utf-8') + b' '
        b1 = wordStr[2:4].encode('utf-8') + b' '
        b2 = wordStr[4:6].encode('utf-8') + b' '
        b3 = wordStr[6:8].encode('utf-8') + b' '
        return b3 + b2 + b1 + b0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    def prepareInt8as4bits(self, i):
        word = BitArray(uint=i, length=4)
        b = word[0:4].hex.encode('utf-8') + b''
        return b