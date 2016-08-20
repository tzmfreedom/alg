# -*- coding: utf-8 -*-


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LikedArray:
    def __init__(self):
        self.first = None
        self.end = None

    def push(self, value):
        elm = Element(value)
        if self.first is not None:
            self.end.next = elm
            self.end = elm
        else:
            self.first = self.end = elm
            self.first

    def size(self):
        i = 0
        elm = self.first
        while elm is not None:
            i += 1
            elm = elm.next
        return i

    def toString(self):
        arr = []
        elm = self.first
        while elm is not None:
            arr.append(str(elm.value))
            elm = elm.next
        return ','.join(arr)

    def getElm(self, idx):
        elm = self.first
        for i in range(0, idx):
            elm = elm.next
            if elm is None:
                raise Exception('Index Error: MaxIndex {0}, Index {1}'.format(i, idx))
        return elm

    def get(self, idx):
        return self.getElm(idx).value

    def insert(self, idx, value):
        if idx == 0:
            nextElem = self.first
            self.first = Element(value)
            self.first.next = nextElem
            return self.first
        else:
            nextElem = self.getElm(idx)
            elm = self.getElm(idx-1)
            elm.next = Element(value)
            elm.next.next = nextElem
            return elm.next


if __name__ == '__main__':
    arr = LikedArray()
    arr.push(1)
    arr.push('moji')
    arr.push(True)
    arr.push(None)

    print(arr.size())

    print(arr.get(0))
    print(arr.get(1))
    print(arr.get(2))
    print(arr.get(3))

    print(arr.insert(3, 'hoge'))
    print(arr.toString())

    print(arr.get(5))
