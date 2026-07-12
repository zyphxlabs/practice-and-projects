## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Work With Strings In Python


## What This Lab Covered
This lab had me working with strings which analysts end up using constantly for things like employee IDs device IDs and URLs. The scenario walked through updating an employee ID to a standardized format extracting specific characters from a device ID and pulling apart different components of a URL.

## What I Actually Did
I started with employee_id set to 4186 as an integer and checked its type first which came back as int. Then I converted it to a string using str() and checked the type again which now returned str confirming the conversion actually worked.

After this when I came to the part which they lack that was when things started to seems bad because next I had to check the length of employee_id using len() and write a conditional that would print a message if the length was less than 5. Since 4186 only has four characters the condition was True and it printed This employee ID has less than five digits. It does not meet length requirements.

That was when I built on that same logic and used concatenation to actually fix the problem instead of just flagging it. I wrote an if statement so that when the length was less than 5 it would reassign employee_id by adding the letter E in front of it using the + operator. Running it gave me E4186 as the final five character ID which met the new standardization requirement.

Next I moved into extracting characters from a device_id set to "r262c36". I pulled the fourth character using index position 3 since Python indexing starts at 0 and got back 2 which was correct. After that I used slicing with device_id[0:3] to grab the first three characters and got back 'r26'.

Then I worked with a url variable set to "https://exampleURL1.com". First I sliced url[0:8] to pull out the protocol along with the :// which gave me https://. After that I used the .index() method to find where .com started inside the string which returned position 19 and I stored that in a variable called ind so I could reuse it instead of hardcoding the number again.

Using ind I sliced url[ind:ind+4] which correctly pulled out .com since the extension is exactly four characters long. Last I extracted the actual website name using url[8:ind] which returned exampleURL1 by slicing everything between the end of the protocol and the start of the domain extension.

## Key Takeaways
- str() converts a number into a string so you can work with it using string specific methods like len() and slicing
- len() is useful for validating that data like an employee ID actually meets a required format
- string concatenation with + lets you fix formatting issues by adding characters directly onto an existing string
- indexing starts at 0 in Python so the fourth character is actually at position 3 not 4
- .index() combined with slicing is a solid way to pull specific components out of a longer string like a URL without hardcoding every position by hand

Completed as part of the Google Cybersecurity Certificate program.