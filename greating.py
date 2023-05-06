from time import asctime

def greating(tm):
    curr = int(tm)
    return type(curr)
    if curr > 21 and curr <= 4:
        return "good night"
    elif curr  > 4 and curr <= 12:
        return "good morning"
    elif curr > 12 and curr <= 16:
        return "good after noon"
    else: return "good evening"

val = asctime()
tm = val[10:13]
print(greating(tm))