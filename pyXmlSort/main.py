# todo load here the lexer, which does also the file reading

from pyXmlSort.Lexer import Lexer # import from python-package has to have the correct prefix! woah
from pyXmlSort.Parser import Parser

def main():
    #inputFile = "TestData/test0.xml"
    #inputFile = "TestData/test1.xml" # the one with real structure
    inputFile = "TestData/test2.xml"  # super simple structure, but has header
    lexer = Lexer(inputFile)
# ---------------------
    # for checking the intermediate result, print the current state of the tokens
    print("########## print the current state of the tokens after lexing ##########")
    for elem in lexer.getTokenList():
        print(elem)
#---------------------
    parser = Parser(lexer.getTokenList())


if __name__ == '__main__':
    main()
