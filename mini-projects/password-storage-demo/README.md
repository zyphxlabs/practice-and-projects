# Password storage: plaintext vs aes vs bcrypt, then cracking the hashes for real

Everyone keeps saying use bcrypt not plaintext but nobody really shows the actual gap so i built a small project to check it myself

## What i built

Stored the same password 3 different ways

Plaintext is basically the password stored raw with no protection at all this is just to show the worst case

Aes encryption is when the password gets encrypted with a key this one is a trap i put on purpose because encryption is reversible so it looks safe since you cant read it directly but if that key ever leaks every password comes back instantly. Passwords should never be recoverable by anyone not even the system storing them, that's basically why hashing exists instead of encryption for this

Bcrypt is a slow hash built specifically for passwords i used cost factor 12 for it

Then i also made a sha256 hash of the same password sha256 is a fast hash meant for general stuff not passwords so i could compare the two properly

## How i tested it

Password used: Passw0rd123
Wordlist: rockyou.txt which has 14344392 passwords in it
Tool used: john the ripper
Ran both hashes through it back to back on the same machine

## What actually happened

Sha256 got cracked instantly, under 1 second running at 10813000 guesses per second

Bcrypt was only doing 10.8 guesses per second and didnt crack at all in the time i let it run johns own eta pushed it weeks out

So basically thats around a 1000000x difference in speed for cracking the exact same password on the exact same machine

## What this actually means

The password i used was weak on purpose since it exists in the wordlist so this isnt saying bcrypt makes a weak password unbreakable given enough time an attacker still gets there eventually. What bcrypt actually does is buy time the same guess a fast hash does in a split second takes bcrypt a million times longer per guess. That basically means the difference between someone cracking your password before you even notice vs it taking long enough that you actually get a chance to catch it and reset it

So slow hashing isn't just something people say to sound like they know security its an actual rate limit built into the hash function itself this is what that looks like as real numbers

## Raw hash output

```
testuser:fa870a2658fc49993579f7471d86d0a54ca1267e52d3f9be2395d6f3689bdcc7
```
Sha256 hash of the password

```
testuser:$2b$12$nzxmCQsaoFj66ey.tbLEpeu0bgP37x3mAhfRClbK9lrkKUF1A/L6y
```
Bcrypt hash of the same password, cost factor 12

## Files in this folder

Password_storage_demo.py this generates all 3 storage methods and writes the hash files john needs

Sha256_hash.txt and bcrypt_hash.txt the actual hash outputs in the format john reads

Terminal-output.png the screenshot of john the ripper actually cracking both hashes

Made for learning and portfolio purposes not something youd actually use in production