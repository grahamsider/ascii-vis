#!/usr/bin/env python


import os, sys, random, time, argparse
from data import asciidata

# Argument Parsing
parser = argparse.ArgumentParser(description='CLI ASCII Visualiser')
parser.add_argument('-i', '--img', metavar='<img_num>', type=int, default=0, required=False,
                    help='select image (default: 0)')
parser.add_argument('-b', '--bold', action='store_true', required=False,
                    help='set this flag to use bold terminal colors')
parser.add_argument('-r', '--rotate', action='store_true', required=False,
                    help='set this flag to rotate through all images (starts at <img_num>, specified above)')
parser.add_argument('-u', '--utime', metavar='<sec>', type=float, default='0.04', required=False,
                    help='unit time - seconds between updates (default: 0.04s)')
parser.add_argument('-s', '--speed', metavar='<int>', type=int, default=6, required=False,
                    help='number of characters changed per unit time (default: 6)')
parser.add_argument('-d', '--delay', metavar='<sec>', nargs=2, type=float, default=[0.3, 1.0], required=False,
                    help='number of seconds to sleep when image disappears and stays colored respectively (default: 0.3, 1.0)')
args = parser.parse_args()

# Default Colors
colors_def = [
    [37, 31, 33, 34, 35, 36, 32],
    [31, 33, 34, 35, 36, 37, 30]
]

colors_bold = [
    [97, 91, 93, 94, 95, 96, 92],
    [91, 93, 94, 95, 96, 97, 30]
]

def slt(img):
    return img.split("\n")

def get_scr_size():
    return [int(x) for x in os.popen("stty size", "r").read().split()]

def get_img_size(img):
    return [IMG.count("\n"), max([len(x) for x in slt(IMG)])]

def get_color(x, y, t, colors):
    f = x -max(img) +abs(t)
    off = random.randint(0, 16)

    for i in range(6, -1, -1):
        if f > y +(i *16) +off:
            if t >= 0:
                return "\033[" +str(colors[1][i]) +"m"
            elif t < 0:
                return "\033[" +str(colors[0][i]) +"m"
    return t <= 0 and "\033[30m" or "\033[" +str(colors[0][-1]) +"m"

def init_screen():
    global scr, img
    os.system("clear")
    scr = get_scr_size()
    img = get_img_size(IMG)

def exit():
    os.system("clear")
    os.system("tput cnorm")
    sys.exit(0)

if __name__ == '__main__':

    # Init
    os.system("tput civis")

    IMG = asciidata.IMG[args.img]
    imgnum = args.img
    colors = colors_bold if args.bold else colors_def

    init_screen()

    frames = img[0] * 6
    step = args.speed

    try:
        while 1:
            for t in (list(range(-frames, step, step)) +list(range(frames, 0, -step))):
                print ("\033[" + str(int((scr[0] - img[0]) / 2)) + "H")

                for y in range(img[0]):
                    print ((" " * int((scr[1] - img[1]) / 2))
                            + "".join([(get_color(x, y, t, colors)
                            + slt(IMG)[y][x] + "\033[0m")
                            for x in range(len(slt(IMG)[y]))]))

                if t == 0:
                    colors[0].append(colors[0].pop(random.randint(1, 3)))
                    init_screen()
                    time.sleep(args.delay[0])
                    if (args.rotate):
                        imgnum = (imgnum + 1) % len(asciidata.IMG)
                        IMG = asciidata.IMG[imgnum]
                        init_screen()

                time.sleep(args.utime)
            time.sleep(args.delay[1])
    finally:
        exit()
