 #!/usr/bin/env python
"""Utility functions and classes shared between modules"""

#calss needed tp scan itterables
class Scan:
    def __init__(self, source):
        #fetch the source itterables
        self.source = list(source)
        #and set the pointer
        self.current = 0

    def peek(self):
        return self.source[self.current]

    def advance(self):
        if not self.atEnd():
            self.current+=1
            return self.source[self.current-1]
        raise EOFError("Reached end of source")

    def atEnd(self):
        return self.current >= len(self.source)
