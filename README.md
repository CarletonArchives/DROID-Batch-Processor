# DROID-Batch-Processor
Code by Caitlin Donahue caitlindonahue95@gmail.com

This is a program to automatically run DROID on a set of files contained within a directory, and produce records for them.
DroidRunner takes a top directory and will run DROID on all of the bags contained within, placing the output files in BAGNAME/data/meta.
DroidRunner will produce a droid.droid file, a droid.csv file, and a droid.pdf file.

Once you have run DroidRunner once it will store the path to your droid files.

##DROID: Digital Record Object Identification
DROID is a software tool developed by The National Archives to perform automated batch identification of file formats.

You can download the newest version of DROID at http://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/
(Make sure to download the binary file, not the source code).

##Installing DROID (MAC)

- Locate the file "droid-binary-6.1.5-bin.zip" in your downloads folder.

- Double click to create the folder "droid-binary-6.1.5-bin". Drag this to the desktop

- Open a terminal window by navigating to "Applications -> Utilities -> Terminal" and clicking on the Terminal icon.

- In the terminal window, type the following commands exactly as they appear, hitting "return" after each line.

  - cd Desktop/droid-binary-6.1.5-bin
  
  - chmod +x droid.sh
  
  - chmod +x droid-ui-6.1.5.jar
  
  - chmod +x droid-command-line-6.1.5.jar

##Java Versions and DROID
DROID 6.1.5 requires Java 7 to run
If you experience errors with DROID running, and you are using a different version of Java, download and install Java 7.

Java 7 can be found here: http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

To check what version of Java (if any) you have installed on your computer, in the command prompt type:

      java -version

If you are running the most recent version of Java 7, the version should be 1.7.0_79.

If you want to run Java 7 for only this program, and keep your current version of Java as the default, Go to the section *Temporary Java environment setup*.
If you want to run Java 7 for all programs, uninstall your current version of Java, and install Java 7. If you are using a Windows computer, follow the instructions under *Java runtime environment setup (PC)*


###Java runtime environment setup (PC)
####Finding the JAVA_HOME Variable:
- Install Java runtime environment
  - Check to see if Java is already installed on your computer. 
  - Go to Start->control panel
  - If Java is present in the control panel, proceed to the section on setting the Java_home environmental variable.  
  - If not download and install Java from the Oracle website or from java.com
- Identifying the JAVA_HOME environmental variable path value
  - If you already know the value of the path for java_home on your computer, proceed to the section for setting the value of this variable. 
  - If you do not know this value, go to Start/Control Panel/Java
  - Select the Java tab in the Java Control Panel.
  - Select View.
  - The value of JAVA_HOME should be everything in the path field before the bin directory.  For example, if the value of the path field is C:\Program Files\Java\jre6\bin\javaw.exe, then the variable value should be C:\Program Files\Java\jre6
#### Configuring the Java_home environment variable:
  - Right click on My computer, select Properties/advanced/environmental properties
  - Scroll down and look for a variable named JAVA_HOME.
  - If a variable is present, make sure it matches the path from the section above on identifying the JAVA_HOME path
  - If no JAVA_HOME variable is present, click New. 
  - The name of the variable should be: JAVA_HOME.
  - The value of the variable should be the path from the section above on identifying the JAVA_HOME path
  - Hit OK.
- Check that the JAVA_HOME variable is set properly 
  - Go to Start/Run 
  - enter cmd in the Run window.
  - Once a command prompt is open, enter Set and hit return
  - This will give a list of all the environmental variables available to this user.
  - JAVA_HOME should be in this list and its value should be the path you identified and entered above. 
  - If JAVA_HOME is not present or has the wrong value assigned, make sure that all the steps above have been followed correctly.  

###Temporary Java environment setup:
####Using the command line in Windows:
-This method is good if you want to run both Java 7 and a newer version of Java on your computer
-This will set up your computer to use Java 7 for anything run in this command window. Once you close the window java will revert to the newest version of Java.
-In the command prompt enter this command:

      set JAVA_HOME=C:\<enter value of JAVA_HOME found in the above section>
  
-Then to make sure the PATH variable is set correctly enter the following into the command prompt:

     set PATH=%JAVA_HOME%\bin;%PATH%
-Check if you successfully changed the version by typing:

      java -version
      
      
####Using the terminal on a Mac:
-Open the terminal and type the command:

      /usr/libexec/java_home -v 1.7
      
-This will output the path to where java_home for this version is stored.
Now to set up the JAVA_HOME variable type:

      export JAVA_HOME=(The output of the above step)
-Check if you successfully changed the version by typing:

      java -version

##Installing Python
You will need Python installed on your computer to run this program.
Python can be found here: https://www.python.org/download/releases/2.7.5/
or here: https://www.python.org/download/releases/3.2.2/

Instructions on setting up Pyton on your computer can be found here: https://apps.carleton.edu/curricular/cs/resources/source/python_install/

##Usage:

(Mac) Open a terminal window by navigating to "Applications -> Utilities -> Terminal" and clicking on the Terminal icon
(PC) Open a command prompt by selecting Start/Run and typing cmd and Enter or Start/Programs/Accessories/Command Prompt.

First navigate in your terminal to the folder in which DroidRunner.py is contained.

        cd PATH_TO_FOLDER_CONTAINING_DROIDRUNNER

There there are several options on how to run the program:

        python DroidRunner.py <option>
        
  - Options are -h or --help 
  - This will display a usage message.


        python DroidRunner.py
     
  - Running with no arguments will prompt you for the required paths.


        python DroidRunner.py <path to files to validate>
        
  - If you have run the program before, or if you have added the location of your DROID files to the droid_settings.txt file, this will automatically run.
  - If you have not already supplied the program with the location of your DROID files, the program will prompt you for the path.
  - Upon prompting you for the path to the DROID files, the program will save their location for future use.


        python DroidRunner.py <path to files to validate> <path to Droid Files>



  - This will run the program without needing to prompt the user for any paths
  - The supplied path to the DROID files will be added to the settings file.

###Input
- A directory of bags (folders) to run DROID's analysis on.

###Output
- A .droid file containing DROID's analysis in each bag.
- A .csv file containing DROID's analysis in each bag.
- A .pdf file containing DROID's analysis in each bag.
- If it does not already exist, a file named froid_settings.txt in the folder containing DroidRunner.py, that contains the path to your DROID program files.
