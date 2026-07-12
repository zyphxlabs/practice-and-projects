## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Assign Python Variables


## What This Lab Covered
This lab had me working through variable assignment which is basically how you store information in Python so you can use it later on. The scenario was based around writing code to automate analysis of login attempts on a device and I had to build out variables for things like the device ID the list of approved usernames the max login attempts allowed and the current attempts a user has made.

## What I Actually Did
I started by assigning the device_id variable to the string "72e08x0" then printed it and it came back exactly as expected. After that I used the type() function to check what data type device_id actually was and stored that in a new variable called device_id_type which when I printed it out showed <class 'str'> confirming the device ID was being stored as a string.

Next I moved on to building the username_list variable which held the five approved usernames madebowa jnguyen tbecker nhersh and redwards. I printed the list and got back all five names in a Python list format. Then I checked the type of username_list the same way I did with device_id and this time the output was <class 'list'> which made sense since it was holding multiple values instead of just one.

After that I had to reassign username_list because a new employee lpope had been added to the approved list. I printed the list before the update and then again after so I could see the difference side by side. The first print showed the original five names and the second print showed all six including lpope which really showed me how reassigning a variable just overwrites whatever was stored there before.

Then I moved into numeric variables starting with max_logins set to 3 and login_attempts set to 2. Checking the type on both of these returned <class 'int'> for each one. After that I used the <= operator to compare login_attempts to max_logins and since 2 is less than or equal to 3 the output came back True meaning the user had not gone over the allowed attempts yet.

I then reassigned login_attempts to 4 just to see what would happen when someone actually exceeded the limit and reran the same comparison. This time the output was False since 4 is not less than or equal to 3 which showed me how the same line of code can give a completely different result just by changing the value stored in one variable.

Last task was creating login_status and assigning it the Boolean value False to represent a user not currently being logged in. Checking its type gave me <class 'bool'> confirming Booleans are their own separate data type in Python.

## Key Takeaways
- Variables let you store and reuse values instead of typing them out over and over
- type() tells you exactly what kind of data you are working with whether that is str list int or bool
- Reassigning a variable completely replaces whatever value it held before
- The <= operator is useful for building logic that checks limits like login attempts
- Booleans are their own data type and are what a lot of security logic ends up relying on when you need a True or False result

Completed as part of the Google Cybersecurity Certificate program.