#!python3
from SentRyObjects import Sequence
import sys
import pickle

class Interpreter:
    def __init__(self, output):
        with open(output, "rb") as handle:
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
