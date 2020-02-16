head          = lambda a: a[0]
keys          = lambda a: list(a.keys())
values        = lambda a: list(a.values())
strlen        = lambda a: len(str(a))
append        = lambda a, b: a.append(b)
mul           = lambda a, b: a * b
is_zero       = lambda a: a == 0
prop          = lambda a, b: a[b]
equals        = lambda a, b: a == b
getter        = lambda a: lambda j: prop(j, a)
getter_setter = lambda a: lambda j, v=None: prop(j, a) if not v else set_prop(j, a, v)
replace       = lambda a, b, c: str(a).replace(b, c)
len_range     = lambda a, start=None: range(len(a)) if not start else range(start, len(a))


def cat(a, b):
    return str(a) + str(b)


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
