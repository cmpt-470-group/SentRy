#!python3
from SentRyObjects import Sequence

def GetSentRNAOutput():
    #temporary output for testing
    ra = []
    ra.append(Sequence(2.4, "GUACACAUCA", "TestStructurelul1", "A"))
    ra.append(Sequence(-1.7, "CUGUGUGAGC", "TestStructurelul2", "B"))
    ra.append(Sequence(24.4, "GUACACACAG", "TestStructurelul3", "C"))
    return ra
