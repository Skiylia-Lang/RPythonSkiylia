 #!/usr/bin/env python
"""Generates a sequence of tokens from plaintext"""

class Lexer:
    def __init__(self):
        #set the position elements to 1 at start
        self.line = self.char = 1
        #set the lexer elements to 0 at start
        self.start = self.current = self.indent = 0

    def scan(self, source):
        while True:
            #create an iterable of the remaining source code
            remaining = iter(source[self.start:])
            #fetch the next token
            self.fetchToken(remaining)
            self.start = self.current

    def fetchToken(self, source):
        thischar = next(source)
        self.current+=1
        print(thischar)

lexer = Lexer()
source="print(5 + 4)\0"
lexer.scan(source)
