"""
Program to automatically run DROID on a set of files contained within a directory, and produce records for them
DROID is a software tool developed by The National Archives to perform automated batch identification of file formats.
This program is tested with DROID 6.0.1, which can be found at http://sourceforge.net/projects/droid
DROID 6.0.1 requires Java 6 to run


Code by Caitlin Donahue
caitlindonahue95@gmail.com
Summer 2015  
"""

import os
import sys
import platform
import ast
import errno
import time

def readSettingsFile():
    if not os.path.isfile("droid_settings.txt"):
        with open("droid_settings.txt", "w") as f:
            f.write("PATH_TO_DROID:\n")
    with open("droid_settings.txt") as f:
        f_content = [line.rstrip() for line in f]
        parse_state = "none"
        path = ""
        for i in range(len(f_content)):
            line = f_content[i]
            #no parse state yet
            #excludes is the files that are excluded from being checked
            #time is the sleep time in the error check
            if parse_state == "none":
                if line == "PATH_TO_DROID:":
                    parse_state = "pathtodroid"
            elif parse_state == "pathtodroid":
                if line != "":
                    path = line
                else:
                    parse_state = "none"
        return path

def usage_message():
    print "DroidRunner is a program to automatically run DROID on a set of files contained within a directory, and produce records for them \n \
    DROID is a software tool developed by The National Archives to perform automated batch identification of file formats. \n \
    This program is tested with DROID 6.0.1, which can be found at http://sourceforge.net/projects/droid \n \
    DROID 6.0.1 requires Java 6 to run" 
    print "--------------------"
    print "Usage:"
    print "-h or --help to display this message"
    print "<python DroidRunner.py> with no arguments will prompt you for the required paths"
    print "<python DroidRunner.py <path to files to validate>> will check settings file for an existing path to Droid, or prompt you for the path"
    print "<python DroidRunner.py <path to files to validate> <path to DROID files>> will run the program, and save the droid path to the settings file"
    print "--------------------"
    print "Dependencies:"
    print "droid_settings.txt must be in the same directory as DroidRunner.py"
    print "Must have Droid installed on your computer"

def main():
    start_time = time.time()
    #store the original directory so we can navigate back to it at the end of the program
    original_location = os.getcwd()
    parent = ""
    droid = ""
    droidName = ""
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            usage_message()
        else:
            parent = sys.argv[1]
    elif len(sys.argv) == 3:
        parent = sys.argv[1]
        droid = sys.argv[2]
    if parent == "":
        #get file locations from the user
        print "Please enter the directory that holds the bags you would like to validate: "
        parent = raw_input().strip()
    temp = readSettingsFile()
    #if there was no command argument and there was a path in the file
    if droid == "" and temp != "":
        droid = temp
    #if there was a command argument, but no path in the file
    elif droid != "" and temp =="":
        with open("droid_settings.txt", "a") as settings:
            settings.write(droid)
    #if there was no command argument and nothing in the file
    elif droid == "" and temp == "":
        print "Please enter the location of your droid program: "
        droid = raw_input().strip()
        with open("droid_settings.txt", "a") as settings:
            settings.write(droid)

    #check what os the user is running to account for terminal command differences
    if platform.system() == "Windows":
        droidName = "droid"
    else:
        droidName = "./droid.sh"
    #make sure the directories are in the correct format
    parent = parent.strip().strip("'").strip('"')
    droid = droid.strip().strip("'").strip('"')
    #navigate to the file that the user's droid program is located in     
    os.chdir(droid)
    #update droids signiture files
    print "--------------------------------------"
    print "Updating Droid"
    print "--------------------------------------"
    cmd = droidName + " -d"
    os.system(cmd)
    print "--------------------------------------"
    print "Validating Files"
    print "--------------------------------------"

    #make a list of all of the folders in this directory
    path_list = [x for x in os.listdir(parent)]

    for folder in path_list:
        full_folder_path = os.path.join(parent, folder).strip()
        if os.path.isdir(full_folder_path):
            print "--------------------------------------"
            print "Validating files in " + full_folder_path
            print "--------------------------------------"
            meta_path = os.path.join(full_folder_path,"data","meta")
            print "--------------------------------------"
            print "Making sure " + meta_path + " exists."
            print "--------------------------------------"
            try:
                os.makedirs(meta_path)
            #If an error is raised
            #ignore it if it is telling us the file already exists
            #raise the error if it is related to something else
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise
            full_folder_path = ('"' + full_folder_path + '"')
            orig_meta = meta_path
            meta_path = ('"' + meta_path + '"')
            profile_path = os.path.join(meta_path, "droid.droid")
            print "--------------------------------------"
            print "Creating profile in " + meta_path
            print "--------------------------------------"
            cmd = droidName + " -R -a " + full_folder_path + " -p " + profile_path
            os.system(cmd)
            print "--------------------------------------"
            print "Creating droid.csv"
            print "--------------------------------------"
            cmd = droidName + " -p " + profile_path + " -e " + os.path.join(meta_path, "droid.csv")
            os.system(cmd)
            print "--------------------------------------"
            print "Creating droid.pdf"
            print "--------------------------------------"
            cmd = droidName + " -p " + profile_path + " -n \"Comprehensive breakdown\" -r " + os.path.join(meta_path, "droid.pdf")
            os.system(cmd)
            print "--------------------------------------"
            print "Checking if files were created"
            print "--------------------------------------"
            #check if droid.droid was created
            file_time = 0
            try:
                file_time = os.path.getmtime(os.path.join(orig_meta, "droid.droid"))
            except:
                print 
                print "--------------------------------------"
                print "WARNING" + os.path.join(orig_meta, "droid.droid")+" NOT CREATED"
                print "--------------------------------------"
            if file_time != 0:
                if file_time - start_time < 0:
                    print "--------------------------------------"
                    print "WARNING" + os.path.join(orig_meta, "droid.droid") + " NOT UPDATED"
                    print "--------------------------------------"
            #check if Droid.csv was created
            file_time = 0
            try:
                file_time = os.path.getmtime(os.path.join(orig_meta, "droid.csv"))
            except:
                print "--------------------------------------"
                print "WARNING" + os.path.join(orig_meta, "droid.csv")+" NOT CREATED"
                print "--------------------------------------"
            if file_time != 0:
                if file_time - start_time < 0:
                    print "--------------------------------------"
                    print "WARNING" + os.path.join(orig_meta, "droid.csv")+" NOT UPDATED"
                    print "--------------------------------------"
            #check if Droid.pdf was created
            file_time = 0
            try:
                file_time = os.path.getmtime(os.path.join(orig_meta, "droid.pdf"))
            except:
                print "--------------------------------------"
                print "WARNING" + os.path.join(orig_meta, "droid.pdf")+" NOT CREATED"
                print "--------------------------------------"
            if file_time != 0:
                if file_time - start_time < 0:
                    print "--------------------------------------"
                    print "WARNING" + os.path.join(orig_meta, "droid.pdf")+" NOT UPDATED"
                    print "--------------------------------------"
            print "--------------------------------------"
            print "Validation of " + full_folder_path + " complete"
            print "--------------------------------------"
           
    print "--------------------------------------"
    print "Validation Complete"
    print "--------------------------------------"
    

    os.chdir(original_location)
main()