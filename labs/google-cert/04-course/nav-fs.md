# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Navigate a Linux file system and read file contents

I worked through this lab to practice navigating a Linux file structure and reading the contents of files directly from the shell without any graphical interface

First I checked my current working directory using pwd and it returned /home/analyst which confirmed that is where I started from then I ran ls to see what was inside and the output showed logs projects reports and temp as the four items in that directory

After this when I came to the reports directory that was when I actually started navigating deeper into the structure I used cd reports to move into it using a relative path and then ran ls again which showed only one subdirectory called users

Then I navigated into /home/analyst/reports/users using cd and ran ls to see what files were there and I found Q1_added_users.txt so I used cat Q1_added_users.txt to read through the content directly in the shell

After analyzing the file I found the employee with username aezra works in the Human Resources department and the employee with username mreed in the Information Technology department has an employee_id of 1104

Next I navigated to /home/analyst/logs using cd and ran ls which showed a single file called server_logs.txt I used head server_logs.txt to display just the first 10 lines instead of the whole file and after going through that output I counted three warning messages within those first 10 lines

Commands I used throughout this lab

- pwd to check current working directory
- ls to list files and subdirectories
- cd with both relative and absolute paths to navigate
- cat to read full file contents
- head to display the first 10 lines of a file

This lab helped me get comfortable moving through a Linux file system and pulling information straight from files using basic commands which is something I know I will use a lot when investigating things like unauthorized access or reviewing user reports

— Completed as part of the Google Cybersecurity Certificate program.