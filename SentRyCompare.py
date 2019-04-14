#!python3
from SentRyObjects import Sequence

def CompareSeqArrs(sa1, sa2, targets):
    ra = []
    shortestLen = min(len(sa1), len(sa2), len(targets))
    for i in range(shortestLen):
        ra.append(CompareSeq(sa1[i], sa2[i], targets[i]))
    return ra


def CompareSeq(s1, s2, target):
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
