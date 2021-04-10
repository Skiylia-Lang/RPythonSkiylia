 #!/usr/bin/env python
"""Generates a sequence of tokens from plaintext"""

import Utils

class Lexer(Utils.Scan):
    def __init__(self):
        #set the position elements to 1 at start
        self.line = self.char = 1
        #set the lexer elements to 0 at start
        self.start = self.indent = 0
        #dictionary of tokens
        self.Tokendict = {"(":"LeftParen", ")":"RightParen", ":":"Colon",
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
        #set of all keywords
        self.keywordset = {"and", "break", "continue", "class", "def", "do", "elif", "else", "false", "for", "if", "import", "in",
                           "not", "null", "or", "return", "self", "super", "true", "var", "where", "while", "xor", }
        #with a special dictionary if certain keywords need to map to something else
        self.keywordmap = {"when": "where", }

    def scan(self, source):
        #initialise the Utils.scan
        super().__init__(source)
        self.tokens = []
        #keep looping while we have tokens to scan
        while not self.atEnd():
            #fetch the next token
            tok = self.fetchToken()
            #if we returned a token
            if tok:
                #add it to our token list
                self.tokens.append(tok)
            #update our starting position
            self.start = self.current
        #and return the tokens
        return self.tokens

    #fetch the next token by matching with lexical rules
    def fetchToken(self):
        #fetch the next character
        thischar = self.next()
        #check if this character matches an entry in the token dict
        if thischar in self.Tokendict:
            return self.fromdict(thischar), thischar
        #check for comments (they need slightly different logic)
        elif thischar == "/":
            if self.match("/"):
                #check for '///' in a row
                if self.match("/"):
                    #keep incrementing until we meet another '///' cluster
                    while not self.matchmul("/","/","/"):
                        self.next()
                #else, we only had '//'
                else:
                    #keep incrementing until we meet a line break
                    while not match("\n"):
                        self.next()
                #and return the comment as an ignorable token I guess
                return "Comment", self.joined(self.start)
            #otherwise, we just have division
            else:
                return "Slash", thischar
        #otherwise, check for numbers / identifiers
        else:
            if self.numeric(thischar):
                return "Number", self.asnumber()
            elif self.alpha(thischar):
                return "Identifier", self.asidentifier()
            return

    def asnumber(self):
        while self.numeric(self.peek()):
            self.next()
        if self.match("."):
            while self.numeric(self.peek()):
                self.next()
        return self.joined(self.start)

    def asidentifier(self):
        while self.alphanumeric(self.peek()):
            self.next()
        ident = self.joined(self.start)
        if ident in self.keywordset:
            ident = ident.capitalize()
        elif ident in self.keywordmap:
            ident = self.keywordmap.get(ident).capitalize()
        return ident

    def numeric(self, char):
        return "0" <= char <= "9"

    def alpha(self, char):
        return ("a" <= char <= "z") or ("A" <= char <= "Z") or char == "_"

    def alphanumeric(self, char):
        return ("0" <= char <= "9") or ("a" <= char <= "z") or ("A" <= char <= "Z") or char == "_"

    #fetch the next token if it is in the dictionary supplied
    def fromdict(self, char):
        #fetch the value at the character key
        this = self.Tokendict.get(char)
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
source="///this is a test///print(5 + 4 and 3 when x > 1)\0"
toks = lexer.scan(source)
print(toks)
