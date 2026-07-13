## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Create Another Algorithm


## What This Lab Covered
This lab combined file handling with loops and conditionals to build a full algorithm that parses a text file of allowed IP addresses and removes the ones that no longer have access. The scenario worked with a file called allow_list.txt and a remove_list containing four IPs that needed to be taken out.

## What I Actually Did
I started by displaying both import_file which was "allow_list.txt" and remove_list which contained 192.168.97.225 192.168.158.170 192.168.201.40 and 192.168.58.57 just to confirm what I was working with before touching anything.

```python
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
print(import_file)
print(remove_list)
```

After that I opened the file using a with statement and "r" mode then used .read() to pull everything into a variable called ip_addresses and displayed it.

```python
with open(import_file, "r") as file:
    ip_addresses = file.read()

print(ip_addresses)
```

The output at this point was still just one long string so comparing it against remove_list wasnt really practical yet.

That was when I used .split() to convert ip_addresses from a string into an actual list which let me work with each IP individually instead of scanning through one giant block of text.

```python
ip_addresses = ip_addresses.split()
print(ip_addresses)
```

After analyzing that I built a for loop using element as the loop variable to go through ip_addresses and print each one just to confirm the loop was working correctly before adding any logic to it.

```python
for element in ip_addresses:
    print(element)
```

Then I added an if statement inside that same loop so that if element was found in remove_list it would get removed from ip_addresses using .remove().

```python
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

print(ip_addresses)
```

After this when I came to the part which they lack that was when things started to seems bad because ip_addresses was still a list at this point and I needed it back as a string in order to actually write it into the file. I used .join() with a space character to merge everything back into one string then opened the file again using "w" mode to overwrite it with the updated list.

```python
ip_addresses = " ".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

To confirm it actually worked I read the file back in one more time and displayed it and the four removed IPs were gone while everything else remained exactly as it should.

```python
with open(import_file, "r") as file:
    text = file.read()

print(text)
```

Last I took all of that code and wrapped it into a single function called update_file() that takes in import_file and remove_list as parameters so the entire process could be reused with a single call instead of rerunning every step manually.

```python
def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)

    ip_addresses = " ".join(ip_addresses)

    with open(import_file, "w") as file:
        file.write(ip_addresses)
```

I tested the finished function by calling update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"]) then reading the file one final time to confirm those three new IPs were removed successfully as well.

```python
update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

with open("allow_list.txt", "r") as file:
    text = file.read()

print(text)
```

## Key Takeaways
- .split() and .join() work as opposites of each other one breaks a string into a list and the other merges a list back into a string
- looping through a list while removing items from it needs to be handled carefully since it can skip elements if not done right
- "w" mode completely overwrites a file so it has to be used only after youre sure the updated content is correct
- wrapping the entire read modify write process into one function makes the whole algorithm reusable for any file and any remove_list without rewriting the logic every time
- this kind of automation is basically how real access control lists get maintained at scale instead of manually editing a file by hand every time someone loses access

Completed as part of the Google Cybersecurity Certificate program.