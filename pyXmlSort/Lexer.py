# Lexer.py

from pyXmlSort.Token import Token
import re # for the regexp-splitting

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
                # todo replace with lstrip, rstrip

                # add it to the complete string
                #print(line)
                cleanString += line

                #current = Token("cn", line)

        print("** readAndPrepareInput **")
        print("\t", cleanString)
        return cleanString

# --------------------------------------------------------------------------------------------------------------------

    def tokenizeString(self, inputString):
        ''' Create a list of tokens with the fitting content '''
        print("** tokenizeString **")

        returnValue = [Token(), Token()] # todo fix this

        splitString = inputString.split(">")
        stringTokenList = []
        # splitting like this removed also the closing >: so add it back to each element
        for elem in splitString:
            # just handle non-empty strings
            if elem != "":
                fullItem = elem + ">"
                # in case there is something like "true</CI>" then it has to be split too, before appending
                if fullItem.__contains__("<"):
                    posOpenBrace = fullItem.index("<")
                    print("posOpenBrace:", posOpenBrace, fullItem)
                    # todo continue
                    if posOpenBrace != 0:
                        beginning = fullItem[:posOpenBrace]
                        ending = fullItem[posOpenBrace:]
                        stringTokenList.append(beginning)
                        stringTokenList.append(ending)
                    else:
                        stringTokenList.append(fullItem)
                else:
                    stringTokenList.append(fullItem)

        #splitString = re.split("(>)", inputString)
        print(splitString)
        for elem in stringTokenList:
            print(elem) # just for checking

        return returnValue

# --------------------------------------------------------------------------------------------------------------------
    # todo should be static ..
    def cutToken(self, input):
        ''' Returns token string and remaining string.'''

        openBraceIndex = input.index("<")
        closeBraceIndex = input.index(">")

        # todo throw token-exception in case of openIndex >= closeIndex

        if closeBraceIndex > openBraceIndex:
            print("found correct indexes", openBraceIndex, closeBraceIndex)


