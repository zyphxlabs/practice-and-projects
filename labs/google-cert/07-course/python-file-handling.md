## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Import And Parse A Text File


## What This Lab Covered
This lab had me working with file handling in Python which is how you actually pull real log files into a program instead of just typing strings directly into the code. The scenario had me importing a security log file reading it splitting it into lines appending a missing entry and then creating a brand new text file to store a list of allowed IP addresses.

## What I Actually Did
I started by writing the first line of a with statement using open() with import_file set to "data/login.txt" and "r" as the mode to open it for reading.

```python
with open(import_file, "r") as file:
```

After that I completed it by using .read() to actually pull the contents into a variable called text and displayed it.

```python
with open(import_file, "r") as file:
    text = file.read()

print(text)
```

The output was one long string containing every line from login.txt with usernames IP addresses login times and dates all packed together.

Next I used .split() on that same text to break it up into a list of individual strings instead of one giant block.

```python
print(text.split())
```

That was when I noticed the real difference between the two outputs since before splitting it was all one string and after splitting it turned into a list where each entry was its own separate piece.

After analyzing that I moved on to appending a missing entry to the log file for jrafael with IP 192.168.243.140 at 4:56:27 on 2022-05-09. I opened the file using "a" as the mode this time instead of "r" so it would add on rather than overwrite.

```python
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

with open(import_file, "a") as file:
    file.write(missing_entry)

with open(import_file, "r") as file:
    text = file.read()

print(text)
```

After running that the missing_entry showed up right at the very end of the file confirming that "a" mode adds new content after everything that was already there instead of replacing it.

After this when I came to the part which they lack that was when things started to seems bad because next I had to build a completely new file from scratch instead of just editing an existing one. I set import_file to "data/allow_list.txt" and stored a string of eleven approved IP addresses in ip_addresses then displayed both just to confirm they held the right values before writing anything.

Then I opened the new file using "w" mode which creates the file if it does not exist yet and writes fresh content into it.

```python
with open(import_file, "w") as file:
    file.write(ip_addresses)
```

Last I added a second with statement using "r" mode to read the file back and confirm the IP addresses had actually been written correctly.

```python
with open(import_file, "r") as file:
    text = file.read()

print(text)
```

The output matched the original ip_addresses string exactly which confirmed the file was created and written to successfully.

## Key Takeaways
- the with statement handles opening and closing a file automatically so you dont have to remember to close it yourself
- "r" mode is for reading "a" mode is for appending without erasing existing content and "w" mode is for writing which creates the file if it doesnt exist or overwrites it if it does
- .read() pulls the entire file in as one string while .split() breaks that string down into a list of individual lines
- appending with "a" always adds new content to the end of the file rather than replacing what was already there
- being careful about which mode you open a file in matters a lot since "w" will wipe out existing content if youre not paying attention

Completed as part of the Google Cybersecurity Certificate program.