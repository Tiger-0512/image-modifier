import os
import argparse
import pathlib
import cv2
import numpy as np


parser = argparse.ArgumentParser(description="Remove background of images")
parser.add_argument("target_path", help="Target folder path")
parser.add_argument("destination_path", help="Destination folder path")
tp = lambda x: list(map(int, x.split(".")))
parser.add_argument("--from_color", type=tp, help="Color for changing")
parser.add_argument("--to_color", type=tp, help="Result Color")
args = parser.parse_args()

target = args.target_path
destination = args.destination_path
from_color = args.from_color
to_color = args.to_color

p = pathlib.Path(target)
p_list = list(p.glob("*"))

os.makedirs(destination, exist_ok=True)

print("******* Start changing color... *******")
for count, p in enumerate(p_list):
    img = cv2.imread(str(p))
    img[np.where((img == from_color).all(axis=2))] = to_color
    cv2.imwrite(f"{destination}/ccolor_{pathlib.Path(p.name).stem}.png", img)

    if (count + 1) % 50 == 0:
        print("Changing {}th image's color...\n".format(count + 1))

print("\n******* Finish changing color! *******")
