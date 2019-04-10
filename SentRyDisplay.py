#!python3
from SentRyObjects import Sequence

def DisplayOutput(output):
    i = 0
    for seq in output:
        i += 1
        print("Sequence " + str(i))
        print(seq.Display())


#def OutputToFile(output, filename):
