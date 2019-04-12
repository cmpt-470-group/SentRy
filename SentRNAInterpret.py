#!python3
from SentRyObjects import Sequence
import SentRyCompare
import os
import pickle
import ConvertPickles

class Interpreter:
    def __init__(self, models):
        self.SentRNAOutput = []
        self.models = open(models, 'r').read().split('\n')
        for model in self.models:
            if (model == ''): break
            ConvertPickles.ConvertToUnix(model)

            with open(model, "rb") as handle:
                self.SentRNAOutput.append(pickle.load(handle))

    def GetSentRNAOutput(self):
        ra = []
        for model in self.SentRNAOutput:
            tempra = []

            #merge best sequences
            for seq in model:
                tempra.append(Sequence(seq[1], seq[0]))

            #if first model
            if (len(ra) == len(tempra)):
                ra = SentRyCompare.CompareSeqArrs(tempra, ra)

            #error handling
            else if (len(ra) = 0):
                ra = tempra
            else:
                print('model not expected length')
                break
        return ra
