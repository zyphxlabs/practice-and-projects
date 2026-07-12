## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Create Loops


## What This Lab Covered
This lab had me working with iterative statements which are basically how you get Python to repeat an action instead of writing the same line over and over. The scenario covered three parts displaying network connection messages checking IP addresses against an allow list and generating employee ID numbers for a Sales department.

## What I Actually Did
I started with a basic for loop using range(3) which printed Connection could not be established three times in a row using i as the loop variable. After that I swapped out the hardcoded 3 for a variable called connection_attempts set to 3 and passed that into range() instead which gave me the exact same output but made the loop way more flexible since I could just change the value of connection_attempts instead of touching the loop itself.

Then I rebuilt the same result using a while loop this time starting connection_attempts at 0 and looping while it was less than 3 incrementing it by 1 at the end of each pass. The output looked identical to the for loop but the underlying logic was different since a for loop runs a set number of times automatically while a while loop keeps going until a condition stops being true which means you have to manually update the variable yourself inside the loop body.

After this when I came to the part which they lack that was when things started to seems bad because next I had to loop through an actual list of ip_addresses containing six IPs and print each one out using i as the loop variable which printed all six exactly in order.

Then I combined that with an if statement so for each IP in ip_addresses it would check against an allow_list containing eight approved addresses and print IP address is allowed or IP address is not allowed depending on the result. Running this against the six IPs gave me not allowed not allowed allowed not allowed allowed not allowed which lined up correctly with which addresses were actually on the allow_list.

After analyzing that I added a break statement so that as soon as an IP outside the allow_list was found the loop would stop completely and print IP address is not allowed. Further investigation of login activity required instead of just continuing through the rest of the list. Since the very first IP 192.168.142.245 was not on the allow_list the loop broke immediately and only printed that one message which showed me how break can cut off a loop the moment something suspicious shows up instead of wasting time checking everything else.

Last part was generating employee IDs for the Sales department starting at 5000 and going up to 5150 in steps of 5 using a while loop. That gave me every ID from 5000 all the way to 5150 spaced out by 5 each time. I then added an if statement inside the loop so that once i reached 5100 it would print Only 10 valid employee ids remaining as an alert right after printing 5100 itself and before continuing on to 5105 and the rest of the sequence.

## Key Takeaways
- for loops are best when you already know exactly how many times something needs to repeat
- while loops are better when you are repeating something until a condition is met rather than a fixed number of times
- break lets you stop a loop immediately which is useful for security work when you dont want to keep checking after something suspicious is already found
- putting print(i) before an if statement instead of inside it makes sure every single value gets displayed not just the one that matches the condition
- looping through IP addresses against an allow list is basically the foundation of a lot of access control logic

Completed as part of the Google Cybersecurity Certificate program.