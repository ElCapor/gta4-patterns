from keystone import keystone
from GtaExecutable import GtaExecutable
import os
from Config import Config
from Eyestep.Eyestep import Eyestep
from Eyestep.Pattern import convert_ida_pattern_to_byte_pattern_and_mask, aob_scan, xref_string
from Eyestep.Utils import d2h, h2d

config : Config = Config()

for version in [1200]:
    print(f"====================[VERSION {version} START]=======================")
    gta : GtaExecutable = GtaExecutable(config.get_gta_exe_path(version))

    eye : Eyestep = Eyestep(gta.path)

    matches = aob_scan(eye.data, "8B CE E8 ? ? ? ? 81 C6 84 3A 00 00")
#print(matches)
#print([d2h(num) for num in matches])
    print([d2h(num + gta.get_image_base()) for num in matches])
    for sublist in xref_string(eye.data, "commonimg:/"):
        print([d2h(num + gta.get_image_base()) for num in sublist])
        print([d2h(eye.data[num:num + 5]) for num in sublist])
#print(d2h(gta.get_image_base()))
