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
