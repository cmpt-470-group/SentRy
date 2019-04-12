#!python3
from SentRyObjects import Sequence

def GetEBOutput():
    #temporary output for testing
    ra = []
    ra.append(Sequence("ACAUCAGUAC", "X"))
    ra.append(Sequence("UGAGCCUGUG", "Y"))
    ra.append(Sequence( "GUACAGACAC", "Z"))
    return ra
