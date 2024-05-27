from dataclasses import dataclass, field
from typing import List

@dataclass
class Operand:
    flags: int = 0
    opmode: int = 0
    reg: List[int] = field(default_factory=list)
    mul: int = 0

    rel8: int = 0
    rel16: int = 0
    rel32: int = 0

    imm8: int = 0
    imm16: int = 0
    imm32: int = 0

    disp8: int = 0
    disp16: int = 0
    disp32: int = 0

    def append_reg(self, reg_type: int) -> int:
        self.reg.append(reg_type)
        return reg_type