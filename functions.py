append        = lambda a, b: a.append(b)
equals        = lambda a, b: a == b
getter        = lambda a: lambda j: prop(j, a)
getter_setter = lambda a: lambda j, v=None: prop(j, a) if not v else set_prop(j, a, v)
head          = lambda a: a[0]
is_zero       = lambda a: a == 0
keys          = lambda a: list(a.keys())
len_range     = lambda a, start=None: range(len(a)) if not start else range(start, len(a))
mul           = lambda a, b: a * b
prop          = lambda a, b: a[b]
replace       = lambda a, b, c: str(a).replace(b, c)
reverse       = lambda a: None if a.reverse() else a
strlen        = lambda a: len(str(a))
values        = lambda a: list(a.values())
arr_to_string = lambda a: list(map(str, a))
surround      = lambda a, b: cat(b, cat(a, b))
if_else       = lambda a, b, c: b if a else c
if_then       = lambda a, b: b if a else None


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
    for x in tuple(itr):
        acc = func(x, acc)
    return acc


def foreach(func, itr):
    for x in itr:
        func(x)
    return itr
