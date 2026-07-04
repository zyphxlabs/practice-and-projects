# Access Control Worksheet Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I reviewed an event log to investigate a security incident and fill out an access control worksheet covering notes issues and recommendations. The goal was to look at authorization and authentication details from the log and figure out what went wrong and how it could be prevented going forward.

## What I found in the notes

The event took place on 10/03/23 and the user tied to it was listed as Legal slash Administrator. The IP address of the computer used to login was 152.207.255.255. Event logs like this are usually where you start since they can point you toward the who what and why of an incident.

## The authorization issues

After this when I came to the part where I dug into who this user actually was that was when things started to look bad. Robert Taylor Jr was a contractor who had admin access to the system. His contract had ended back in 2019 but his account was still active enough to access payroll systems in 2023. That is a four year gap where an account that should have been deactivated was sitting there with admin level access to sensitive payroll data.

This tells me the issue here wasnt some sophisticated attack it was a misconfigured or misused system that never cleaned up old accounts. A former contractor still having active credentials years after their contract ended is exactly the kind of thing that puts a business at risk without anyone noticing until its too late.

## My recommendations

- User accounts should expire after 30 days
- Contractors should have limited access to business resources
- Enable multi factor authentication (MFA)

## What I took away from this

It's worth noting that even though Robert Taylor Jr looks like the obvious threat actor here it's possible he wasnt the one actually responsible for the login. People reuse credentials across different platforms all the time and if those credentials get compromised somewhere else an attacker could use them to get into a system just like this one. That is exactly why access controls like password policies limited file permissions and MFA matter so much since they protect a business even when a login looks legitimate on paper.

This lab really showed me how easy it is to lose track of users especially contractors once their work is done. This needs the most urgent attention since an unmonitored account with admin access is one of the simplest ways for a business to end up in a security incident without ever seeing it coming.

— Completed as part of the Google Cybersecurity Certificate program.