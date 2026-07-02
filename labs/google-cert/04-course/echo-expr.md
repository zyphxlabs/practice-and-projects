# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Use the echo and expr commands to examine input and output

I worked through this lab in the Bash shell to get a better understanding of how input and output actually work when you communicate with the operating system through the shell

First I used echo hello and it returned hello directly which showed me that whatever string I type after echo is just going to be printed back to me as output then I ran it again with echo "hello" using quotation marks and got the exact same result hello so I understood the quotes are optional here but they matter more when the string has special characters that could get misread by the shell

After that I ran echo followed by my own name and the shell returned it back as output which confirmed the same behavior

Then I moved into the expr command to run some calculations directly in the shell I was given a scenario where I had 32 alerts total and only 8 of them required action so I needed to figure out how many were false positives I typed expr 32 - 8 and it returned 24 which meant 24 of the alerts were false positives and that is useful feedback I could give back to the team that configures the alerting system

After this when I came to the part where I had to calculate expected login attempts for the year that was when I saw how expr can be used for more real world type calculations I was told the average was 3500 login attempts per month so I typed expr 3500 * 12 and it returned 42000 which gave me the expected total logins for the year

Once I was done with the calculations I used the clear command to wipe the shell output and reset the cursor back to the top left so I could keep working in a clean window without old commands cluttering the screen

I also ran a couple extra commands on my own to explore further

- echo "Example text" to generate additional output
- expr 25 + 15 to test basic addition in the shell

This lab helped me understand how the shell processes input and returns either output or an error and how commands like echo and expr can actually be used for practical tasks like calculating false positive rates and projecting login attempt volume

— Completed as part of the Google Cybersecurity Certificate program.