#!python3

import EternaBrainInterpret as EB
import SentRNAInterpret as SR
import SentRyCompare
import SentRyDisplay

SentRNAOutputFilepath = 'E100SentRNA_models.txt'
target = "..." # where do we get target
sri = SR.Interpreter(SentRNAOutputFilepath)

sa1 = EB.GetEBOutput()
sa2 = sri.GetSentRNAOutput()

sa3 = SentRyCompare.CompareSeqArrs(sa1, sa2, target)

SentRyDisplay.DisplayOutput(sa3)
