# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Use man whatis and apropos to find Linux command help

I worked through this lab to practice using the built in Linux help resources so I could look up what commands do and figure out which command to use when I could not remember the exact one

I started with whatis cat to get a quick reminder of what the command does and the short description returned was concatenate files which told me exactly what I needed without going through a full manual page

After this when I came to needing more detail on cat that was when I used man cat instead which gave me the full description along with all of its available options going through the output I found the -n option which numbers all the output lines of the cat command I pressed Q to exit out of the manual page once I was done reading through it

Then I used apropos -a first part file to search for a command that returns just the first part of a file since I could not remember the exact command name and this search returned head as the command that prints only the first part of a file

Next I moved into exploring the useradd command since I wanted to figure out how to set an expiration date for a temporary user account I ran man useradd and went through the options until I found -e which is the option used to set an expiration date for a user account

After analyzing the difference between rm and rmdir since I could not remember how they were different I ran whatis rm and whatis rmdir separately and confirmed that rmdir is the command that only removes empty directories while rm is used more generally to remove files

Finally I needed to figure out the command to create a new group so I used apropos -a create new group with those exact keywords and this search returned groupadd as the correct command to create a new group

Commands I used throughout this lab

- whatis to get a short one line description of a command
- man to get the full manual page and all options for a command
- apropos -a to search for a command using keywords when I could not remember the exact name

This lab was useful because it showed me I do not need to memorize every single command and option since Linux has built in resources like man whatis and apropos that let me look things up quickly which is realistic since as a security analyst I will run into commands I have not used in a while and need a fast way to relearn them

— Completed as part of the Google Cybersecurity Certificate program.