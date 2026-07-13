## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Use Regular Expressions To Find Patterns


## What This Lab Covered
This lab had me working with the re module in Python which is used for building regular expressions. The scenario had two parts one where I had to pull out device IDs starting with a specific character combination from a log and another where I had to extract valid IP addresses out of a messier login log and cross check them against a flagged list.

## What I Actually Did
I started by importing the re module since none of the regex functions work without it.

```python
import re
```

Then I displayed the devices string just to see what I was actually working with which was a long line of alphanumeric device IDs separated by spaces.

After that I built target_pattern using r15\w+ so it would match anything starting with r15 followed by one or more word characters.

```python
target_pattern = "r15\w+"
print(re.findall(target_pattern, devices))
```

Running that against devices pulled out r151dm4 r15xk9h r15u9q5 and r159r1u which were exactly the four device IDs that needed the operating system update.

After this when I came to the part which they lack that was when things started to seems bad because the log_file for the IP address portion was way messier than the device string. I displayed it first to get a sense of what I was dealing with and it had usernames dates login times and IP addresses all packed into one long string with some of the IP addresses clearly corrupted with extra digits.

I built my first pattern using exact three digit segments.

```python
pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(pattern, log_file))
```

This only pulled out the addresses where every single segment happened to be exactly three digits long which meant it completely skipped over valid ones like 192.168.22.115 just because one segment only had two digits.

That was when I updated the pattern to use + instead so each segment could be any number of digits.

```python
pattern = "\d+\.\d+\.\d+\.\d+"
print(re.findall(pattern, log_file))
```

This time findall() grabbed everything including the badly corrupted entries like 1923.1689.3.24 and 19245.168.2345.49 which are not real IP addresses at all they just happened to have periods in similar positions.

After analyzing that problem I rebuilt the pattern one more time using curly brackets instead so each segment was restricted to somewhere between one and three digits.

```python
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)
print(valid_ip_addresses)
```

This time it correctly filtered out the badly malformed entries and returned a clean list of nine valid addresses including 192.168.152.148 192.168.22.115 192.168.190.178 192.168.213.128 192.168.96.200 192.168.247.153 192.168.174.117 192.168.148.115 and 192.168.168.144. I did notice one entry 192.168.103.10654 still got partially picked up as 192.168.103.106 since the regex has no way of knowing the real segment kept going past three digits which is something worth keeping in mind when relying on this pattern alone.

Last I displayed flagged_addresses which contained four IPs that had been previously flagged for unusual activity.

```python
flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]
```

I looped through valid_ip_addresses using address as the loop variable and checked each one against flagged_addresses.

```python
for address in valid_ip_addresses:
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")
```

The ones that matched 192.168.190.178 192.168.96.200 192.168.174.117 and 192.168.168.144 all printed as flagged for further analysis while every other address in the list printed that it did not require further analysis.

## Key Takeaways
- \w+ is useful for matching alphanumeric strings of unknown length like device IDs
- \d matches digits but on its own it forces an exact character count which can miss valid data
- using + after \d loosens the match too much and starts pulling in corrupted or invalid data
- curly brackets like {1,3} give you precise control over how many digits are allowed per segment which is the right balance for something like IP validation
- regex without proper anchoring can still partially match malformed data so the output always needs a second look before trusting it fully
- looping through a list of extracted values and checking them against a flagged list is a simple but effective way to automate triage

Completed as part of the Google Cybersecurity Certificate program.