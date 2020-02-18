from functions import head, keys, values, foreach, reduce, strlen, append
from functions import cat, mul, len_range, surround as surr

TLC = u'\u250C' # ┌
TRC = u'\u2510' # ┐
BLC = u'\u2514' # └
BRC = u'\u2518' # ┘
HSL = u'\u2500' # ─
VSL = u'\u2502' # │
LRU = u'\u2534' # ┴
LRD = u'\u252C' # ┬
UDR = u'\u251C' # ├
UDL = u'\u2524' # ┤
CRS = u'\u253C' # ┼


class Table():
    def __init__(self, data, title=None, margin=0):
        col_heads    = keys(head(data))
        get_values   = lambda a: values(a)
        table_values = map(get_values, data)
        append_table = lambda a: append(self._values, a)
        self._values = [col_heads]
        self._title  = title
        self._margin = margin

        foreach(append_table, table_values)

        self._max   = self._get_max_col_len()
        self._width = self._get_width()

    def _get_max_col_len(self):
        max_len = lambda a, b: strlen(a) if strlen(a) > b else b
        get_val = lambda i: list(j[i] for j in self._values)
        get_max = lambda i: reduce(max_len, get_val(i), 0)
        tbl_rng = len_range(head(self._values))

        return list(map(get_max, tbl_rng))

    def _get_width(self):
        return reduce(lambda a, b: b + a + 3, self._max, 1)

    def _sep_border(self, sep, ls, rs):
        left  = cat(mul(' ',  self._margin), ls)
        right = cat('\b', rs)
        cell  = lambda a: cat(mul(HSL, a + 2), sep)

        return cat(reduce(lambda a, b: cat(b, cell(a)), self._max, left), right)

    def _print_title(self):
        out       = self._width - 2
        ttl       = len(self._title)
        pad       = (out - ttl) // 2
        rem       = out - pad - ttl
        left_pad  = cat(cat(mul(' ', self._margin), VSL), mul(' ', pad))
        right_pad = cat(mul(' ', rem), VSL)
        ttl_cell  = cat(left_pad, cat(self._title, right_pad))

        print(self._sep_border(HSL, TLC, TRC)) # Top Border
        print(ttl_cell)                        # Title
        print(self._sep_border(LRD, UDR, UDL)) # Separator

    def print(self):
        rows      = len_range(self._values, start=1)
        val_rng   = lambda a: len_range(self._values[a])
        val       = lambda a, b: self._values[a][b]
        rem_spc   = lambda a, b: self._max[b] - len(str(a))
        cell      = lambda a, b: surr(cat(str(val(a, b)), mul(' ', rem_spc(val(a, b), b))), ' ')
        add_cell  = lambda a: lambda b, c: cat(c, cat(cell(a, b), VSL))
        print_row = lambda a: print(reduce(add_cell(a), val_rng(a), cat(mul(' ', self._margin), VSL)))

        if self._title: self._print_title()    # Table Title (Optional)

        print_row(0)                           # Column Header
        print(self._sep_border(CRS, UDR, UDL)) # Seperator
        foreach(print_row, rows)               # Table Values
        print(self._sep_border(LRU, BLC, BRC)) # Bottom Border
