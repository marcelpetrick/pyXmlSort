# Lexer.py

from pyXmlSort.Token import Token
#import String

class Lexer:
    ''' task: read the file, remove all whitespace, separate into tokens with identified type '''
    def __init__(self, fileName):
        self.fileName = fileName
        print("Lexer:__init__")

        #self.printInputFile()

        # this is not truly class-based, because the content could be handed over via members ..
        cleanContent = self.readAndPrepareInput()
        listOfTokens = self.tokenizeString(cleanContent)
        print(listOfTokens)

#--------------------------------------------------------------------------------------------------------------------

    def printInputFile(self):
        ''' Print content of the given file. '''
        with open(self.fileName, "r") as file: # implicit close
            for line in file:
                print(line)


# --------------------------------------------------------------------------------------------------------------------

    def readAndPrepareInput(self):
        ''' Returns a big concatenated string of input without the whitespace between the items. '''
        cleanString = "" # shall be a string

        with open(self.fileName, "r") as file: # implicit close
            for line in file:
                # remove all kinds of whitespace: newline and tabs
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                line = line.replace("\t", "")

                # add it to the complete string
                print(line)
                cleanString += line

                #current = Token("cn", line)

        print(cleanString)
        return cleanString

# --------------------------------------------------------------------------------------------------------------------

    def tokenizeString(self, inputString):
        ''' Create a list of tokens with the fitting content '''

        returnValue = [Token(), Token()]
        return returnValue
