import struct

def convert_ida_pattern_to_byte_pattern_and_mask(ida_pattern):
    byte_pattern = []
    mask = []
    i = 0

    while i < len(ida_pattern):
        if ida_pattern[i] == ' ':
            i += 1
            continue
        if ida_pattern[i] == '?':
            byte_pattern.append(0)
            mask.append(False)
            if i + 1 < len(ida_pattern) and ida_pattern[i + 1] == '?':
                i += 2
            else:
                i += 1
        else:
            byte = int(ida_pattern[i:i+2], 16)
            byte_pattern.append(byte)
            mask.append(True)
            i += 2

    return byte_pattern, mask


def string2aob(string :str) -> str:
    aob = ' '.join(f'{ord(c):02X}' for c in string)
    return aob

def ptr2string(ptr :int) -> str:
    aob = ''.join(f'{byte:02X}' for byte in struct.pack('<I', ptr))
    return aob

def compare_bytes(data, pattern, mask, start):
    for i in range(len(pattern)):
        if mask[i] and data[start + i] != pattern[i]:
            return False
    return True

def aob_scan(data, ida_pattern):
    pattern, mask = convert_ida_pattern_to_byte_pattern_and_mask(ida_pattern)
    pattern_length = len(pattern)
    data_length = len(data)

    matches = []

    for i in range(data_length - pattern_length + 1):
        if compare_bytes(data, pattern, mask, i):
            matches.append(i)

    return matches

"""
for data in convert_ida_pattern_to_byte_pattern_and_mask("F8 ? F9 90"):
    print(data)


data = [0xF8, 0x12, 0xF9, 0x90, 0xF8, 0x34, 0xF9, 0x90]
ida_pattern = "F8 ? F9 90"
matches = aob_scan(data, ida_pattern)
print(matches)  # Output: [0, 4]

"""