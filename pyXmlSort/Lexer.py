from pyXmlSort.Token import Token
from pyXmlSort.Token import TokenType

# --------------------------------------------------------------------------------------------------------------------

class Lexer:
    ''' task: read the file, remove all whitespace, separate into tokens with identified type '''
    def __init__(self, fileName):
        self.fileName = fileName
        print("Lexer:__init__")

        # this is not truly class-based, because the content could be handed over via members ..
        cleanContent = self.readAndPrepareInput()
        listOfTokens = self.tokenizeString(cleanContent)
        print(listOfTokens)

# --------------------------------------------------------------------------------------------------------------------

    def readAndPrepareInput(self):
        ''' Returns a big concatenated string of input without the whitespace between the items. '''
        cleanString = "" # shall be a string

        with open(self.fileName, "r") as file: # implicit close
            for line in file:
                # remove all kinds of whitespace: newline and tabs with rstrip and lstrip
                # add it to the complete string
                cleanString += line.rstrip().lstrip()

        print("** readAndPrepareInput **")
        print("\t", cleanString)
        return cleanString

# --------------------------------------------------------------------------------------------------------------------

    def tokenizeString(self, inputString):
        ''' Create a list of tokens with the fitting content '''
        print("** tokenizeString **")

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
                    #print("posOpenBrace:", posOpenBrace, fullItem)
                    if posOpenBrace != 0:
                        beginning = fullItem[:posOpenBrace]
                        ending = fullItem[posOpenBrace:]
                        stringTokenList.append(beginning)
                        stringTokenList.append(ending)
                    else:
                        stringTokenList.append(fullItem) # add unaltered
                else:
                    stringTokenList.append(fullItem) # add unaltered

        # just for checking the intermediate result
#        print(splitString)
#        for elem in stringTokenList:
#            print(elem) # just for checking

        # convert the list of strings to a list of tokens
        returnValue = []
        for elem in stringTokenList:
            returnValue.append(self.recognizeToken(elem))

        return returnValue

# --------------------------------------------------------------------------------------------------------------------

    def recognizeToken(self, inputString): #todo may be static
        ''' Recognize and convert the given string to a fitting Token. '''
        #print("** recognizeToken **")
        # form is always <CI> or </CI> - so check at second position for a slash
        # or, even better: check if first four characters contain CI, /CI, CN, /CN ... else unidentified (which means: take over unaltered)
        prefix = inputString[:4]
        print(prefix)

        type = TokenType.UnIdentified
        # check in that order because CN is contained in /CN!
        if "/CN" in prefix:
            type = TokenType.CnEnd
        elif "CN" in prefix:
            type = TokenType.CnEnd
        elif "/CI" in prefix:
            type = TokenType.CnEnd
        elif "CI" in prefix:
            type = TokenType.CnEnd
        elif ((not "<" in inputString) and (not ">" in inputString)):
            type = TokenType.Content # seriously: I have no idea what happens if the content is containing < or > .. I treat this right now as unidentified

        return Token(type, inputString)

# --------------------------------------------------------------------------------------------------------------------
