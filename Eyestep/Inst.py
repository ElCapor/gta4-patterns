from dataclasses import dataclass, field
from typing import List, Union
from Operand import Operand
from Constants import MAX_INSTR_READBITS
from OpInfo import OpInfo

@dataclass
class Inst:
    data: str = field(default_factory=lambda: '\0' * 256)
    info: OpInfo = field(default_factory=OpInfo)

    flags: int = 0
    bytes: List[int] = field(default_factory=lambda: [0] * (MAX_INSTR_READBITS // 8))
    len: int = 0
    address: int = 0
    operands: List[Operand] = field(default_factory=lambda: [Operand() for _ in range(4)])

    def source(self) -> Operand:
        if len(self.operands) <= 0:
            return Operand()
        return self.operands[0]

    def destination(self) -> Operand:
        if len(self.operands) <= 1:
            return Operand()
        return self.operands[1]
