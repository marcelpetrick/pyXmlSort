from pyXmlSort.Token import Token
from pyXmlSort.Token import TokenType

class Parser:
    def __init__(self, tokenList = []):
        print("Parser::__init__")
        if tokenList.__len__() != 0:
            self.tokenList = tokenList
            print(self.tokenList)
        else:
            print("ERROR: missing input tokens!")

