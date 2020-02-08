def prop(obj, att, val):
    obj[att] = val
    return obj


def every(cond, it):
    for x in it:
        if not cond(x):
            return False
    return True
