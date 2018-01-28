#!/usr/bin/env python3

import sys
from PIL import Image
#import matplotlib.pyplot as plt
import numpy as np
import re

fline = re.compile(r"(static.*)")
lline = re.compile(r"};")
comment = re.compile(r"^\/\*.*\*\/")
info = re.compile(r"\"\d+\s+\d+\s+\d+\s+\d+\s*\"")
colorl = re.compile(r"\"(.)\s+c\s+#([0-9A-Fa-f]{6})\"")

def getXPM(arg):
    ret = []
    col_arr = {}
    i = 0;
    with open(arg, 'r') as xpm:
        line = xpm.readline()
        for line in xpm.readlines():
            line = line.strip()
            if comment.match(line) or fline.match(line) or lline.match(line):
                continue
            elif info.match(line):
                line = line.strip(',').strip('"')
                width, height, colors, chars = [int(x) for x in line.split()]
            elif colorl.match(line):
                l = colorl.match(line)
                key, color = l.group(1), l.group(2)
                col_arr[key] = color
            else:
                arr = []
                line = line.strip('"')
                for y in range(height):
                    arr += [[int(col_arr[line[y]][0:2], 16), int(col_arr[line[y]][2:4], 16), int(col_arr[line[y]][4:6], 16)]]
                ret += [arr]
    return (ret)

def main():
    if (len(sys.argv) == 2):
        arr = getXPM(sys.argv[1])
        im = Image.fromarray(np.array(arr, dtype=np.uint8), 'RGB')
        im.show()
    else :
        print("Usage: ./view_xpm.py [.xpm image]")

if __name__ == '__main__':
    main()
