# GnomeWPChanger
Simple python script that changes the background picture.

You can change the time in between each time the picture changes
directl in the code, when the function gets called.

The program uses `subprocess` to run a command in order to change the
gnome background. And it uses `time` to wait when not changing the picture,
`pathlib` and `os` to walk in the directory of the pictures.

To make the program work, you must write the path of the wallpapers in the
path variable. I could do a input function, but this would require to write
it everytime.

# How to run:

Paste into the terminal:
```sh
git clone https://github.com/bongstong/GnomeWPChanger
```

Then `cd GnomeWPChanger` And in order to run the program run
```python set-wp.py```

# Don't use this on your computer
I first made this for fun, and to train a bit. If you want to use this,
it is better to use the [C++ version](https://github.com/bongstong/GnomeBackgroundChanger), which is more lightweight,
and way better then the python version, since it uses less ressources.
