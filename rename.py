import os
import pathlib
import argparse
import random
import shutil
from natsort import natsorted


parser = argparse.ArgumentParser(description="Rename files in the directory")
parser.add_argument("target_path", help="Target file path")
parser.add_argument("destination_path", help="Destination file path to save")
parser.add_argument("name", help="File name to change: results=[name]_*.[extension]")
parser.add_argument("extension", help="Extension of files to change")
parser.add_argument("--shuffle", default=False)
args = parser.parse_args()

target = args.target_path
destination = args.destination_path
name = args.name
ext = args.extension
shuffle = args.shuffle

p = pathlib.Path(target)
p_list = list(p.glob(f"*{ext}"))

os.makedirs(destination, exist_ok=True)

if shuffle:
    p_list = random.sample(p_list, len(p_list))
else:
    p_list = natsorted(p_list)

NoD = len(str(len(p_list)))
print("******* Start renaming files... *******")
for i, p in enumerate(p_list):
    prefix = "0" * (NoD - len(str(i)))
    _i = f"{prefix}{i}"
    print(_i)
    shutil.copy(p, f"{destination}/{name}_{_i}.{ext}")
print("******* Finish renaming files... *******")

