# CLI ASCII Visualizer

Fork from `rasmusmerzin/cli-visuals` -- all credit for this idea goes to them.

Supports terminal colors.

## Usage

`python3` `/path/to/vis.py` `[args]`

Optional Arguments:

  `-h`, `--help`: show help message and exit

  `-i`, `--img <img_num>`: select image (default: 0)

  `-r`, `--rotate`: set this flag to rotate through all images (starts at <img_num>, specified above)

  `-u`, `--utime <sec>`: unit time - seconds between updates (default: 0.04s)

  `-s`, `--speed <int>`: number of characters changed per unit time (default: 6)

  `-d`, `--delay <sec> <sec>`: number of seconds to sleep when image disappears and stays colored respectively (default: 0.3, 1.0)
