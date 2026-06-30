# Network Hardening Risk Assessment — Google Cybersecurity Certificate

## Course
Google Cybersecurity Certificate — Course 3 Detect and Respond to Cybersecurity Incidents

## Scenario
I worked through a scenario where I am a security analyst for a social media organization that recently went through a major data breach which compromised customer personal information like names and addresses so i was assigneedd with the task  to inspect the network and figure out what hardening practices could be put in place to stop this from happening again.

## What I found
After inspecting the organization’s network I found four major vulnerabilities Employees were sharing passwords with each other which means there is no way to track who actually accessed what The admin password for the database was still set to the default password which is an easy target for anyone trying to brute force their way in The firewalls had no rules in place to filter traffic coming in or out of the network at all. And on top of that multifactor authentication was not being used anywhere which is a huge problem I observed since it removes a major layer of protection against stolen or guessed credentials.

After this when I came to the part where I realized none of these four issues were addressed at the same time that was when things started to seems bad because each one of these on its own is risky but together they make the network an easy target.

## Recommended hardening methods
I am recommending the following hardening practices to address what I found

- Enforce a strict password policy so employees can no longer share passwords and each login is tied to one individual
- Change the default admin password on the database immediately to a unique strong password
- Set up firewall rules to filter both inbound and outbound traffic so unauthorized traffic cannot pass through
- Implement multifactor authentication across the organization so a password alone is not enough to access a system

## Why these methods are effective
Changing the default admin password and enforcing a real password policy directly closes the gap that allowed easy guessing or shared access in the first place. This is something that should be done once immediately and then maintained going forward as part of normal account management.

Firewall rules need regular maintenance and should be checked and updated consistently to stay ahead of new threats since attackers are always changing how they try to get in. Multifactor authentication is mostly a one time setup but it adds a second layer of verification so even if a password is compromised the attacker still cannot get in without the second factor.

This needs the most urgent attention since right now there is nothing stopping another breach from happening the exact same way it did before.

— Completed as part of the Google Cybersecurity Certificate program.