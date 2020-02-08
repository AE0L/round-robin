is_zero = lambda a: a == 0
prop    = lambda a, b: a[b]
equals  = lambda a, b: a == b


def set_prop(obj, att, val):
    obj[att] = val
    return obj


def every(cond, itr):
    for x in itr:
        if not cond(x):
            return False
    return True


def reduce(func, itr, acc=0):
    for x in itr:
        acc = func(x, acc)
    return acc


def foreach(func, itr):
    for x in itr:
        func(x)
    return itr
