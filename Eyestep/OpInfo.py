from dataclasses import dataclass, field
from typing import List
from Constants import OpTypes

@dataclass
class OpInfo:
    code: str
    opcode_name: str
    operands: List[OpTypes] = field(default_factory=list)
    description: str