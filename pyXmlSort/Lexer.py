# Lexer.py

class Lexer:
    def __init__(self, fileName):
        self.fileName = fileName
        print("Lexer:__init__")

        self.printInputFile()

    def printInputFile(self):
        with open(self.fileName, "r") as file: # implicit close
            for line in file:
                print(line)