# todo load here the lexer, which does also the file reading

from pyXmlSort.Lexer import Lexer # import from python-package has to have the correct prefix! woah

def main():
    #inputFile = "TestData/test0.xml"
    inputFile = "TestData/test1.xml" # the one with real structure
    lexer = Lexer(inputFile)

if __name__ == '__main__':
    main()
