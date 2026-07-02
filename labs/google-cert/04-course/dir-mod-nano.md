# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Modify a Linux directory structure and edit files with nano

I worked through this lab to reorganize the /home/analyst directory using core Linux commands and also used the nano text editor for the first time to edit a file directly from the shell

I started by creating a new subdirectory called logs inside /home/analyst using mkdir logs and ran ls afterward to confirm it was created along with the existing notes reports and temp directories

After this when I came to the part where I had to remove the temp directory that was when I used rmdir temp since it was no longer going to be used for anything and running ls again confirmed it was gone and only logs notes and reports remained

Then I navigated into /home/analyst/notes using cd and moved the Q3patches.txt file into the reports directory using mv Q3patches.txt /home/analyst/reports/ after that I listed the reports directory and confirmed all three quarterly files Q1patches.txt Q2patches.txt and Q3patches.txt were now together in the same place

After analyzing what else needed cleanup I removed the tempnotes.txt file from the notes directory using rm tempnotes.txt since it was unused and ran ls to confirm it no longer existed in that directory

Next I created a new empty file called tasks.txt inside the notes directory using touch tasks.txt and confirmed it was created by listing the directory contents again

Finally I opened tasks.txt using the nano text editor with nano tasks.txt and added a note documenting the tasks I completed then I pressed CTRL+X to exit and Y to confirm saving followed by ENTER to confirm the file name after that I used clear to clean up the shell window and ran cat tasks.txt to confirm the note was saved correctly inside the file

Commands I used throughout this lab

- mkdir to create a new directory
- rmdir to remove an empty directory
- mv to move a file to a different directory
- rm to delete a file
- touch to create a new empty file
- nano to edit a file directly in the shell
- cat and ls to confirm changes at each step

This lab gave me hands on practice organizing a directory structure the way a security analyst actually would by creating removing moving and editing files and it helped me get comfortable using nano for quick edits directly from the shell

— Completed as part of the Google Cybersecurity Certificate program.