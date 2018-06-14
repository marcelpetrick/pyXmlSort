# Lexer.py

class Lexer:
    def __init__(self, fileName):
        self.fileName = fileName
        print("__init__")
        self.betterRead(self.fileName) # call for a test


    def betterRead(filename):
        with open(filename, "r") as file: # implicit close
            for line in file:
                print(line)