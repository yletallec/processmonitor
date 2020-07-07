def mem_to_octet(mem):
    if len(mem) == 0:
        return None
    factor = 1
    last_char = mem[-1].upper()
    if last_char == "T":
        factor = 1024**4
    elif last_char == "G":
        factor = 1024**3
    elif last_char == "M":
        factor = 1024**2
    elif last_char == "K":
        factor = 1024
    try:
        val = int(mem[:-1] if factor > 1 else mem)
    except:
        return None
    return val * factor if val >= 0 else None

def string_to_integer(val):
    try:
        val = float(val)
        if not val.is_integer():
            raise Exception("Not an integer")
    except ValueError:
        raise
    return int(val)
