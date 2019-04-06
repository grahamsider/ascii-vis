#!/usr/bin/env python


import os, sys, random, time, argparse
import imgdata


# Argument Parsing
parser = argparse.ArgumentParser(description='CLI ASCII Visualiser')
parser.add_argument('-i', '--img', metavar='<img_num>', type=int, default=0, required=False,
                    help='select image (default: 0)')
parser.add_argument('-r', '--rotate', action='store_true', required=False,
                    help='set this flag to rotate through all images, starting at <img_num>')
parser.add_argument('-d', '--delay', metavar='<delay time (s)>', type=float, default='0.04', required=False,
                    help='set the amount animation delay (speed) (default: 0.04s)')
args = parser.parse_args()

# Default Colors
colors = [
    [37, 31, 33, 34, 35, 36, 32],
    [31, 33, 34, 35, 36, 37, 30]
]

def slt(img):
    return img.split("\n")

def get_scr_size():
    return [int(x) for x in os.popen("stty size", "r").read().split()]

def get_img_size(img):
    return [IMG.count("\n"), max([len(x) for x in slt(IMG)])]

def get_color(x, y, t):
    global colors, img

    f = x -max(img) +abs(t)

    off = random.randint(0, 16)

    for i in range(6, -1, -1):
        if f > y +(i *16) +off:
            if t >= 0:
                return "\033[" +str(colors[1][i]) +"m"
            elif t < 0:
                return "\033[" +str(colors[0][i]) +"m"
    return t <= 0 and "\033[30m" or "\033[" +str(colors[0][-1]) +"m"

def init():
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

    IMG = imgdata.IMG[args.img]
    imgnum = args.img

    del1 = args.delay * 7.5
    del2 = args.delay
    del3 = args.delay * 25

    init()

    frames = img[0] * 6
    step = 6

    try:
        while 1:
            for t in (list(range(-frames, step, step)) +list(range(frames, 0, -step))):
                print ("\033[" + str(int((scr[0] - img[0]) / 2)) + "H")

                for y in range(img[0]):
                    print ((" " * int((scr[1] - img[1]) / 2))
                            + "".join([(get_color(x, y, t)
                            + slt(IMG)[y][x] + "\033[0m")
                            for x in range(len(slt(IMG)[y]))]))

                if t == 0:
                    colors[0].append(colors[0].pop(random.randint(1, 3)))
                    init()
                    time.sleep(del1)
                    if (args.rotate):
                        imgnum = (imgnum + 1) % len(imgdata.IMG)
                        IMG = imgdata.IMG[imgnum]
                        init()

                time.sleep(del2)
            time.sleep(del3)
    finally:
        exit()
