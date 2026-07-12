## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Develop An Algorithm

## What This Lab Covered
This lab pulled together everything from earlier in the course to build an actual algorithm that connects users to their assigned devices. The scenario had me working with two synchronized lists approved_users and approved_devices where the user at a given index in one list corresponds to the device at the same index in the other and eventually I built a full login function out of all of it.

## What I Actually Did
I started by exploring how indexing works across both lists using approved_users[0] and approved_devices[0] which returned elarson and 8rp2k75 confirming that both lists lined up by position. Swapping the index to other numbers showed me the same pairing held true across the whole list.

After that a new employee named gesparza needed to be added along with their device 3rcv4w6 so I used .append() on both approved_users and approved_devices to add them to the end of each list. Printing both afterward confirmed gesparza and 3rcv4w6 were now the last elements in their respective lists.

That was when an employee named tshah left the team so I used .remove() to take tshah and their device 2ye3lzg out of both lists. Displaying the lists again showed tshah and 2ye3lzg were completely gone while everyone else stayed in the same order they were before.

Next I wrote a conditional to check if a given username was inside approved_users using the in operator. Testing with username set to sgilmore returned The username sgilmore is approved to access the system since sgilmore was still in the updated list.

After analyzing that I used the .index() method to find sgilmore's position inside approved_users and stored it in a variable called ind which came back as 2. I then used that same ind value to pull the matching entry out of approved_devices which returned 4n482ts confirming that indexing could connect information across two separate lists as long as they stayed synchronized.

After this when I came to the part which they lack that was when things started to seems bad because next I had to combine both checks into one conditional using and so it would verify the username was approved and that the device_id at ind matched what was entered. Testing with username sgilmore and device_id 4n482ts returned both The username sgilmore is approved to access the system and 4n482ts is the assigned device for sgilmore confirming the full match worked correctly.

I then added an elif to handle the case where the username was approved but the device_id did not match which would print a message saying the user is approved but that specific device is not assigned to them.

For the final task I pulled everything together into one function called login that takes username and device_id as parameters using a nested conditional inside it. The outer if checks whether username is in approved_users and the inner if checks whether device_id actually matches at the correct index. I tested this with three different combinations login for bmoreno with hl0s5o1 which correctly returned as approved and assigned login for elarson with the wrong device r2s5r9g which returned approved but not their assigned device and login for abernard with 4n482ts which correctly returned as not approved since abernard was never in the list at all.

## Key Takeaways
- when two lists are synchronized by index you can use one list to look up matching information in the other
- .append() and .remove() are the core methods for keeping an allow list updated as people join or leave a team
- .index() combined with list lookups is what makes it possible to connect a username to its correct device
- nested conditionals let you check multiple layers of logic inside one function instead of writing everything out flat
- wrapping all this logic into a single login() function turns a bunch of separate checks into one reusable tool that can be called with any combination of username and device_id

Completed as part of the Google Cybersecurity Certificate program.