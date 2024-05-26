from keystone import keystone
from GtaExecutable import GtaExecutable
import os
from Config import Config
import angr

cfg : Config = Config()

gta : GtaExecutable = GtaExecutable(cfg.get_gta_exe_path(1050))

proj = angr.Project(gta.path)