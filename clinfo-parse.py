#!/usr/bin/python


#######################################

#  Copyright (c) 2015 TierraDelFuego

#######################################


import os
import sys



global havegpu
havegpu = 0

def linecheck(line):
    global havegpu
    if 'Board name:' in line:
        print line.strip()
    if havegpu:
        if 'Global memory size:' in line:
            print line.strip()
            exit(1)
    if 'CL_DEVICE_TYPE_GPU' in line:
        print line.strip()
        havegpu = 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], 'rb') as hwinfo:
                for line in hwinfo:
                    linecheck(line)
            hwinfo.close()
        else:
            for file in sys.argv[1:]:
                print "No file found %s" % file
    else:
        for line in sys.stdin:
            linecheck(line)



