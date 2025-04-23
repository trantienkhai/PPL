# Generated from c:/Users/trant/OneDrive/Desktop/PPL/PPL/Assigment1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,76,525,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,1,0,5,0,102,8,0,10,0,12,0,105,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,122,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,133,8,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,143,8,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,157,8,5,1,6,1,6,1,6,4,6,162,8,6,11,6,
        12,6,163,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,4,8,175,8,8,11,8,12,
        8,176,1,8,1,8,1,9,1,9,1,9,3,9,184,8,9,1,9,1,9,3,9,188,8,9,1,9,1,
        9,1,10,1,10,1,10,5,10,195,8,10,10,10,12,10,198,9,10,1,11,1,11,1,
        11,5,11,203,8,11,10,11,12,11,206,9,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,3,12,215,8,12,1,12,1,12,3,12,219,8,12,1,12,1,12,1,12,3,12,
        224,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,235,8,
        13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,245,8,14,1,14,1,
        14,3,14,249,8,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,258,8,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,5,17,275,8,17,10,17,12,17,278,9,17,1,17,1,17,1,17,1,17,
        1,17,3,17,285,8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,3,19,312,8,19,1,20,1,20,1,20,3,20,317,8,20,1,20,1,
        20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,330,8,22,1,
        23,1,23,1,23,3,23,335,8,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,25,3,25,346,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,3,25,358,8,25,1,26,1,26,1,27,1,27,1,28,1,28,1,28,3,28,367,
        8,28,1,29,1,29,1,29,3,29,372,8,29,1,29,1,29,1,30,1,30,1,31,1,31,
        3,31,380,8,31,1,32,1,32,1,32,5,32,385,8,32,10,32,12,32,388,9,32,
        1,32,1,32,1,33,1,33,1,33,5,33,395,8,33,10,33,12,33,398,9,33,1,34,
        1,34,1,34,1,34,1,34,1,34,5,34,406,8,34,10,34,12,34,409,9,34,1,35,
        1,35,1,35,1,35,1,35,1,35,5,35,417,8,35,10,35,12,35,420,9,35,1,36,
        1,36,1,36,1,36,1,36,1,36,5,36,428,8,36,10,36,12,36,431,9,36,1,37,
        1,37,1,37,1,37,1,37,1,37,5,37,439,8,37,10,37,12,37,442,9,37,1,38,
        1,38,1,38,1,38,1,38,1,38,5,38,450,8,38,10,38,12,38,453,9,38,1,39,
        1,39,1,39,3,39,458,8,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,3,40,469,8,40,1,41,1,41,1,41,1,41,1,41,4,41,476,8,41,11,41,
        12,41,477,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,
        1,43,3,43,492,8,43,1,44,1,44,3,44,496,8,44,1,45,1,45,1,45,1,45,1,
        45,3,45,503,8,45,1,45,1,45,1,46,1,46,1,46,3,46,510,8,46,1,47,1,47,
        1,47,3,47,515,8,47,1,47,1,47,1,48,1,48,3,48,521,8,48,1,49,1,49,1,
        49,0,5,68,70,72,74,76,50,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,88,90,92,94,96,98,0,8,2,0,66,66,71,71,2,0,36,
        40,48,48,1,0,3,15,2,0,41,44,55,56,1,0,50,51,1,0,52,54,2,0,47,47,
        51,51,2,0,33,35,66,68,544,0,103,1,0,0,0,2,108,1,0,0,0,4,121,1,0,
        0,0,6,123,1,0,0,0,8,136,1,0,0,0,10,156,1,0,0,0,12,158,1,0,0,0,14,
        167,1,0,0,0,16,171,1,0,0,0,18,180,1,0,0,0,20,191,1,0,0,0,22,199,
        1,0,0,0,24,223,1,0,0,0,26,234,1,0,0,0,28,236,1,0,0,0,30,253,1,0,
        0,0,32,261,1,0,0,0,34,284,1,0,0,0,36,286,1,0,0,0,38,311,1,0,0,0,
        40,316,1,0,0,0,42,321,1,0,0,0,44,323,1,0,0,0,46,331,1,0,0,0,48,336,
        1,0,0,0,50,357,1,0,0,0,52,359,1,0,0,0,54,361,1,0,0,0,56,366,1,0,
        0,0,58,368,1,0,0,0,60,375,1,0,0,0,62,377,1,0,0,0,64,381,1,0,0,0,
        66,391,1,0,0,0,68,399,1,0,0,0,70,410,1,0,0,0,72,421,1,0,0,0,74,432,
        1,0,0,0,76,443,1,0,0,0,78,457,1,0,0,0,80,468,1,0,0,0,82,470,1,0,
        0,0,84,479,1,0,0,0,86,491,1,0,0,0,88,495,1,0,0,0,90,497,1,0,0,0,
        92,509,1,0,0,0,94,511,1,0,0,0,96,520,1,0,0,0,98,522,1,0,0,0,100,
        102,3,4,2,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,
        104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,0,0,1,107,
        1,1,0,0,0,108,109,5,20,0,0,109,110,5,1,0,0,110,111,5,58,0,0,111,
        112,5,59,0,0,112,113,3,64,32,0,113,114,5,65,0,0,114,3,1,0,0,0,115,
        122,3,6,3,0,116,122,3,8,4,0,117,122,3,10,5,0,118,122,3,24,12,0,119,
        122,3,28,14,0,120,122,3,30,15,0,121,115,1,0,0,0,121,116,1,0,0,0,
        121,117,1,0,0,0,121,118,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,
        122,5,1,0,0,0,123,124,5,29,0,0,124,132,5,71,0,0,125,126,3,26,13,
        0,126,127,5,49,0,0,127,128,3,68,34,0,128,133,1,0,0,0,129,133,3,26,
        13,0,130,131,5,49,0,0,131,133,3,68,34,0,132,125,1,0,0,0,132,129,
        1,0,0,0,132,130,1,0,0,0,133,134,1,0,0,0,134,135,5,65,0,0,135,7,1,
        0,0,0,136,137,5,28,0,0,137,138,5,71,0,0,138,142,5,49,0,0,139,143,
        3,68,34,0,140,143,3,32,16,0,141,143,3,34,17,0,142,139,1,0,0,0,142,
        140,1,0,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,145,5,65,0,0,145,
        9,1,0,0,0,146,147,5,21,0,0,147,148,5,71,0,0,148,149,3,12,6,0,149,
        150,5,65,0,0,150,157,1,0,0,0,151,152,5,21,0,0,152,153,5,71,0,0,153,
        154,3,16,8,0,154,155,5,65,0,0,155,157,1,0,0,0,156,146,1,0,0,0,156,
        151,1,0,0,0,157,11,1,0,0,0,158,159,5,22,0,0,159,161,5,60,0,0,160,
        162,3,14,7,0,161,160,1,0,0,0,162,163,1,0,0,0,163,161,1,0,0,0,163,
        164,1,0,0,0,164,165,1,0,0,0,165,166,5,61,0,0,166,13,1,0,0,0,167,
        168,5,71,0,0,168,169,3,26,13,0,169,170,5,65,0,0,170,15,1,0,0,0,171,
        172,5,23,0,0,172,174,5,60,0,0,173,175,3,18,9,0,174,173,1,0,0,0,175,
        176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,
        179,5,61,0,0,179,17,1,0,0,0,180,181,5,71,0,0,181,183,5,58,0,0,182,
        184,3,20,10,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,
        187,5,59,0,0,186,188,3,26,13,0,187,186,1,0,0,0,187,188,1,0,0,0,188,
        189,1,0,0,0,189,190,5,65,0,0,190,19,1,0,0,0,191,196,3,22,11,0,192,
        193,5,64,0,0,193,195,3,22,11,0,194,192,1,0,0,0,195,198,1,0,0,0,196,
        194,1,0,0,0,196,197,1,0,0,0,197,21,1,0,0,0,198,196,1,0,0,0,199,204,
        5,71,0,0,200,201,5,64,0,0,201,203,5,71,0,0,202,200,1,0,0,0,203,206,
        1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,204,
        1,0,0,0,207,208,3,26,13,0,208,23,1,0,0,0,209,224,3,2,1,0,210,211,
        5,20,0,0,211,212,5,71,0,0,212,214,5,58,0,0,213,215,3,20,10,0,214,
        213,1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,216,218,5,59,0,0,217,
        219,3,26,13,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,
        221,3,64,32,0,221,222,5,65,0,0,222,224,1,0,0,0,223,209,1,0,0,0,223,
        210,1,0,0,0,224,25,1,0,0,0,225,235,5,25,0,0,226,235,5,26,0,0,227,
        235,5,27,0,0,228,235,5,24,0,0,229,235,5,71,0,0,230,231,5,62,0,0,
        231,232,7,0,0,0,232,233,5,63,0,0,233,235,3,26,13,0,234,225,1,0,0,
        0,234,226,1,0,0,0,234,227,1,0,0,0,234,228,1,0,0,0,234,229,1,0,0,
        0,234,230,1,0,0,0,235,27,1,0,0,0,236,237,5,20,0,0,237,238,5,58,0,
        0,238,239,5,71,0,0,239,240,5,71,0,0,240,241,5,59,0,0,241,242,5,71,
        0,0,242,244,5,58,0,0,243,245,3,20,10,0,244,243,1,0,0,0,244,245,1,
        0,0,0,245,246,1,0,0,0,246,248,5,59,0,0,247,249,3,26,13,0,248,247,
        1,0,0,0,248,249,1,0,0,0,249,250,1,0,0,0,250,251,3,64,32,0,251,252,
        5,65,0,0,252,29,1,0,0,0,253,254,5,71,0,0,254,257,5,48,0,0,255,258,
        3,32,16,0,256,258,3,34,17,0,257,255,1,0,0,0,257,256,1,0,0,0,258,
        259,1,0,0,0,259,260,5,65,0,0,260,31,1,0,0,0,261,262,5,62,0,0,262,
        263,7,0,0,0,263,264,5,63,0,0,264,265,3,26,13,0,265,266,5,60,0,0,
        266,267,3,66,33,0,267,268,5,61,0,0,268,33,1,0,0,0,269,270,5,71,0,
        0,270,271,5,60,0,0,271,276,3,36,18,0,272,273,5,64,0,0,273,275,3,
        36,18,0,274,272,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,
        1,0,0,0,277,279,1,0,0,0,278,276,1,0,0,0,279,280,5,61,0,0,280,285,
        1,0,0,0,281,282,5,71,0,0,282,283,5,60,0,0,283,285,5,61,0,0,284,269,
        1,0,0,0,284,281,1,0,0,0,285,35,1,0,0,0,286,287,5,71,0,0,287,288,
        5,2,0,0,288,289,3,68,34,0,289,37,1,0,0,0,290,291,3,40,20,0,291,292,
        5,65,0,0,292,312,1,0,0,0,293,294,3,44,22,0,294,295,5,65,0,0,295,
        312,1,0,0,0,296,297,3,48,24,0,297,298,5,65,0,0,298,312,1,0,0,0,299,
        300,3,52,26,0,300,301,5,65,0,0,301,312,1,0,0,0,302,303,3,54,27,0,
        303,304,5,65,0,0,304,312,1,0,0,0,305,306,3,56,28,0,306,307,5,65,
        0,0,307,312,1,0,0,0,308,309,3,62,31,0,309,310,5,65,0,0,310,312,1,
        0,0,0,311,290,1,0,0,0,311,293,1,0,0,0,311,296,1,0,0,0,311,299,1,
        0,0,0,311,302,1,0,0,0,311,305,1,0,0,0,311,308,1,0,0,0,312,39,1,0,
        0,0,313,317,5,71,0,0,314,317,3,82,41,0,315,317,3,84,42,0,316,313,
        1,0,0,0,316,314,1,0,0,0,316,315,1,0,0,0,317,318,1,0,0,0,318,319,
        3,42,21,0,319,320,3,68,34,0,320,41,1,0,0,0,321,322,7,1,0,0,322,43,
        1,0,0,0,323,324,5,16,0,0,324,325,5,58,0,0,325,326,3,68,34,0,326,
        327,5,59,0,0,327,329,3,64,32,0,328,330,3,46,23,0,329,328,1,0,0,0,
        329,330,1,0,0,0,330,45,1,0,0,0,331,334,5,17,0,0,332,335,3,44,22,
        0,333,335,3,64,32,0,334,332,1,0,0,0,334,333,1,0,0,0,335,47,1,0,0,
        0,336,337,5,18,0,0,337,338,3,50,25,0,338,339,3,64,32,0,339,49,1,
        0,0,0,340,358,3,68,34,0,341,346,3,6,3,0,342,343,3,40,20,0,343,344,
        5,65,0,0,344,346,1,0,0,0,345,341,1,0,0,0,345,342,1,0,0,0,346,347,
        1,0,0,0,347,348,3,68,34,0,348,349,5,65,0,0,349,350,3,40,20,0,350,
        358,1,0,0,0,351,352,5,71,0,0,352,353,5,64,0,0,353,354,5,71,0,0,354,
        355,5,48,0,0,355,356,5,32,0,0,356,358,5,71,0,0,357,340,1,0,0,0,357,
        345,1,0,0,0,357,351,1,0,0,0,358,51,1,0,0,0,359,360,5,31,0,0,360,
        53,1,0,0,0,361,362,5,30,0,0,362,55,1,0,0,0,363,367,3,94,47,0,364,
        367,3,90,45,0,365,367,3,58,29,0,366,363,1,0,0,0,366,364,1,0,0,0,
        366,365,1,0,0,0,367,57,1,0,0,0,368,369,3,60,30,0,369,371,5,58,0,
        0,370,372,3,66,33,0,371,370,1,0,0,0,371,372,1,0,0,0,372,373,1,0,
        0,0,373,374,5,59,0,0,374,59,1,0,0,0,375,376,7,2,0,0,376,61,1,0,0,
        0,377,379,5,19,0,0,378,380,3,68,34,0,379,378,1,0,0,0,379,380,1,0,
        0,0,380,63,1,0,0,0,381,386,5,60,0,0,382,385,3,38,19,0,383,385,3,
        4,2,0,384,382,1,0,0,0,384,383,1,0,0,0,385,388,1,0,0,0,386,384,1,
        0,0,0,386,387,1,0,0,0,387,389,1,0,0,0,388,386,1,0,0,0,389,390,5,
        61,0,0,390,65,1,0,0,0,391,396,3,68,34,0,392,393,5,64,0,0,393,395,
        3,68,34,0,394,392,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,
        1,0,0,0,397,67,1,0,0,0,398,396,1,0,0,0,399,400,6,34,-1,0,400,401,
        3,70,35,0,401,407,1,0,0,0,402,403,10,2,0,0,403,404,5,46,0,0,404,
        406,3,70,35,0,405,402,1,0,0,0,406,409,1,0,0,0,407,405,1,0,0,0,407,
        408,1,0,0,0,408,69,1,0,0,0,409,407,1,0,0,0,410,411,6,35,-1,0,411,
        412,3,72,36,0,412,418,1,0,0,0,413,414,10,2,0,0,414,415,5,45,0,0,
        415,417,3,72,36,0,416,413,1,0,0,0,417,420,1,0,0,0,418,416,1,0,0,
        0,418,419,1,0,0,0,419,71,1,0,0,0,420,418,1,0,0,0,421,422,6,36,-1,
        0,422,423,3,74,37,0,423,429,1,0,0,0,424,425,10,2,0,0,425,426,7,3,
        0,0,426,428,3,74,37,0,427,424,1,0,0,0,428,431,1,0,0,0,429,427,1,
        0,0,0,429,430,1,0,0,0,430,73,1,0,0,0,431,429,1,0,0,0,432,433,6,37,
        -1,0,433,434,3,76,38,0,434,440,1,0,0,0,435,436,10,2,0,0,436,437,
        7,4,0,0,437,439,3,76,38,0,438,435,1,0,0,0,439,442,1,0,0,0,440,438,
        1,0,0,0,440,441,1,0,0,0,441,75,1,0,0,0,442,440,1,0,0,0,443,444,6,
        38,-1,0,444,445,3,78,39,0,445,451,1,0,0,0,446,447,10,2,0,0,447,448,
        7,5,0,0,448,450,3,78,39,0,449,446,1,0,0,0,450,453,1,0,0,0,451,449,
        1,0,0,0,451,452,1,0,0,0,452,77,1,0,0,0,453,451,1,0,0,0,454,455,7,
        6,0,0,455,458,3,78,39,0,456,458,3,80,40,0,457,454,1,0,0,0,457,456,
        1,0,0,0,458,79,1,0,0,0,459,469,3,96,48,0,460,469,3,82,41,0,461,469,
        3,84,42,0,462,469,3,90,45,0,463,469,3,94,47,0,464,465,5,58,0,0,465,
        466,3,68,34,0,466,467,5,59,0,0,467,469,1,0,0,0,468,459,1,0,0,0,468,
        460,1,0,0,0,468,461,1,0,0,0,468,462,1,0,0,0,468,463,1,0,0,0,468,
        464,1,0,0,0,469,81,1,0,0,0,470,475,5,71,0,0,471,472,5,62,0,0,472,
        473,3,68,34,0,473,474,5,63,0,0,474,476,1,0,0,0,475,471,1,0,0,0,476,
        477,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,83,1,0,0,0,479,480,
        3,88,44,0,480,481,3,86,43,0,481,85,1,0,0,0,482,483,5,57,0,0,483,
        484,5,71,0,0,484,492,3,86,43,0,485,486,5,62,0,0,486,487,3,68,34,
        0,487,488,5,63,0,0,488,489,3,86,43,0,489,492,1,0,0,0,490,492,1,0,
        0,0,491,482,1,0,0,0,491,485,1,0,0,0,491,490,1,0,0,0,492,87,1,0,0,
        0,493,496,5,71,0,0,494,496,3,94,47,0,495,493,1,0,0,0,495,494,1,0,
        0,0,496,89,1,0,0,0,497,498,3,92,46,0,498,499,5,57,0,0,499,500,5,
        71,0,0,500,502,5,58,0,0,501,503,3,66,33,0,502,501,1,0,0,0,502,503,
        1,0,0,0,503,504,1,0,0,0,504,505,5,59,0,0,505,91,1,0,0,0,506,510,
        5,71,0,0,507,510,3,94,47,0,508,510,3,84,42,0,509,506,1,0,0,0,509,
        507,1,0,0,0,509,508,1,0,0,0,510,93,1,0,0,0,511,512,5,71,0,0,512,
        514,5,58,0,0,513,515,3,66,33,0,514,513,1,0,0,0,514,515,1,0,0,0,515,
        516,1,0,0,0,516,517,5,59,0,0,517,95,1,0,0,0,518,521,3,98,49,0,519,
        521,5,71,0,0,520,518,1,0,0,0,520,519,1,0,0,0,521,97,1,0,0,0,522,
        523,7,7,0,0,523,99,1,0,0,0,46,103,121,132,142,156,163,176,183,187,
        196,204,214,218,223,234,244,248,257,276,284,311,316,329,334,345,
        357,366,371,379,384,386,396,407,418,429,440,451,457,468,477,491,
        495,502,509,514,520
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "':'", "'getInt'", "'putInt'", 
                     "'putIntLn'", "'getFloat'", "'putFloat'", "'putFloatLn'", 
                     "'getBool'", "'putBool'", "'putBoolLn'", "'getString'", 
                     "'putString'", "'putStringLn'", "'putLn'", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'=='", "'!='", "'<='", "'>='", 
                     "'&&'", "'||'", "'!'", "':='", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'<'", "'>'", "'.'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "EQUAL", "NOT_EQUAL", 
                      "LESS_EQUAL", "GREATER_EQUAL", "AND", "OR", "NOT", 
                      "ASSIGN_DECL", "ASSIGN", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "LESS", "GREATER", "DOT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COMMA", "SEMI", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "ID", "WS", "UNCLOSE_STRING", 
                      "NEWLINE", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_main_function = 1
    RULE_declare = 2
    RULE_variable_declaration = 3
    RULE_constant_declaration = 4
    RULE_type_declaration = 5
    RULE_struct_declaration = 6
    RULE_struct_field = 7
    RULE_interface_declaration = 8
    RULE_interface_method = 9
    RULE_parameter_list = 10
    RULE_parameter = 11
    RULE_function_declaration = 12
    RULE_type_specifier = 13
    RULE_method_declare = 14
    RULE_quick_decl = 15
    RULE_arrayLiteral = 16
    RULE_structLiteral = 17
    RULE_structField = 18
    RULE_statement = 19
    RULE_assignment_statement = 20
    RULE_assignment_operator = 21
    RULE_if_statement = 22
    RULE_else_clause = 23
    RULE_for_statement = 24
    RULE_for_condition = 25
    RULE_break_statement = 26
    RULE_continue_statement = 27
    RULE_call_statement = 28
    RULE_builtin_function_call = 29
    RULE_builtin_function_name = 30
    RULE_return_statement = 31
    RULE_block = 32
    RULE_expressionlist = 33
    RULE_expression1 = 34
    RULE_expression2 = 35
    RULE_expression3 = 36
    RULE_expression4 = 37
    RULE_expression5 = 38
    RULE_expression6 = 39
    RULE_expression7 = 40
    RULE_array_access = 41
    RULE_struct_access = 42
    RULE_struct_tail = 43
    RULE_primary1 = 44
    RULE_method_call = 45
    RULE_primary = 46
    RULE_function_call = 47
    RULE_operand = 48
    RULE_literal = 49

    ruleNames =  [ "program", "main_function", "declare", "variable_declaration", 
                   "constant_declaration", "type_declaration", "struct_declaration", 
                   "struct_field", "interface_declaration", "interface_method", 
                   "parameter_list", "parameter", "function_declaration", 
                   "type_specifier", "method_declare", "quick_decl", "arrayLiteral", 
                   "structLiteral", "structField", "statement", "assignment_statement", 
                   "assignment_operator", "if_statement", "else_clause", 
                   "for_statement", "for_condition", "break_statement", 
                   "continue_statement", "call_statement", "builtin_function_call", 
                   "builtin_function_name", "return_statement", "block", 
                   "expressionlist", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "array_access", "struct_access", "struct_tail", "primary1", 
                   "method_call", "primary", "function_call", "operand", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    IF=16
    ELSE=17
    FOR=18
    RETURN=19
    FUNC=20
    TYPE=21
    STRUCT=22
    INTERFACE=23
    STRING=24
    INT=25
    FLOAT=26
    BOOLEAN=27
    CONST=28
    VAR=29
    CONTINUE=30
    BREAK=31
    RANGE=32
    NIL=33
    TRUE=34
    FALSE=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    EQUAL=41
    NOT_EQUAL=42
    LESS_EQUAL=43
    GREATER_EQUAL=44
    AND=45
    OR=46
    NOT=47
    ASSIGN_DECL=48
    ASSIGN=49
    PLUS=50
    MINUS=51
    MULT=52
    DIV=53
    MOD=54
    LESS=55
    GREATER=56
    DOT=57
    LPAREN=58
    RPAREN=59
    LBRACE=60
    RBRACE=61
    LBRACK=62
    RBRACK=63
    COMMA=64
    SEMI=65
    INTLIT=66
    FLOATLIT=67
    STRINGLIT=68
    LINE_COMMENT=69
    BLOCK_COMMENT=70
    ID=71
    WS=72
    UNCLOSE_STRING=73
    NEWLINE=74
    ILLEGAL_ESCAPE=75
    ERROR_CHAR=76

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclareContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclareContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & 2251799813686019) != 0):
                self.state = 100
                self.declare()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_main_function




    def main_function(self):

        localctx = MiniGoParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MiniGoParser.FUNC)
            self.state = 109
            self.match(MiniGoParser.T__0)
            self.state = 110
            self.match(MiniGoParser.LPAREN)
            self.state = 111
            self.match(MiniGoParser.RPAREN)
            self.state = 112
            self.block()
            self.state = 113
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declarationContext,0)


        def constant_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Constant_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declarationContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declareContext,0)


        def quick_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Quick_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declare




    def declare(self):

        localctx = MiniGoParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.constant_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.type_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.function_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.method_declare()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.quick_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_declaration




    def variable_declaration(self):

        localctx = MiniGoParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniGoParser.VAR)
            self.state = 124
            self.match(MiniGoParser.ID)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 125
                self.type_specifier()
                self.state = 126
                self.match(MiniGoParser.ASSIGN)
                self.state = 127
                self.expression1(0)
                pass

            elif la_ == 2:
                self.state = 129
                self.type_specifier()
                pass

            elif la_ == 3:
                self.state = 130
                self.match(MiniGoParser.ASSIGN)
                self.state = 131
                self.expression1(0)
                pass


            self.state = 134
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def structLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constant_declaration




    def constant_declaration(self):

        localctx = MiniGoParser.Constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MiniGoParser.CONST)
            self.state = 137
            self.match(MiniGoParser.ID)
            self.state = 138
            self.match(MiniGoParser.ASSIGN)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 139
                self.expression1(0)
                pass

            elif la_ == 2:
                self.state = 140
                self.arrayLiteral()
                pass

            elif la_ == 3:
                self.state = 141
                self.structLiteral()
                pass


            self.state = 144
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declarationContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def interface_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_declaration




    def type_declaration(self):

        localctx = MiniGoParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_declaration)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MiniGoParser.TYPE)
                self.state = 147
                self.match(MiniGoParser.ID)
                self.state = 148
                self.struct_declaration()
                self.state = 149
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(MiniGoParser.TYPE)
                self.state = 152
                self.match(MiniGoParser.ID)
                self.state = 153
                self.interface_declaration()
                self.state = 154
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declaration




    def struct_declaration(self):

        localctx = MiniGoParser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_struct_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MiniGoParser.STRUCT)
            self.state = 159
            self.match(MiniGoParser.LBRACE)
            self.state = 161 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 160
                self.struct_field()
                self.state = 163 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==71):
                    break

            self.state = 165
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MiniGoParser.ID)
            self.state = 168
            self.type_specifier()
            self.state = 169
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def interface_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_methodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declaration




    def interface_declaration(self):

        localctx = MiniGoParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interface_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MiniGoParser.INTERFACE)
            self.state = 172
            self.match(MiniGoParser.LBRACE)
            self.state = 174 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self.interface_method()
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==71):
                    break

            self.state = 178
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MiniGoParser.ID)
            self.state = 181
            self.match(MiniGoParser.LPAREN)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 182
                self.parameter_list()


            self.state = 185
            self.match(MiniGoParser.RPAREN)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 141012366262287) != 0):
                self.state = 186
                self.type_specifier()


            self.state = 189
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter_list




    def parameter_list(self):

        localctx = MiniGoParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.parameter()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==64:
                self.state = 192
                self.match(MiniGoParser.COMMA)
                self.state = 193
                self.parameter()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MiniGoParser.ID)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==64:
                self.state = 200
                self.match(MiniGoParser.COMMA)
                self.state = 201
                self.match(MiniGoParser.ID)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.type_specifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_function(self):
            return self.getTypedRuleContext(MiniGoParser.Main_functionContext,0)


        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declaration




    def function_declaration(self):

        localctx = MiniGoParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.main_function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(MiniGoParser.FUNC)
                self.state = 211
                self.match(MiniGoParser.ID)
                self.state = 212
                self.match(MiniGoParser.LPAREN)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==71:
                    self.state = 213
                    self.parameter_list()


                self.state = 216
                self.match(MiniGoParser.RPAREN)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 141012366262287) != 0):
                    self.state = 217
                    self.type_specifier()


                self.state = 220
                self.block()
                self.state = 221
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_specifier




    def type_specifier(self):

        localctx = MiniGoParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(MiniGoParser.INT)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.match(MiniGoParser.STRING)
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.match(MiniGoParser.ID)
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.match(MiniGoParser.LBRACK)
                self.state = 231
                _la = self._input.LA(1)
                if not(_la==66 or _la==71):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.match(MiniGoParser.RBRACK)
                self.state = 233
                self.type_specifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_listContext,0)


        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declare




    def method_declare(self):

        localctx = MiniGoParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MiniGoParser.FUNC)
            self.state = 237
            self.match(MiniGoParser.LPAREN)
            self.state = 238
            self.match(MiniGoParser.ID)
            self.state = 239
            self.match(MiniGoParser.ID)
            self.state = 240
            self.match(MiniGoParser.RPAREN)
            self.state = 241
            self.match(MiniGoParser.ID)
            self.state = 242
            self.match(MiniGoParser.LPAREN)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 243
                self.parameter_list()


            self.state = 246
            self.match(MiniGoParser.RPAREN)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 141012366262287) != 0):
                self.state = 247
                self.type_specifier()


            self.state = 250
            self.block()
            self.state = 251
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Quick_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN_DECL(self):
            return self.getToken(MiniGoParser.ASSIGN_DECL, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def structLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_quick_decl




    def quick_decl(self):

        localctx = MiniGoParser.Quick_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_quick_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MiniGoParser.ID)
            self.state = 254
            self.match(MiniGoParser.ASSIGN_DECL)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.state = 255
                self.arrayLiteral()
                pass
            elif token in [71]:
                self.state = 256
                self.structLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 259
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Type_specifierContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLiteral




    def arrayLiteral(self):

        localctx = MiniGoParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MiniGoParser.LBRACK)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==66 or _la==71):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 263
            self.match(MiniGoParser.RBRACK)
            self.state = 264
            self.type_specifier()
            self.state = 265
            self.match(MiniGoParser.LBRACE)
            self.state = 266
            self.expressionlist()
            self.state = 267
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def structField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structLiteral




    def structLiteral(self):

        localctx = MiniGoParser.StructLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_structLiteral)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(MiniGoParser.ID)
                self.state = 270
                self.match(MiniGoParser.LBRACE)
                self.state = 271
                self.structField()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 272
                    self.match(MiniGoParser.COMMA)
                    self.state = 273
                    self.structField()
                    self.state = 278
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 279
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(MiniGoParser.ID)
                self.state = 282
                self.match(MiniGoParser.LBRACE)
                self.state = 283
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structField




    def structField(self):

        localctx = MiniGoParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MiniGoParser.ID)
            self.state = 287
            self.match(MiniGoParser.T__1)
            self.state = 288
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.assignment_statement()
                self.state = 291
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.if_statement()
                self.state = 294
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.for_statement()
                self.state = 297
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.break_statement()
                self.state = 300
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 302
                self.continue_statement()
                self.state = 303
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 305
                self.call_statement()
                self.state = 306
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 308
                self.return_statement()
                self.state = 309
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = MiniGoParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 313
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 314
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 315
                self.struct_access()
                pass


            self.state = 318
            self.assignment_operator()
            self.state = 319
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_DECL(self):
            return self.getToken(MiniGoParser.ASSIGN_DECL, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_operator




    def assignment_operator(self):

        localctx = MiniGoParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 283605280489472) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.IF)
            self.state = 324
            self.match(MiniGoParser.LPAREN)
            self.state = 325
            self.expression1(0)
            self.state = 326
            self.match(MiniGoParser.RPAREN)
            self.state = 327
            self.block()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 328
                self.else_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_clause




    def else_clause(self):

        localctx = MiniGoParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.ELSE)
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 332
                self.if_statement()
                pass
            elif token in [60]:
                self.state = 333
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def for_condition(self):
            return self.getTypedRuleContext(MiniGoParser.For_conditionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.FOR)
            self.state = 337
            self.for_condition()
            self.state = 338
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def assignment_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_statementContext,i)


        def variable_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declarationContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGN_DECL(self):
            return self.getToken(MiniGoParser.ASSIGN_DECL, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_condition




    def for_condition(self):

        localctx = MiniGoParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_condition)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.expression1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29]:
                    self.state = 341
                    self.variable_declaration()
                    pass
                elif token in [71]:
                    self.state = 342
                    self.assignment_statement()
                    self.state = 343
                    self.match(MiniGoParser.SEMI)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 347
                self.expression1(0)
                self.state = 348
                self.match(MiniGoParser.SEMI)
                self.state = 349
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 351
                self.match(MiniGoParser.ID)
                self.state = 352
                self.match(MiniGoParser.COMMA)
                self.state = 353
                self.match(MiniGoParser.ID)
                self.state = 354
                self.match(MiniGoParser.ASSIGN_DECL)
                self.state = 355
                self.match(MiniGoParser.RANGE)
                self.state = 356
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def builtin_function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Builtin_function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_call_statement)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.method_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self.builtin_function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def builtin_function_name(self):
            return self.getTypedRuleContext(MiniGoParser.Builtin_function_nameContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_builtin_function_call




    def builtin_function_call(self):

        localctx = MiniGoParser.Builtin_function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_builtin_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.builtin_function_name()
            self.state = 369
            self.match(MiniGoParser.LPAREN)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 335041282055) != 0):
                self.state = 370
                self.expressionlist()


            self.state = 373
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_builtin_function_name




    def builtin_function_name(self):

        localctx = MiniGoParser.Builtin_function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_builtin_function_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65528) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(MiniGoParser.RETURN)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 335041282055) != 0):
                self.state = 378
                self.expression1(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclareContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclareContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MiniGoParser.LBRACE)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4030595064) != 0) or _la==71:
                self.state = 384
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 382
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 383
                    self.declare()
                    pass


                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 389
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expression1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expression1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionlist




    def expressionlist(self):

        localctx = MiniGoParser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expressionlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.expression1(0)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==64:
                self.state = 392
                self.match(MiniGoParser.COMMA)
                self.state = 393
                self.expression1(0)
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 402
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 403
                    self.match(MiniGoParser.OR)
                    self.state = 404
                    self.expression2(0) 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 413
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 414
                    self.match(MiniGoParser.AND)
                    self.state = 415
                    self.expression3(0) 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 424
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 425
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 108119376405725184) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 426
                    self.expression4(0) 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 435
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 436
                    _la = self._input.LA(1)
                    if not(_la==50 or _la==51):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 437
                    self.expression5(0) 
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def MULT(self):
            return self.getToken(MiniGoParser.MULT, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 446
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 447
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31525197391593472) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 448
                    self.expression6() 
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6




    def expression6(self):

        localctx = MiniGoParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                _la = self._input.LA(1)
                if not(_la==47 or _la==51):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 455
                self.expression6()
                pass
            elif token in [33, 34, 35, 58, 66, 67, 68, 71]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression7)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.struct_access()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 462
                self.method_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 463
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 464
                self.match(MiniGoParser.LPAREN)
                self.state = 465
                self.expression1(0)
                self.state = 466
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expression1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expression1Context,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(MiniGoParser.ID)
            self.state = 475 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 471
                    self.match(MiniGoParser.LBRACK)
                    self.state = 472
                    self.expression1(0)
                    self.state = 473
                    self.match(MiniGoParser.RBRACK)

                else:
                    raise NoViableAltException(self)
                self.state = 477 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary1(self):
            return self.getTypedRuleContext(MiniGoParser.Primary1Context,0)


        def struct_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.primary1()
            self.state = 480
            self.struct_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_tailContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_tail




    def struct_tail(self):

        localctx = MiniGoParser.Struct_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_struct_tail)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(MiniGoParser.DOT)
                self.state = 483
                self.match(MiniGoParser.ID)
                self.state = 484
                self.struct_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.match(MiniGoParser.LBRACK)
                self.state = 486
                self.expression1(0)
                self.state = 487
                self.match(MiniGoParser.RBRACK)
                self.state = 488
                self.struct_tail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary1




    def primary1(self):

        localctx = MiniGoParser.Primary1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_primary1)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.primary()
            self.state = 498
            self.match(MiniGoParser.DOT)
            self.state = 499
            self.match(MiniGoParser.ID)
            self.state = 500
            self.match(MiniGoParser.LPAREN)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 335041282055) != 0):
                self.state = 501
                self.expressionlist()


            self.state = 504
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary




    def primary(self):

        localctx = MiniGoParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_primary)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.function_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.struct_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(MiniGoParser.ID)
            self.state = 512
            self.match(MiniGoParser.LPAREN)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 335041282055) != 0):
                self.state = 513
                self.expressionlist()


            self.state = 516
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_operand)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35, 66, 67, 68]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.literal()
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            _la = self._input.LA(1)
            if not(((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 60129542151) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.expression1_sempred
        self._predicates[35] = self.expression2_sempred
        self._predicates[36] = self.expression3_sempred
        self._predicates[37] = self.expression4_sempred
        self._predicates[38] = self.expression5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




