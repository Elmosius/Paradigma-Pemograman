# Unicode string

def main():
    byte1 = b'abcdfedg'
    print(byte1)
    print(type(byte1))
    print(list(map(hex, byte1)))
    print(list(map(bin, byte1)))
    
    byte2 = bytes([137,80,78,71,13,10,26,10])
    print(byte2)
    
    char1 = b'\x63\x63\x69\x63\x68\xc3\xa9'
    print(char1)
    print(char1.decode("utf-8"))
    print(char1.decode("iso8859-5"))
    print(char1.decode("cp037"))
    
    ba = bytearray(b"abcdefgh")
    print(ba)
    ba[4:6] = b"\x15\xa3"
    print(ba)
    ba = bytearray(b"abcdefgh")
    print(ba)
    ba[3] = ord(b'g')
    ba[4] = 65
    print(ba)
    
if __name__ == "__main__":
    main()