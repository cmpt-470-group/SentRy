#!python3
from SentRyObjects import Sequence

def CompareSeqArrs(sa1, sa2):
    ra = []
    for i in range(len(sa1)):
        ra.append(CompareSeq(sa1[i], sa2[i]))
    return ra


def CompareSeq(s1, s2):
    hd1 = s1.hamming_distance(target)
    hd2 = s2.hamming_distance(target)
    if(hd1 < hd2):
        return s1
    else if (hd1 == hd2):
        if (min(s1.FreeEnergy, s2.FreeEnergy) == s1.FreeEnergy):
            return s1
        else:
            return s2
    else:
        return s2
        
