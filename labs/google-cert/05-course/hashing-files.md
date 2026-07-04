# Hashing Files Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I logged in as user analyst with /home/analyst as my home directory. Inside there were two files file1.txt and file2.txt which looked like they contained the same data. My job was to figure out if they were actually identical or different by generating hashes and comparing them manually using Linux commands.

## Looking at the files first

I ran ls to see what was in the directory and it listed file1.txt and file2.txt. Then I used cat file1.txt and cat file2.txt to look at the contents of each one side by side. Both files showed the exact same string starting with X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H* so visually there was no difference at all between them.

## Generating the hashes

After this when I came to the hashing part that was when things actually got interesting. I ran sha256sum file1.txt and got the hash 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267 for file1.txt. Then I ran sha256sum file2.txt and got a completely different hash 2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b for file2.txt.

Even though cat showed the same content on screen the hash values told a totally different story. This confirmed the files were not actually identical even though they appeared that way at first glance.

## Comparing the hashes

Next I wrote each hash out to its own file using sha256sum file1.txt >> file1hash and sha256sum file2.txt >> file2hash. Once I had both saved I used cat file1hash and cat file2hash to display them and could see right away the values were different.

To pin down exactly where they differed I ran cmp file1hash file2hash and the output told me the files differ at char 1 line 1. So the hashes were different from the very first character which makes sense given how different the full hash strings looked.

## What I took away from this

This lab really drove home why relying on how a file looks isnt enough when you need to verify integrity. A few things I know ill carry forward from this:

- Using sha256sum to generate a hash for a file
- Writing hash output to a separate file for comparison
- Using cmp to find the exact point where two files differ

On top of that this showed me why hashing matters so much in security work since a malicious file could look identical to a legit one but the hash would immediately expose the difference which is a huge problem if youre not checking for it. This needs the most urgent attention anytime file integrity is in question.

— Completed as part of the Google Cybersecurity Certificate program.