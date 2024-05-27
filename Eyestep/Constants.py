from enum import Enum, IntEnum

MAX_INSTR_READBITS = 128

# Prefix Flags
PRE_REPNE = 0x0001
PRE_REPE = 0x0002
PRE_66 = 0x0004
PRE_67 = 0x0008
PRE_LOCK = 0x0010
PRE_SEG_CS = 0x0020
PRE_SEG_SS = 0x0040
PRE_SEG_DS = 0x0080
PRE_SEG_ES = 0x0100
PRE_SEG_FS = 0x0200
PRE_SEG_GS = 0x0400

# Opcode Prefixes
OP_LOCK = 0xF0
OP_REPNE = 0xF2
OP_REPE = 0xF3
OP_66 = 0x66
OP_67 = 0x67
OP_SEG_CS = 0x2E
OP_SEG_SS = 0x36
OP_SEG_DS = 0x3E
OP_SEG_ES = 0x26
OP_SEG_FS = 0x64
OP_SEG_GS = 0x65

# Low-grade filters (or flags) for instructions
OP_NONE = 0x00000000  # Undefined or blank opcode
OP_SINGLE = 0x00000001  # Single operand in opcode (only Source)
OP_SRC_DEST = 0x00000002  # Two operands in opcode (Typical) (Source and Destination)
OP_EXTENDED = 0x00000004  # More than two operands in the opcode
OP_IMM8 = 0x00000010  # This operand has an 8-bit offset
OP_IMM16 = 0x00000020  # This operand has a 16-bit offset
OP_IMM32 = 0x00000040  # This operand has a 32-bit offset
OP_DISP8 = 0x00000080  # This operand has an 8-bit constant value
OP_DISP16 = 0x00000100  # This operand has a 16-bit constant value
OP_DISP32 = 0x00000200  # This operand has a 32-bit constant value
OP_R8 = 0x00000400
OP_R16 = 0x00000800
OP_R32 = 0x00001000
OP_R64 = 0x00002000
OP_XMM = 0x00004000
OP_MM = 0x00008000
OP_ST = 0x00010000
OP_SREG = 0x00020000
OP_DR = 0x00040000
OP_CR = 0x00080000


# 8-bit Registers
class R8(Enum):
    AL = 0
    CL = 1
    DL = 2
    BL = 3
    AH = 4
    CH = 5
    DH = 6
    BH = 7

# 16-bit Registers
class R16(Enum):
    AX = 0
    CX = 1
    DX = 2
    BX = 3
    SP = 4
    BP = 5
    SI = 6
    DI = 7

# 32-bit Registers
class R32(Enum):
    EAX = 0
    ECX = 1
    EDX = 2
    EBX = 3
    ESP = 4
    EBP = 5
    ESI = 6
    EDI = 7

# Operand Types
class OpTypes(IntEnum):
    AL = 0
    AH = 1
    AX = 2
    EAX = 3
    ECX = 4
    EDX = 5
    ESP = 6
    EBP = 7
    CL = 8
    CX = 9
    DX = 10
    Sreg = 11
    ptr16_32 = 12
    Flags = 13
    EFlags = 14
    ES = 15
    CS = 16
    DS = 17
    SS = 18
    FS = 19
    GS = 20
    one = 21
    r8 = 22
    r16 = 23
    r16_32 = 24
    r32 = 25
    r64 = 26
    r_m8 = 27
    r_m16 = 28
    r_m16_32 = 29
    r_m16_m32 = 30
    r_m32 = 31
    moffs8 = 32
    moffs16_32 = 33
    m16_32_and_16_32 = 34
    m = 35
    m8 = 36
    m14_28 = 37
    m16 = 38
    m16_32 = 39
    m16_int = 40
    m32 = 41
    m32_int = 42
    m32real = 43
    m64 = 44
    m64real = 45
    m80real = 46
    m80dec = 47
    m94_108 = 48
    m128 = 49
    m512 = 50
    rel8 = 51
    rel16 = 52
    rel16_32 = 53
    rel32 = 54
    imm8 = 55
    imm16 = 56
    imm16_32 = 57
    imm32 = 58
    mm = 59
    mm_m64 = 60
    xmm = 61
    xmm0 = 62
    xmm_m32 = 63
    xmm_m64 = 64
    xmm_m128 = 65
    STi = 66
    ST1 = 67
    ST2 = 68
    ST = 69
    LDTR = 70
    GDTR = 71
    IDTR = 72
    PMC = 73
    TR = 74
    XCR = 75
    MSR = 76
    MSW = 77
    CRn = 78
    DRn = 79
    CR0 = 80
    DR0 = 81
    DR1 = 82
    DR2 = 83
    DR3 = 84
    DR4 = 85
    DR5 = 86
    DR6 = 87
    DR7 = 88
    IA32_TIMESTAMP_COUNTER = 89
    IA32_SYS = 90
    IA32_BIOS = 91


