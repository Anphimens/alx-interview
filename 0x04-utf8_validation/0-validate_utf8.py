#!/usr/bin/python3


def validUTF8(data):
    index = 0

    while index < len(data):
        # Get the number of leading 1's in the first byte
        byte = data[index]
        num_bytes = 0


        if byte & 0b10000000 == 0:
            num_bytes = 1
        elif byte  & 0b11100000 == 0b11000000:
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:
            num_bytes = 4
        else:
            return False
        
        # Check if there are enough bytes left
        if index + num_bytes > len(data):
            return False
        
        # Check the continuation bytes
        for i in range(1, num_bytes):
            if index + i >= len(data) or data[index + i] & 0b11000000 != 0b10000000:
                return False
        
        # Move to the next character
        index += num_bytes

    return True
