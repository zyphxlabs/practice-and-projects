## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Create A Conditional Statement

## What This Lab Covered
This lab was all about conditional statements which let code make decisions based on whether something is True or False. The scenario had two parts one where I had to check if a user's operating system needed an update and another where I had to investigate login attempts to a device and figure out if the user was approved and if they logged in during organization hours.

## What I Actually Did
I started with a simple if statement that checked whether system was equal to "OS 2" and if it was the code printed no update needed. When I set system to "OS 1" instead nothing printed at all because the condition never evaluated to True which showed me that an if statement on its own just does nothing if the condition fails.

After this I added an else block so that any system other than OS 2 would print update needed. I tested this with system set to "OS 3" and got update needed back which made more sense than having nothing display.

That was when I ran into the next issue though because the else block would still say update needed even if system was set to some random value that was not a real operating system at all. To fix that I used elif so I could specifically check for OS 1 and OS 3 separately and only print update needed when one of those two was actually true. I tested this with system set to "OS 4" and nothing printed which was the correct behavior since OS 4 is not a real option.

After analyzing that setup I realized the two elif statements could be combined into one using the or operator so instead of writing out OS 1 and OS 3 as two separate checks I combined them into a single elif system == "OS 1" or system == "OS 3" line which did the exact same thing but was way more concise.

Then I moved into the login attempt part of the lab. First I compared a username variable directly against two approved usernames elarson and bmoreno using an if and else statement with the or operator and when I set username to "bmoreno" it correctly printed This user has access to this device.

After that the number of approved users grew to five so instead of comparing against each one individually I built an approved_list containing elarson bmoreno tshah sgilmore and eraab and used the in operator to check if username was part of that list. I tested this with username set to "jhill" who was not on the list and it correctly printed This user does not have access to this device.

Next I built a separate conditional to check organization_hours which was a Boolean variable. When organization_hours was set to True the code printed Login attempt made during organization hours and when it was False it would print the opposite message.

For the final part I combined both conditions into one single if statement using and so it checked whether username was in approved_list and organization_hours was True at the same time. When both conditions were met with username set to "bmoreno" and organization_hours set to True the output was Login attempt made by an approved user during organization hours which condensed what used to be two separate print statements into one clean message.

## Key Takeaways
- if on its own does nothing when the condition is False you need else to handle the opposite case
- elif is what lets you check multiple specific conditions instead of relying on one broad else
- the or operator can combine multiple elif checks into a single line to keep code cleaner
- the in operator is much more efficient than comparing a variable against multiple usernames one by one especially as an allow list grows
- combining conditions with and lets you check multiple requirements at once and only return a message when every condition is satisfied

Completed as part of the Google Cybersecurity Certificate program.