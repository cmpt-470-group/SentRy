#!/usr/bin/env python

#convert dos linefeeds (crlf) to unix (lf)
def ConvertToUnix(filename):

    content = ''
    outsize = 0
    with open(filename, 'rb') as infile:
        content = infile.read()
    with open(filename, 'wb') as output:
        for line in content.splitlines():
                outsize += len(line) + 1
                output.write(line + str.encode('\n'))

    print("Done. Saved %s bytes." % (len(content)-outsize))

def GetTargets(path):
    items = open(path, 'r').read().split('\t')
    targets = []
    for i in range(len(items)):
        if i % 7 == 4:
            if i != 4:
                targets.append(items[i])
    print(targets)
    return targets
