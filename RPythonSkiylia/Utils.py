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

    #fetch the current object, and increment
    def next(self):
        self.current+=1
        return self.source[self.current-1]

    #check if we have reached the end of the object itterables
    def atEnd(self, offset=0):
        if offset:
            return (self.current+offset) >= len(self.source)
        return self.current >= len(self.source)
