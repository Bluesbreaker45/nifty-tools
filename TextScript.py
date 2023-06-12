def readLines(path):
    import os
    with open(path, "r") as f:
        return [l[:-1] if l[-1] == "\n" else l for l in f.readlines()]

def removeLineSepFunc():
    def r(string: str):
        return string.replace("\n", " ")
    return r