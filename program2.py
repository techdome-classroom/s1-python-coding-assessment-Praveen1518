import re

def decode_message(s: str, p: str) -> bool:
    p = p.replace('?', '.')
    p = p.replace('*', '.*')
    regex = f"^{p}$"
    return bool(re.match(regex, s))