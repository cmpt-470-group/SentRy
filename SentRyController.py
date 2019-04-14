#!python3

import EternaBrainInterpret as EB
import SentRNAInterpret as SR
import SentRyCompare
import SentRyDisplay
from Utilities import GetTargets

SentRNAOutputFilepath = r'Data\E100SentRNA_models.txt'
targets = GetTargets(r'..\Data\eterna100.txt') #called from Utilities folder

sri = SR.Interpreter(SentRNAOutputFilepath)

sa1 = EB.GetEBOutput()
sa2 = sri.GetSentRNAOutput()

sa3 = SentRyCompare.CompareSeqArrs(sa1, sa2, targets)

SentRyDisplay.DisplayOutput(sa2)
