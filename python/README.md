# Python samples and code

The `files` directory contains skeleton code that can be modified to run a GRIP-generated pipeline.

The `samples` directory has sample programs that can be run directly. Just clone this repository and run the main python files.

## Using the samples

The samples use Python 3 and require three libraries:

1. OpenCV
2. numpy (rquired by OpenCV)
3. pynetworktables

These can all be installed with pip3.

```bash
$ pip3 install numpy opencv-python pynetworktables
```

(if your default python version is at least 3+, the normal `pip` command should work)


Then `cd` into the directory of the sample you want to run and use the `python3` command to run the sample, eg

```bash
$ cd samples/frc_find_red_areas
$ python3 frc_find_red_areas.py
```

(Again, if your default python version is at least 3+, just the `python` command should work)


## Binaries

Since the Raspberry Pi 3 is a cheap ($35) and easy to use co-processor, we've created a Python 3 package for OpenCV for it and is available in the libs directory. To install it, you'll need to have the python `wheel` tool

```bash
$ pip3 install wheel
$ python3 -m wheel install opencv_python_rpi3-...whl
```
