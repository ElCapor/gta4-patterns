from keystone import keystone
from GtaExecutable import GtaExecutable
import os
from Config import Config
from Eyestep.Eyestep import Eyestep
from Eyestep.Pattern import get_relative,read_int,read_bytes,convert_ida_pattern_to_byte_pattern_and_mask, aob_scan, xref_string
from Eyestep.Utils import d2h, h2d, b2h

config : Config = Config()


data = bytearray([
    0x90, 0x90, 0xE8, 0x01, 0x00, 0x00, 0x00,  # NOP NOP CALL 0x00000001
    0x90, 0x90, 0xE9, 0x02, 0x00, 0x00, 0x00   # NOP NOP JMP  0x00000002
])
start_address = 2  # Position of the CALL instruction
relative_address = get_relative(data, start_address)
print(f"Relative address from CALL instruction at {start_address}: {relative_address:#x}")

start_address = 9  # Position of the JMP instruction
relative_address = get_relative(data, start_address)
print(f"Relative address from JMP instruction at {start_address}: {relative_address:#x}")

for version in [1200]:
    print(f"====================[VERSION {version} START]=======================")
    gta : GtaExecutable = GtaExecutable(config.get_gta_exe_path(version))

    eye : Eyestep = Eyestep(gta.path)

    matches = aob_scan(eye.data, "8B CE E8 ? ? ? ? 81 C6 84 3A 00 00")
    res = read_bytes(eye.data, matches[0], 10)
    print(b2h(res))
    print(read_int(eye.data, matches[0]))
    print(d2h(get_relative(eye.data, matches[0] + 2) + 0x401000))
#print(matches)
    print([d2h(num + 0x400000) for num in matches])
"""
    print([d2h(num + gta.get_image_base()) for num in matches])
    for sublist in xref_string(eye.data, "commonimg:/"):
        print([d2h(num + gta.get_image_base()) for num in sublist])
        print([b2h(eye.data[num - 1:num + 5]) for num in sublist])
"""
#print(d2h(gta.get_image_base()))
