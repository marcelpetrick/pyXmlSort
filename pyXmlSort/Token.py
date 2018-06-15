from enum import Enum

class TokenType(Enum):
    UnIdentified = 1
    CnStart = 2
    CnEnd = 3
    CiStart = 4
    CiEnd = 5

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

# todo enum for token-types: how to define this in python?

#----------------------------------------------------------------------------------------------------------------
