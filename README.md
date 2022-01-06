# Image Modifier
Modify Sets of Image Data

## cut_out_blank_space.py
Cut out the whitespace of each image and save in the target directory.
```
$ python cut_out_blank_space.py [target directory path] [destination directory path]
```

## detect_edge.py
Detect the edge of each image and save in the target directorty.
```
$ python detect_edge.py [target directory path] [destination directory path]
```

## remove_bg.py
Remove the background of each image and save in the target directory.
```
$ python remove_bg.py [target directory path] [destination directory path]
```

## resize.py
Resize each image and save in the target directory.
```
$ python resize.py [target directory path] [destination directory path] [length of one side of the image to resize (pixel)]
```

## rename.py
Rename each file in order and save in the target directory.
```
$ python rename.py [target directory path] [destination directory path] [file name] [file extension] [Option: --shuffle (True or False)]

e.g.,
$ python rename.py ../images/test ../images/test-renamed img png --shuffle True
```
If the number of the files are 200, the outputs of the above example are like this: `img_000.png`, `img_001.png`, ..., `img_200.png` <br>
If you set `--shuffle True`, the order of the files are shuffled before renaming (Default is False).


## fill_one_color.py
Change one color to another color in images and save in the target directory.
```
$ python fill_one_color.py [target directory path] [destination directory path] --from_color [red.green.blue] --to_color [red.green.blue]

e.g., If you want to change "white" to "gray"
$ python fill_one_color.py ./target/directory/path ./destination/directory/path --from_color 0.0.0 --to_color 128.128.128
```

## find_contours.py
Detect contours of the objects in images and save in the target directory.
```
$ python find_contours.py [target directory path] [destination directory path]
```

