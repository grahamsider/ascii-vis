# CLI ASCII Visualizer

Fork from `rasmusmerzin/cli-visuals` -- all credit for this idea goes to him/her.

Supports terminal colors.

## Usage

python3 /path/to/ad.py [args]


Optional Arguments:
  `-h`, `--help`: show this help message and exit
  `-i`, `--img <img_num>`: select image (default: 0)
  `-r`, `--rotate`: set this flag to rotate through all images, starting at <img_num>
  `-u`, `--utime <sec>`: unit time: seconds between updates (default: 0.04s)
  `-s`, `--speed <int>`: number of characters changed per unit time
  `-d`, `--delay <sec> <sec>`: number of seconds to sleep when image disappears and stays colored respectively (default: 0.3, 1.0)
