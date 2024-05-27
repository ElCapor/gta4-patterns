
def d2h(h :int) -> str:
    return hex(h)

def b2h(b :bytes) -> str:
    """Convert bytes into a hex str

    Args:
        b (bytes): the bytes

    Returns:
        str: hex str
    """
    hex_str = b.hex()
    spaced_hex_str = ' '.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2))
    return spaced_hex_str
    

def h2d(h :str) -> str:
    return int(h, 16)

__all__ = ["d2h", "h2d"]