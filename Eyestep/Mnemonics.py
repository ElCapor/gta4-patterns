r8_names = [
    "al",
    "cl",
    "dl",
    "bl",
    "ah",
    "ch",
    "dh",
    "bh"
]

r16_names = [
    "ax",
    "cx",
    "dx",
    "bx",
    "sp",
    "bp",
    "si",
    "di"
]

r32_names = [
    "eax",
    "ecx",
    "edx",
    "ebx",
    "esp",
    "ebp",
    "esi",
    "edi"
]

r64_names = [
    "rax",
    "rcx",
    "rdx",
    "rbx",
    "rsp",
    "rbp",
    "rsi",
    "rdi"
]

xmm_names = [
    "xmm0",
    "xmm1",
    "xmm2",
    "xmm3",
    "xmm4",
    "xmm5",
    "xmm6",
    "xmm7"
]

mm_names = [
    "mm0",
    "mm1",
    "mm2",
    "mm3",
    "mm4",
    "mm5",
    "mm6",
    "mm7"
]

sreg_names = [
    "es",
    "cs",
    "ss",
    "ds",
    "fs",
    "gs",
    "hs",
    "is"
]

dr_names = [  # debug register
    "dr0",
    "dr1",
    "dr2",
    "dr3",
    "dr4",
    "dr5",
    "dr6",
    "dr7"
]

cr_names = [  # control register
    "cr0",
    "cr1",
    "cr2",
    "cr3",
    "cr4",
    "cr5",
    "cr6",
    "cr7"
]

st_names = [  # FPU stack register
    "st(0)",
    "st(1)",
    "st(2)",
    "st(3)",
    "st(4)",
    "st(5)",
    "st(6)",
    "st(7)"
]

__all__ = ["r8_names", "r16_names", "r32_names", "r64_names", "xmm_names", "mm_names", "sreg_names", "dr_names", "cr_names","st_names"]