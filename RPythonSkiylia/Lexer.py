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
        self.tokens = []
        #keep looping while we have tokens to scan
        while not self.atEnd():
            #fetch the next token
            tok = self.fetchToken()
            if tok:
                self.tokens.append(tok)
            #update our starting position
            self.start = self.current
        #and return the tokens
        return self.tokens

    #fetch the next token by matching with lexical rules
    def fetchToken(self):
        #fetch the next character
        thischar = self.next()
        #dictionary of tokens
        Tokendict = {"(":"LeftParen", ")":"RightParen", ":":"Colon",
                     ",":"Comma", ".":"Dot", "&":"And", "|":"Or", "^":"Xor",
                     #dual (or single) character tokens
                     "-": {"-":"MinusMinus", "":"Minus"},
                     "+": {"+":"PlusPlus", "":"Plus"},
                     "*": {"*":"StarStar", "":"Star"},
                     ">": {"=":"EGreater", "":"Greater"},
                     "<": {"=":"ELess", "":"Less"},
                     "?": {":":"QColon", "?":"QQuestion", "":"Question"},
                     # 'n' character tokens
                     "=": {"=": {"=":"EEEqual", "":"EEqual"}, "":"Equal"},
                     "~": {"~": {"~":"Fuzequal"}, },
                     "!": {"=": {"=": "NEEqual", "":"NEqual"}, "~": {"~": "NFuzequal", }, "":"Not"}, }
        #check if this character matches an entry in the token dict
        if thischar in Tokendict:
            return self.fromdict(Tokendict, thischar)
        elif thischar == " ":
            return

    #fetch the next token if it is in the dictionary supplied
    def fromdict(self, dic, char):
        #fetch the value at the character key
        this = dic.get(char)
        #if that was a dictionary
        while isinstance(this, dict):
            #fetch the next character
            nextchar = self.peek()
            #if the next character is in the child dictionary
            if self.peek() in this:
                #consume the character
                self.next()
                #and fetch the subchild
                this = this.get(nextchar)
            #if it was not, but we have a blank dict
            elif "" in this:
                #return the value of that
                this = this.get("")
        #and return the final value
        return this

lexer = Lexer()
source="print(5 + 4)\0"
toks = lexer.scan(source)
print(toks)
