#!python3
import RNA # pip install RNAlib-2.4.11

class Sequence:
    def __init__(self, PS = "", Name="Undefined",Target="Undefined"):
        self.FreeEnergy = 0.1
        self.PrimaryS = PS
        self.SecondaryS = ""
        self.Name = Name
        self.Target = target
        self.FoldAndEvaluate()

    def Display(self):
        output = "\n"
        output +=  + self.Name
        output += "\n------------------------------------------------"
        output += "\nPrimary Structure: " + self.PrimaryS
        output += "\nSecondary Structure: " + self.SecondaryS
        output += "\nFree Energy: " + str(self.FreeEnergy)
        output += "\n"
        return output

    def FoldAndEvaluate(self):
        (ss, fe) = RNA.fold(this.PrimaryS)
        self.SecondaryS = ss
        self.FreeEnergy = fe
        return true;

    def hamming_distance(self, target):
        assert len(self.SecondaryS) == len(target)
        return sum(ch1 != ch2 for ch1, ch2 in zip(self.SecondaryS, target))
