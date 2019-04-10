#!python3

import EternaBrainInterpret as EB
import SentRNAInterpret as SR
import SentRyCompare
import SentRyDisplay

sa1 = EB.GetEBOutput()
sa2 = SR.GetSentRNAOutput()

sa3 = SentRyCompare.CompareSeqArrs(sa1, sa2)

SentRyDisplay.DisplayOutput(sa3)
