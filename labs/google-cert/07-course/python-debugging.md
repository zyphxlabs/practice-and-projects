## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Debug Python Code

## What This Lab Covered
This lab was all about debugging which is basically the process of finding whats broken in code and fixing it. Each task gave me broken code that I had to run identify the error type on and then correct whether that was a syntax error a logic error or an exception.

## What I Actually Did
First task was a for loop missing a colon at the end of the header.

```python
for i in range(10)
    print("Connection cannot be established")
```

Running it threw a SyntaxError right away and once I looked closer the issue was just the missing colon after range(10). Adding it back in fixed it immediately and the loop printed the message ten times like it was supposed to.

Second task had a list of usernames where the fourth entry zdutchma was missing its closing quotation mark and there was also a missing comma between it and the next username esmith.

```python
usernames_list = ["djames", "jpark", "tbailey", "zdutchma "esmith",, "srobinso", "dcoleman", "fbautist"]
```

That threw a SyntaxError too since Python had no way of telling where one string ended and the next began. I fixed it by closing the quote properly and adding the missing comma so it read "zdutchma", "esmith", which resolved the error.

Third task was a print statement using .upper() that was just missing its closing parenthesis.

```python
print("update needed".upper()
```

This threw a SyntaxError: unexpected EOF while parsing which is Pythons way of saying it ran out of code before finding something it expected like a closing bracket. Adding the missing ) fixed it and it printed UPDATE NEEDED correctly.

Fourth task had three separate issues stacked in the same block of code. The if statement was using a single = instead of the == comparison operator the print() statement inside the if block was missing its indentation and the for loop referenced username_list instead of the actual variable usernames_list.

```python
for name in username_list:
    if name = username:
    print("The user is an approved user")
```

I fixed all three one at a time starting with the misspelled variable then the comparison operator and finally the indentation. After all three fixes the loop correctly found esmith in the list and printed The user is an approved user.

Fifth task involved an IndexError caused by trying to access usernames_list[4] when checking against the wrong index for the final element.

```python
if username == usernames_list[5]:
```

Since usernames_list only had five elements the valid indices only went up to 4 so index 5 was out of range. I fixed it by changing 5 to 4 which correctly matched eraab as the last username in the list.

Sixth task combined a missing colon on a with statement header along with an exception caused by calling a string method backwards.

```python
with open(import_file, "r") as file
    ip_addresses = file.read()

ip_addresses = split.ip_addresses()
```

The first issue was the missing colon after the with statement header. The second was that split.ip_addresses() has the method and the variable reversed since .split() has to be called on the string variable itself not the other way around. I fixed it by adding the colon back and rewriting it as ip_addresses.split() which resolved both issues and let the rest of the removal logic run correctly.

Last task was a logic error rather than a syntax issue or exception. The code was mapping operating systems to the wrong patch dates using incorrect list indices.

```python
if system == "OS 1":
    print("Patch date:", patch_schedule[2])
elif system == "OS 2":
    print("Patch date:", patch_schedule[0])
elif system == "OS 3":
    print("Patch date:", patch_schedule[1])
```

Testing this with system set to "OS 2" returned March 1st which was wrong since that date belonged to OS 1. I fixed the indices so OS 1 correctly pointed to patch_schedule[0] OS 2 to patch_schedule[1] and OS 3 to patch_schedule[2] which lined everything up correctly with April 1st now showing for OS 2.

## Key Takeaways
- Python stops at the very first error it hits so if a cell has multiple issues you often only see one error message at a time and have to fix them in order
- syntax errors are usually about punctuation like a missing colon missing comma or missing closing parenthesis
- exceptions often come from small things like misspelled variable names or calling a method on the wrong object
- logic errors are the trickiest because the code runs without crashing at all it just gives you the wrong answer which means you have to actually trace through the logic to catch it
- rerunning the code after every single fix is the best way to confirm the problem is actually solved instead of assuming it is

Completed as part of the Google Cybersecurity Certificate program.