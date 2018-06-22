from pyXmlSort.Token import Token
from pyXmlSort.Token import TokenType
import unittest

class Parser:
    def __init__(self, tokenList = []):
        print("Parser::__init__")

        self.tokenList = [] # funny: in case it would not initialize with param, then the member does not exist -> problem with UnitTest for "empty" Parser

        if tokenList.__len__() != 0:
            self.tokenList = tokenList
            # just for checking the current state
            self.printTokenList()
        else:
            print("ERROR: missing input tokens!")

        # ----- static part
        self.stack = [] # TODO stack or better a list? should not matter

    def printTokenList(self):
        print("Parser::printTokenList")
        for elem in self.tokenList:
            print("\t", elem)
        print("-> %i items" % self.tokenList.__len__())

    def processTokenList(self):
        '''
        Ok, the parser should read the input from the tokenList as long as there is content:
        * grab one item, put it to the stack (or whatever structure)
        * then check if the last items (here: top) are reducible via one rule
        ** rule could be: last touched elem was CnEnd
        ** then apply the rule (in that example: find the fitting first CnStart; then sort all elements between End and Start; then write them all back as 'content'-item (to be discussed)
        * do this until the tokenList is empty (last applied rule should be something like: items on stack are [Content, XmlHeader] - if this is a rule at all)
        ** as aforementioned: tokenList.empty() shall be accompanied by that situation on the stack

        :return: nothing right now
        '''
        pass

    def isValidState(self):
        ''' Used to check if the current state (based on the tokenList and the stack) is valid and process-able. '''
        returnValue = False

        if (self.tokenList.__len__() == 0 and self.stack.__len__() == 0):
            returnValue = True
        print("Parser::isValidState: returnValue will be:", returnValue)
        return returnValue

#------------------------------------------------------------------------------

class ParserTestCase(unittest.TestCase):
    '''
    Unit-testing: from easy to heavy .. at least this is the plan
    '''

    def testParserEmpty(self):
        parser = Parser()
        self.assertTrue(parser.isValidState())

    def testParserMini(self):
        inputTokenList = [Token(TokenType.XmlHeader, "header"), Token(TokenType.Content, "content")]
        parser = Parser(inputTokenList)

        self.assertFalse(parser.isValidState())

#------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
