import re

def regex_match(text, pattern):
    found = re.findall(pattern.lower(), text.lower())
    for match in re.finditer(pattern.lower(), text.lower()):
        start, end = match.span()
        return start
    return -999 