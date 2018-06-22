from pyXmlSort.Token import Token
from pyXmlSort.Token import TokenType

class Parser:
    def __init__(self, tokenList = []):
        print("Parser::__init__")
        if tokenList.__len__() != 0:
            self.tokenList = tokenList
            # just for checking the current state
            self.printTokenList()
        else:
            print("ERROR: missing input tokens!")

    def printTokenList(self):
        print("Parser::printTokenList")
        for elem in self.tokenList:
            print("\t", elem)
        print("-> %i items" % self.tokenList.__len__())

    def processTokenList(self):
        pass
