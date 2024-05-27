def d2h(h :int) -> str:
    return hex(h)

def h2d(h :str) -> str:
    return int(h, 16)

__all__ = ["d2h", "h2d"]