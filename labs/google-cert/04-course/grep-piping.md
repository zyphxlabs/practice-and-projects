# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Use grep and piping to search files and filter output

I worked through this lab to practice using grep and piping to search through log files and file names for specific information

I started by navigating to /home/analyst/logs using cd logs and then used grep error server_logs.txt to filter the file and return only the lines containing the word error after going through the output I counted six entries in the server_logs.txt file that included the error string

After this when I came to the users directory that was when I started working with piping instead of just grep on its own I navigated to /home/analyst/reports/users and ran ls | grep Q1 to pipe the output of ls into grep and only show files with Q1 in the name I found three files in that directory with Q1 in their names

Then I ran ls | grep access to search for files containing the word access in their names and this returned four files in the reports/users directory that had access in the file name

After analyzing the file names I moved into searching actual file contents I ran ls again to see everything in the users directory then used grep jhill Q2_deleted_users.txt to search for the username jhill inside that file and confirmed yes the user jhill is listed in the Q2_deleted_users.txt file which means that user was deleted from the system

I also searched the Q4_added_users.txt file to find users added to the Human Resources department using grep on the file to pull out only the matching entries

Commands I used throughout this lab

- grep to search file contents for a specific string
- ls piped into grep using the pipe character to filter file names
- cd with relative and absolute paths to move between directories

This lab helped me understand how useful grep and piping are for a security analyst since being able to search through logs and file names quickly for a specific string like error or a username makes investigating incidents a lot faster than manually reading through everything

— Completed as part of the Google Cybersecurity Certificate program.