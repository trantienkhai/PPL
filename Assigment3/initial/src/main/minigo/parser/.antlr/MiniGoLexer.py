# Generated from /Users/nhphung/LocalDocuments/fromMacBookAir1/Monhoc/KS-NNLT/Materials/Assignments/MiniGo/Assignment3/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,17,98,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,
        8,1,8,1,9,4,9,62,8,9,11,9,12,9,63,1,10,4,10,67,8,10,11,10,12,10,
        68,1,11,4,11,72,8,11,11,11,12,11,73,1,11,1,11,4,11,78,8,11,11,11,
        12,11,79,1,12,1,12,1,12,1,12,1,13,4,13,87,8,13,11,13,12,13,88,1,
        13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,0,0,17,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,
        17,1,0,3,1,0,97,122,1,0,48,57,3,0,9,9,13,13,32,32,102,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,
        33,1,0,0,0,1,35,1,0,0,0,3,39,1,0,0,0,5,43,1,0,0,0,7,45,1,0,0,0,9,
        47,1,0,0,0,11,52,1,0,0,0,13,54,1,0,0,0,15,56,1,0,0,0,17,58,1,0,0,
        0,19,61,1,0,0,0,21,66,1,0,0,0,23,71,1,0,0,0,25,81,1,0,0,0,27,86,
        1,0,0,0,29,92,1,0,0,0,31,94,1,0,0,0,33,96,1,0,0,0,35,36,5,118,0,
        0,36,37,5,97,0,0,37,38,5,114,0,0,38,2,1,0,0,0,39,40,5,105,0,0,40,
        41,5,110,0,0,41,42,5,116,0,0,42,4,1,0,0,0,43,44,5,61,0,0,44,6,1,
        0,0,0,45,46,5,59,0,0,46,8,1,0,0,0,47,48,5,102,0,0,48,49,5,117,0,
        0,49,50,5,110,0,0,50,51,5,99,0,0,51,10,1,0,0,0,52,53,5,40,0,0,53,
        12,1,0,0,0,54,55,5,41,0,0,55,14,1,0,0,0,56,57,5,123,0,0,57,16,1,
        0,0,0,58,59,5,125,0,0,59,18,1,0,0,0,60,62,7,0,0,0,61,60,1,0,0,0,
        62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,20,1,0,0,0,65,67,7,
        1,0,0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        22,1,0,0,0,70,72,7,1,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,
        0,73,74,1,0,0,0,74,75,1,0,0,0,75,77,5,46,0,0,76,78,7,1,0,0,77,76,
        1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,24,1,0,0,0,
        81,82,5,10,0,0,82,83,1,0,0,0,83,84,6,12,0,0,84,26,1,0,0,0,85,87,
        7,2,0,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,90,1,0,0,0,90,91,6,13,0,0,91,28,1,0,0,0,92,93,9,0,0,0,93,30,1,
        0,0,0,94,95,9,0,0,0,95,32,1,0,0,0,96,97,9,0,0,0,97,34,1,0,0,0,6,
        0,63,68,73,79,88,1,6,0,0
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    ID = 10
    INTLIT = 11
    FLOATLIT = 12
    NL = 13
    WS = 14
    ERROR_CHAR = 15
    ILLEGAL_ESCAPE = 16
    UNCLOSE_STRING = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'int'", "'='", "';'", "'func'", "'('", "')'", "'{'", 
            "'}'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "ID", "INTLIT", "FLOATLIT", "NL", "WS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


