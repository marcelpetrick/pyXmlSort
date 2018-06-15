# Lexer.py

from pyXmlSort.Token import Token

class Lexer:
    ''' task: read the file, remove all whitespace, separate into tokens with identified type '''
    def __init__(self, fileName):
        self.fileName = fileName
        print("Lexer:__init__")

        self.printInputFile()

    def printInputFile(self):
        with open(self.fileName, "r") as file: # implicit close
            for line in file:
                print(line)
                current = Token("cn", line)

