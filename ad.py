#!/usr/bin/env python


import os, sys, random, time, argparse
import imgdata


# Argument Parsing
parser = argparse.ArgumentParser(description='CLI ASCII Visualiser')
parser.add_argument('-i', '--img', metavar='<img_num>', type=int, required=False,
                    help='select image (default: 0)')
parser.add_argument('-o', '--once', action='store_true', required=False,
                    help='set this flag to exit after only one iteration')
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

    try: IMG = imgdata.IMG[args.img]
    except: IMG = imgdata.IMG[0]

    os.system("tput civis")
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
                    time.sleep(.3)

                time.sleep(.04)
            time.sleep(1)
            if (args.once):
                exit()
    finally:
        exit()
