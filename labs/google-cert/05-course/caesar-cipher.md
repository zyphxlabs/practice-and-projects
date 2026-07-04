# Caesar Cipher Decryption Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I logged in as user analyst with my home directory /home/analyst as the current working directory. All the files in my home directory had been encrypted and I needed to use Linux commands to break a Caesar cipher and decrypt everything to reveal the hidden messages inside.

## Reading the first file

I started by running ls /home/analyst to see what I was working with and it listed two files Q1.encrypted and README.txt along with a subdirectory called caesar. After that I ran cat README.txt to read the message inside and it told me all of my data had been encrypted and that to recover it I would need to solve a cipher by looking for a hidden file in the caesar subdirectory.

## Finding the hidden file

After this when I came to the caesar subdirectory that was when things started to make sense. I used cd caesar to move into it then ran ls -a to list all files including hidden ones. That revealed a file called .leftShift3 which I hadnt seen before since hidden files in Linux start with a period.

I ran cat .leftShift3 to look inside but the message came out scrambled since it was encrypted using a Caesar cipher with a shift of three letters to the left. So a letter like d actually stood for a and e stood for b. To fix this I ran cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z" which translated everything back to the original alphabet position and that finally revealed the real command I needed which was openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute.

Once I had that I ran cd ~ to go back to my home directory before moving on to the next task.

## Decrypting the file

Using the command revealed in the previous step I ran openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute to decrypt the encrypted file. This command uses AES-256-CBC as the symmetric cipher with pbkdf2 added for extra key security and the k flag set the password as ettubrute.

After running that I used ls again and saw a new file called Q1.recovered sitting in the directory which confirmed the decryption worked. I ran cat Q1.recovered to read the final message and that was when I could finally see the recovered data.

## What I took away from this

This lab gave me hands on practice with a few core Linux skills that I know ill keep using going forward:

- Listing hidden files using ls -a
- Decrypting a Caesar cipher using the tr command to shift characters back
- Decrypting an encrypted file using openssl with aes-256-cbc

This needs the most urgent attention when it comes to understanding since encryption and decryption are foundational to almost everything else in security work moving forward.

— Completed as part of the Google Cybersecurity Certificate program.