from enum import Enum

class TokenType(Enum):
    '''
    CnStart needs CnEnd
    CiStart needs CiEnd
    Header is really the XML-header (should always be the very first line; will also be reduced with CN to "nothing"
    Content is anything as string between CI or CN-tags
    UnIdentified better does never happen!
    '''
    UnIdentified = 1 # todo check of the manual numbering is really needed
    CnStart = 2
    CnEnd = 3
    CiStart = 4
    CiEnd = 5
    Content = 6
    XmlHeader = 7

#----------------------------------------------------------------------------------------------------------------

class Token:
    def __init__(self, type = TokenType.UnIdentified, content = ""):
        self.__type__ = type # initially none
        self.__content__ = content # initially empty

    def __repr__(self):
        return "(%s, %s)" % (self.__type__, self.__content__)

    def getType(self):
        return self.__type__

    def setType(self, type):
        self.__type__ = type

    # todo maybe add for content something similar

#----------------------------------------------------------------------------------------------------------------
