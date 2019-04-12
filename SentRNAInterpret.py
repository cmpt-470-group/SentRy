#!python3
from SentRyObjects import Sequence
import os
import pickle
import ConvertPickles

class Interpreter:
    def __init__(self, models):
        self.models = open(models, 'r').read().split('\n')
        for model in self.models:
            ConvertPickles.ConvertToUnix(model)
            with open(model, "rb") as handle:
                self.SentRNAOutput = pickle.load(handle)

    def GetSentRNAOutput(self):
        #temporary output for testing
        ra = []
        for seq in self.SentRNAOutput:
            ra.append(Sequence(self.getFreeEnergy(), #David's tool
             seq[1], "TestStructurelul1", seq[0]))
        return ra

    def getFreeEnergy(self):
        return 0 #placeholder for david's tool
