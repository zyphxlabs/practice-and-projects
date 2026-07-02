# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Manage user authentication with useradd usermod userdel and chown

I worked through this lab to practice managing user access in Linux for a new employee named researcher9 joining the organization using sudo for every command since adding and removing users requires root privileges

I started by adding the new user to the system using sudo useradd researcher9 and then added them to their primary group using sudo usermod -g research_team researcher9 since researcher9 was joining the Research department I also noted that both of these steps could have been done together using sudo useradd researcher9 -g research_team but I did them separately to practice each command on its own

After this when I came to assigning file ownership that was when I had to make researcher9 the owner of project_r.txt since they were taking over responsibility for that project the file was located in /home/researcher2/projects and was originally owned by researcher2 so I ran sudo chown /home/researcher2/projects/project_r.txt to transfer ownership over to researcher9

A couple months later in the scenario researcher9 started working in both Research and Sales so I had to add them to a secondary group without changing their primary group I used sudo usermod -a -G sales_team researcher9 making sure to use lowercase a and uppercase G exactly since Linux options are case sensitive and using the wrong case here would not work correctly

After analyzing the final part of the scenario where researcher9 left the company a year later I had to remove them from the system completely I ran sudo userdel researcher9 to delete the user and it gave me a message saying the researcher9 group was not removed because it was not the primary group which was expected since Linux automatically creates a group with the same name as the user when they are first added I also ran the command to delete that leftover researcher9 group afterward as good practice so no empty group was left behind

Commands I used throughout this lab

- sudo useradd to create a new user
- sudo usermod -g to set a primary group
- sudo usermod -a -G to add a secondary group without removing the primary one
- sudo chown to change file ownership
- sudo userdel to delete a user from the system

This lab helped me understand how authentication and access management actually work together in Linux since I had to add a user assign them ownership of a file change their group access as their role changed and eventually remove them completely which is exactly the kind of full lifecycle a security analyst needs to manage for real employees

— Completed as part of the Google Cybersecurity Certificate program.