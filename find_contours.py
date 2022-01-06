import os
import argparse
import pathlib
import cv2


def find_contors(img, destination, name):
    # Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to binary
    ret, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

    # Check
    cv2.imshow("gray", bin_img)
    cv2.waitKey(0)

    # Extract contours
    contours, hierarchy = cv2.findContours(
        bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Remove small contours
    contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))

    # Draw contours
    cv2.drawContours(img, contours, -1, color=(0, 0, 255), thickness=2)

    cv2.imwrite(f"{destination}/countored_{name}.png", img)


parser = argparse.ArgumentParser(description="Remove background of images")
parser.add_argument("target_path", help="Target folder path")
parser.add_argument("destination_path", help="Destination folder path")
args = parser.parse_args()

target = args.target_path
destination = args.destination_path

p = pathlib.Path(target)
p_list = list(p.glob("*"))

os.makedirs(destination, exist_ok=True)

print("******* Start finding contors... *******")
for count, p in enumerate(p_list):
    img = cv2.imread(str(p))
    find_contors(img, destination, pathlib.Path(p.name).stem)

    if (count + 1) % 50 == 0:
        print("Changing {}th image's color...\n".format(count + 1))

print("******* Finish finding contors... *******")
