# DROID-Batch-Processor
Archives automatic DROID runner
===============================

Code by Caitlin Donahue caitlindonahue95@gmail.com

Program to automatically run DROID on a set of files contained within a directory, and produce records for them.
DROID is a software tool developed by The National Archives to perform automated batch identification of file formats.


This program is tested with DROID 6.0.1, which can be found at http://sourceforge.net/projects/droid
DROID 6.0.1 requires Java 6 to run

To run this program you must have DROID installed on your computer. This program assumes a basic knowledge of how DROID works.

DroidRunner takes a top directory and will run droid on all of the bags contained within, placing the output files in BAGNAME/data/meta.
DroidRunner will produce a droid.droid file, a droid.csv file, and a droid.pdf file.

Once you have run DroidRunner once it will store the path to your droid files

Usage:
python DroidRunner.py -h
-h or --help to display a usage message.

python DroidRunner.py:
Running with no arguments will prompt you for the required paths.

python DroidRunner.py <path to files to validate>:
Running with the argument <path to files to validate> will check settings file for an existing path to Droid, or prompt you for the path, then save that path to the settings file.

python DroidRunner.py <path to files to validate> <path to Droid Files>:
Running with the arguments <<path to files to validate> <path to DROID files>> will run the program, and save the droid path to the settings file.

The program will prompt you for the directory that contains the files you want to validate, and the directory that your droid files are stored in.

If droid_settings.txt does not already exist in the folder you are running DroidRunner in, it will create it.