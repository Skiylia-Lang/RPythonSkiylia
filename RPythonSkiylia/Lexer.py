 #!/usr/bin/env python
"""Generates a sequence of tokens from plaintext"""

import Utils

class Lexer(Utils.Scan):
    def __init__(self):
        #set the position elements to 1 at start
        self.line = self.char = 1
        #set the lexer elements to 0 at start
        self.current = self.indent = 0

    def scan(self, source):
        #initialise the Utils.scan
        super().__init__(source)
        while not self.atEnd():
            #fetch the next token
            self.fetchToken()
            #update our starting position
            self.start = self.current

    def fetchToken(self):
        thischar = self.next()
        print(thischar)

lexer = Lexer()
source="print(5 + 4)\0"
lexer.scan(source)
