 #!/usr/bin/env python
"""Utility functions and classes shared between modules"""

#calss needed tp scan itterables
class Scan:
    def __init__(self, source):
        #fetch the source itterables
        self.source = list(source)
        #and set the pointer
        self.current = 0

    #fetch the current object
    def peek(self, offset=0):
        if offset and not self.atEnd(offset):
            return self.source[self.current+offset]
        return self.source[self.current]

    #check if the next object matches an expectation, and increment if it does
    def match(self, obj):
        if self.peek() == obj:
            self.current+=1
            return True
        return False

    def matchmul(self, *objs):
        if self.group(self.current + len(objs)) == list(objs):
            self.current+=len(objs)
            return True
        return False

    #fetch the current object, and increment
    def next(self):
        self.current+=1
        return self.source[self.current-1]

    #fetch the objects between two indices as a list
    def group(self, idxa, idxb=""):
        #if we are only given one index
        if not idxb:
            #then use the current pointer location
            idxb=self.current
            #if the given index is larger than the current
            if (idxa > idxb):
                #then return from the current to that index
                return self.source[idxb : idxa]
        #else return between the two
        return self.source[idxa : idxb]

    #fetch the objects between two indices, but as a string
    def joined(self, idxa, idxb=""):
        return "".join(self.group(idxa, idxb))

    #check if we have reached the end of the object itterables
    def atEnd(self, offset=0):
        if offset:
            return (self.current+offset) >= len(self.source)
        return self.current >= len(self.source)
