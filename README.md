# DROID-Batch-Processor
Code by Caitlin Donahue caitlindonahue95@gmail.com

This is a program to automatically run DROID on a set of files contained within a directory, and produce records for them.
DroidRunner takes a top directory and will run DROID on all of the bags contained within, placing the output files in BAGNAME/data/meta.
DroidRunner will produce a droid.droid file, a droid.csv file, and a droid.pdf file.

Once you have run DroidRunner once it will store the path to your droid files

##DROID: Digital Record Object Identification
DROID is a software tool developed by The National Archives to perform automated batch identification of file formats.

This program is tested with DROID 6.0.1, which can be found at http://sourceforge.net/projects/droid

Instructions to install DROID can be found at https://wiki.carleton.edu/display/ds/DROID+-+Digital+Record+Object+Identification

##Java Versions and DROID
DROID 6.0.1 requires Java 6 to run
If you experience errors with DROID running, and you are using a newer version of Java, try uninstalling Java, and installing Java 6.

Java 6 can be found here: http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase6-419409.html#jdk-6u45-oth-JPR


##Usage:
First navigate in your terminal to the folder in which DroidRunner.py is contained.
Once there there are several options on how to run the program.

- python DroidRunner.py (option)
  - Options are -h or --help 
  - This will display a usage message.

- python DroidRunner.py:
  - Running with no arguments will prompt you for the required paths.

- python DroidRunner.py <path to files to validate>:
  - If you have run the program before, or if you have added the location of your DROID files to the droid_settings.txt file, this will automatically run.
  - If you have not already supplied the program with the location of your DROID files, the program will prompt you for the path.
  - Upon prompting you for the path to the DROID files, the program will save their location for future use.

- python DroidRunner.py <path to files to validate> <path to Droid Files>:
  - This will run the program without needing to prompt the user for any paths
  - The supplied path to the DROID files will be added to the settings file.

###Input
- A directory of bags (folders) to run DROID's analysis on.
###Output
- A .droid file containing DROID's analysis in each bag.
- A .csv file containing DROID's analysis in each bag.
- A .pdf file containing DROID's analysis in each bag.
- If it does not already exist, a file named froid_settings.txt in the folder containing DroidRunner.py, that contains the path to your DROID program files
