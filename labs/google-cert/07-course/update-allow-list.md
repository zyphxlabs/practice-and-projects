## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Project Update A File Through A Python Algorithm


## What This Project Covered
This project had me building out a full algorithm that automates updating an allow list of IP addresses. At my organization access to restricted content is controlled through an allow_list.txt file and theres a separate remove_list containing IPs that should no longer have access. My job was to write code that opens that file reads it removes the flagged addresses and writes the updated list back to the same file.

## What I Actually Did
I started by assigning the file name "allow_list.txt" to a variable called import_file then opened it using a with statement paired with open() in "r" mode.

```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
```

The with statement handles closing the file automatically once im done working with it inside that block which meant I didnt have to worry about manually closing anything myself. The "r" argument specifically told Python I only wanted to read from the file not modify it yet.

After that I used .read() inside that with block to actually pull the contents of the file into a string and stored the result in a variable called ip_addresses.

```python
with open(import_file, "r") as file:
    ip_addresses = file.read()
```

At this point ip_addresses was just one long string of every IP address in the allow list separated by whitespace which wasnt very useful yet since I needed to work with each address individually.

That was when I used .split() on ip_addresses to convert it from a string into an actual list.

```python
ip_addresses = ip_addresses.split()
```

Since .split() breaks a string apart by whitespace by default this gave me a clean list where each IP address was its own separate element which made it possible to actually loop through and remove specific ones.

After analyzing that I built a for loop to iterate through every element in ip_addresses using element as the loop variable.

```python
for element in ip_addresses:
```

Inside that loop I added a conditional to check whether element was found in remove_list before doing anything else. I did this specifically because calling .remove() on something that isnt actually in the list would throw an error so the check had to come first.

```python
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)
```

Once that condition was True I applied .remove() directly to ip_addresses passing in element as the argument which meant every IP that matched something in remove_list got taken out of the allow list.

After this when I came to the part which they lack that was when things started to seems bad because ip_addresses was now a list again and I needed it back in string form to actually write it to the file. I used .join() this time with "\n" as the separator instead of a space so each IP address would land on its own line in the file.

```python
ip_addresses = "\n".join(ip_addresses)
```

Last I opened the file one more time this time using "w" mode instead of "r" so I could overwrite the existing contents with the revised list.

```python
with open(import_file, "w") as file:
    file.write(ip_addresses)
```

The "w" mode completely replaces whatever was already in the file which is exactly what I wanted here since the goal was to remove access for those flagged IPs going forward. Once this ran the file no longer contained any of the addresses from remove_list and restricted content was no longer accessible to them.

## Key Takeaways
- with statements are the standard way to handle files in Python since they close the file automatically once youre done
- .split() turns a whitespace separated string into a list which is what actually makes it possible to loop through and check individual items
- always check if an element exists in a list before calling .remove() on it or the code will throw an error
- .join() is the reverse of .split() and lets you control exactly how the final string is formatted like using "\n" to put each item on its own line
- "w" mode fully overwrites a file so it should only be used once the final version of the data is ready to be written

Completed as part of the Google Cybersecurity Certificate program.