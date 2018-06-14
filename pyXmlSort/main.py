# todo load here the lexer, which does also the file reading

from pyXmlSort.Lexer import Lexer
# import from same directory has to be prefaced with .

def main():
    inputFile = "foo.xml"
    lexer = Lexer(inputFile)
    # lexer.printTokens()

if __name__ == '__main__':
    main()
