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
