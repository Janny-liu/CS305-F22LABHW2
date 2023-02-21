import os
import socket
import struct
import sys
import threading
import time

# def calculate_checksum(data):
#     if len(data) % 2:
#         data += b'\00'
#
#     checksum = 0
#     for i in range(len(data)//2):
#         print("data: "+str(data[2*i:2*i+2]))
#         word, = struct.unpack('!H',data[2*i:2*i+2])
#         checksum += word
#
#     while True:
#         carry = checksum >> 16
#         if carry:
#             checksum = (checksum & 0xffff) + carry
#         else:
#             break
#
#     sum = ~checksum & 0xffff
#
#     return sum#struct.pack('!H', checksum)
#
#
def check_checksum(data,check):
    if len(data) % 2:
        data += b'\00'

    checksum = 0
    for i in range(len(data)//2):
        print(data[2*i:2*i+2])
        word, = struct.unpack('!H',data[2*i:2*i+2])
        checksum += word

    checksum+=check
    print("checksum"+str(checksum))

    while True:
        carry = checksum >> 16
        print("carry: "+str(carry))
        if carry:
            checksum = (checksum & 0xffff) + carry
        else:
            break

    sum = checksum & 0xffff
    if sum==65535:
        return True
    return sum#struct.pack('!H', checksum)
#
# icmp= b'\x08\x00\x00\x01\x00\x01\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69'
# i=b'\x08\x00\x00\x01\x00\x01\x61\x62\x63'
# checksum=calculate_checksum(i)
# print("real checksum:"+str(checksum))
# sum=check_checksum(i,checksum)
packet=b'E\x00\x00p\x00\x05\x00\x00\x80\x01\x00\x00\xc0\xa8\x01g\xc0\xa8\x01g\x03\x01%\xaa\x00\x00\x00\x00E\x00\x00T\xcd\x8a\x00\x00@\x01\x00\x00\xc0\xa8\x01g\xc0\xa8\x01\xbc\x08\x00T\xd5\x0eU\x00\x001h3fn0ueYjgR06TdC5yGzZwegKtJDWazgVHqsVi4frLZ0jVz2MXENk8t'
print(packet[20:28].hex())
print(packet.hex())
type, code = struct.unpack('!BB',packet[20:22])
checksum,=struct.unpack('!H',packet[22:24])
data=packet[20:22]+packet[24:]

print(packet[28:].hex())
print(packet[48:].hex())
print(packet[52:54].hex())
print("t"+str(type))
print("c"+str(code))
print("c"+str(checksum))

