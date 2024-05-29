import struct
from .Utils import d2h, h2d

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
    aob = ' '.join(f'{byte:02X}' for byte in struct.pack('<I', ptr))
    return aob

def compare_bytes(data, pattern, mask, start):
    for i in range(len(pattern)):
        if mask[i] and data[start + i] != pattern[i]:
            return False
    return True

def aob_scan(data :bytes, ida_pattern :str, offset :int = 0):
    pattern, mask = convert_ida_pattern_to_byte_pattern_and_mask(ida_pattern)
    pattern_length = len(pattern)
    data_length = len(data)

    matches = []

    for i in range(data_length - pattern_length + 1):
        if compare_bytes(data, pattern, mask, i):
            matches.append(i + offset)

    return matches


def find_pattern(data :bytes, ida_pattern :str, offsets :list[int] = [], deferences :list[int] = []) -> list[int]:
    # you must specify an offset for each deference even if it's 0
    
    # initial scan
    matches = aob_scan(data, ida_pattern)
    ret = []
    for match in matches:
        if (len(deferences) > 0):
            for i in range(len(deferences)):
                match += offsets[i]
                # careful, the ptr we readin is prolly tied to base address
                match = read_ptr(data, match)
        else:
            match += offsets[0]
        ret.append(match)
    return ret

def xref_string(data, string :str) -> list[int]:
    # careful , hardcoded base address
    result :list[int] = aob_scan(data, string2aob(string))
    print(d2h(result[0] + 0x401000))
    if len(result) > 0:
        return [aob_scan(data, ptr2string(ptr + 0x401000)) for ptr in result]
    else:
        print(f"[WARNING] String {string} not found in memory")
        return []
    
def read_bytes(data,start, len) ->bytes:
    return data[start:start+len]

def read_int(data, start, le :bool = False, signed :bool = False) -> int:
    return int.from_bytes(read_bytes(data, start, 4), byteorder="little" if le else "big", signed=signed)

# read a ptr, for now same as int
def read_ptr(data , start) -> int:
    return read_int(data, start)

def get_relative(data, start) -> int:
    return start + 5 + read_int(data, start + 1, True, True)


"""
for data in convert_ida_pattern_to_byte_pattern_and_mask("F8 ? F9 90"):
    print(data)


data = [0xF8, 0x12, 0xF9, 0x90, 0xF8, 0x34, 0xF9, 0x90]
ida_pattern = "F8 ? F9 90"
matches = aob_scan(data, ida_pattern)
print(matches)  # Output: [0, 4]

"""