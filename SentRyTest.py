#!python3

import EternaBrainInterpret as EB
import SentRNAInterpret as SR
import SentRyCompare
import SentRyDisplay
import ConvertPickles

SentRNAOutputFilepath = 'C:\\Users\\Sam\\SentRNA\\models\\refined_models\\batch1\\eterna100_trial-19_MI-39.pkl'
ConvertPickles.ConvertToUnix(SentRNAOutputFilepath)
sri = SR.Interpreter(SentRNAOutputFilepath)

sa1 = EB.GetEBOutput()
sa2 = sri.GetSentRNAOutput()

sa3 = SentRyCompare.CompareSeqArrs(sa1, sa2)

SentRyDisplay.DisplayOutput(sa3)
