#!/usr/bin/python3
"""
utf-8 validation
"""


def validUTF8(data):
    """
    determines if a given data set
    represents a valid UTF-8 encoding
    """
    con_bytes = 0

    for byte in data:
        if con_bytes > 0:
            if (byte >> 6) == 0b10:
                con_bytes -= 1
            else:
                return False
        else:
            if (byte >> 7) == 0:
                con_bytes = 0
            elif (byte >> 5) == 0b110:
                con_bytes = 1
            elif (byte >> 4) == 0b1110:
                con_bytes = 2
            elif (byte >> 3) == 0b11110:
                con_bytes = 3
            else:
                return False
    return True
