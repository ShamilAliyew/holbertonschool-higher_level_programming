#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
       tuple_a += (0,) * (2-len(tuple_a))
    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    return tuple(x + y for x, y in zip(tuple_a, tuple_b))
