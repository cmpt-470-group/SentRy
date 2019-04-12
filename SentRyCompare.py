#!python3
from SentRyObjects import Sequence

def CompareSeqArrs(sa1, sa2):
    ra = []
    print(str(sa1) + "\n Sa2: " + str(sa2)) #check values in arrays
    for i in range(len(sa1)):
        ra.append(CompareSeq(sa1[i], sa2[i]))
    return ra


def CompareSeq(s1, s2):
    if(min(s1.FreeEnergy, s2.FreeEnergy) == s1.FreeEnergy):
        return s1
    else:
        return s2
