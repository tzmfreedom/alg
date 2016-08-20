#!/usr/bin/env python

REPEATED = 'REPEATED'
NON_REPEATED = 'NON_REPEATED'


class Permutation(object):

    def __init__(self, arr, mode=REPEATED, length=None):
        self.out_array = []
        self.length = len(arr) if length is None else length
        buf = [None] * self.length
        if mode == REPEATED:
            self.pick_elem_repeated(buf, arr, 0)
        else:
            self.pick_elem_non_repeated(buf, arr, 0)

    def get_array(self):
        return self.out_array

    def pick_elem_non_repeated(self, buf, arr, n):
        if self.length == n:
            self.out_array.append(''.join(buf))
        else:
            for elem in arr:
                new_arr = arr[:]
                new_arr.remove(elem)
                buf[n] = elem
                self.pick_elem_non_repeated(buf, new_arr, n+1)

    def pick_elem_repeated(self, buf, arr, n):
        if self.length == n:
            self.out_array.append(''.join(buf))
        else:
            for elem in arr:
                buf[n] = elem
                self.pick_elem_repeated(buf, arr, n+1)

if __name__ == '__main__':
    arr = ['a', 'b', 'c']
    p = Permutation(arr, length=1)
    print(p.get_array())
    p = Permutation(arr, length=2)
    print(p.get_array())
    p = Permutation(arr, length=3)
    print(p.get_array())
    p = Permutation(arr)
    print(p.get_array())

    p = Permutation(arr, NON_REPEATED, 1)
    print(p.get_array())
    p = Permutation(arr, NON_REPEATED, 2)
    print(p.get_array())
    p = Permutation(arr, NON_REPEATED, 3)
    print(p.get_array())
    p = Permutation(arr, NON_REPEATED)
    print(p.get_array())
