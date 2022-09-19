import socket
import struct
import textwrap


def main():
    conn + socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print(TAB_1 + 'Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))








# Unpack ethernet frame ( (SYNC 8byte):(RECIEVER 6byte):(SENDER 6byte):(TYPE 2byte):(PAYLOAD 46byte-1500byte):(CRC 4byte) )
# MAC(Media Access Control) address - unique 12 character alphanumeric attribute (00:B0:D0:63:C2:26)
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

# Return a properly formatted MAC address.
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_addr).upper()
    return mac_addr

# Unpacks IPv4 packet.




main()