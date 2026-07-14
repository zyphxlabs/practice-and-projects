## Course 8 Activity — Log Analysis with NotebookLM

Google Cybersecurity Certificate — Course 8


## What I Did

For this activity I copied the log data into NotebookLM and used it to go through each entry and figure out what was actually going on in the environment. I started with the basic prompts like what do these logs tell me about user activity and then moved into asking it to flag anything that looked out of the ordinary from a security perspective.

## Findings

After this when I came to the part which they lack that was when things started to seems bad. Going through the log line by line with NotebookLM I asked it to walk me through each event in plain terms so I could understand what was normal daily activity and what actually needed attention.

The entry at 08:30:40 where admin logged in successfully from an external IP address 203.0.113.25 marked as an unusual location is the one that needs the most urgent attention and should be escalated right away. What makes this one stand out is that the same admin account had already logged in from the internal network at 08:00:15 so seeing it log in again from an outside unusual location a half hour later is a strong sign the account may have been compromised. An admin account has full access so if someone outside the company got into it they could do a lot of damage before anyone notices.

The entry at 08:20:20 where John Doe copied the budget_2026_final.xlsx file from the finance folder to public_share is also concerning. Financial data being moved to a public share means anyone could potentially access it which is a data exposure risk even if it turns out to be accidental.

The three failed login attempts from the guest account between 08:15:00 and 08:15:10 from IP 10.0.0.100 look like someone trying to brute force their way in but since it stopped after three tries and guest accounts usually have limited access this one is lower priority compared to the admin login issue.

On top of that least privilege and separation of duties were never implemented so every single employee had access to all internal data including cardholder data and customer PII which is a huge problem I observed. This is not something that came from one log entry it is a structural issue across the whole environment and it means any one compromised account like the admin one above could reach data it never should have been able to touch in the first place.

## Recommendations

- Escalate the 08:30:40 admin login from external IP immediately for account compromise investigation
- Force a password reset and enable multi factor authentication on the admin account
- Review why budget_2026_final.xlsx was copied to public_share and restrict access if not intentional
- Investigate the repeated failed guest login attempts as a possible brute force attempt
- Implement least privilege access controls across all employee accounts
- Apply separation of duties so no single role can access cardholder data and customer PII without justification

---
Completed as part of the Google Cybersecurity Certificate program.