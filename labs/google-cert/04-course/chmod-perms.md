# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Configure authorization with Linux file and directory permissions

I worked through this lab to check and manage file and directory permissions for the researcher2 user in the /home/researcher2/projects directory since researcher2 is part of the research_team group

I navigated into the projects directory using cd projects and ran ls -l to list the contents along with their permissions this showed me that research_team owns all the files in the directory and the listing included drafts project_k.txt project_m.txt project_r.txt and project_t.txt with different permission sets on each one

After this when I came to checking for hidden files that was when I ran ls -la instead of just ls -l and found there was a hidden file called .project_x.txt sitting in the directory that I would have completely missed otherwise

After analyzing the permissions closely I found that project_k.txt was giving write permissions to other users which is not something that should be allowed so I ran chmod o-w project_k.txt to remove write access for others on that file

Then I checked project_m.txt since it was supposed to be a restricted file that only the user should be able to read or write to and I found the group had read permission on it which was incorrect so I ran chmod g-r project_m.txt to remove read access for the group and lock that file down properly

On top of that I went back to the hidden file .project_x.txt and found both the user and the group had write permissions on an archived file that should never be written to again only read so I ran chmod u-w,g-w,g+r .project_x.txt to fix that and make sure the user and group could read it but not modify it

Finally I checked the drafts subdirectory inside projects and found the group still had execute permissions which meant they could access the directory and its contents when they should not have been able to since only researcher2 was supposed to have that access so I ran chmod g-x drafts to remove execute permission for the group and lock the directory down to the user only

Commands I used throughout this lab

- ls -l to list files with permission details
- ls -la to include hidden files in the listing
- chmod o-w to remove write permission for other
- chmod g-r to remove read permission for group
- chmod u-w,g-w,g+r to adjust multiple permissions on a hidden file in one command
- chmod g-x to remove execute permission for group on a directory

This lab really showed me how important it is to actually check permissions file by file instead of assuming they are correct because I found multiple files including a hidden one that had way more access granted than they should have and fixing this kind of thing is exactly the type of authorization work a security analyst needs to be comfortable doing

— Completed as part of the Google Cybersecurity Certificate program.