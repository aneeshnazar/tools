#!/usr/bin/env python3

import sys
from PIL import Image
#import matplotlib.pyplot as plt
import numpy as np

def getXPM(arg):
    ret = []
    col_arr = {}
    with open(arg, 'r') as xpm:
        line = xpm.readline().strip().strip('"')
        width, height, colors, chars = [int(x) for x in line.split(' ')]
        for _ in range(colors):
            line = xpm.readline().strip().strip('"')
            key, _, color = [x for x in line.split(' ')]
            col_arr[key] = color
        for x in range(width):
            arr = []
            line = xpm.readline().strip().strip('"')
            for y in range(height):
                arr += [[int(col_arr[line[y]][1:3], 16), int(col_arr[line[y]][3:5], 16), int(col_arr[line[y]][5:7], 16)]]
            ret += [arr]
    return (ret)

def main():
    arr = getXPM(sys.argv[1])
    im = Image.fromarray(np.array(getXPM(sys.argv[1]), dtype=np.uint8), 'RGB')
    #im = np.array(getXPM(sys.argv[1]))
    #plt.imsave("tmp.jpg",im)
    #print(im)
    im.show()

if __name__ == '__main__':
    main()
