#!python3
class Sequence:
    def __init__(self, FE = 0, PS = "", SS = "", Name="Undefined"):
        self.FreeEnergy = FE
        self.PrimaryS = PS
        self.SecondaryS = SS
        self.Name = Name

    def Display(self):
        output = "\n"
        output += "\n" + self.Name
        output += "\n------------------------------------------------"
        output += "\nPrimary Structure: " + self.PrimaryS
        output += "\nSecondary Structure: " + self.SecondaryS
        output += "\nFree Energy: " + str(self.FreeEnergy)
        return output
