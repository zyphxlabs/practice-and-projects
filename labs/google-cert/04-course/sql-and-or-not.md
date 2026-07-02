# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Apply AND OR and NOT operators to build complex SQL filters

I worked through this lab to practice combining conditions in SQL queries using AND OR and NOT so I could filter the organization database for more specific security related information across the log_in_attempts and employees tables

I started with the after hours failed login investigation my team wanted to know about failed logins that happened after 18:00 so I ran SELECT * FROM log_in_attempts WHERE login_time > '18:00' AND success = FALSE combining a time filter with a success filter using AND and this returned 19 failed login attempts that occurred after 18:00

After this when I came to the suspicious event on 2022-05-09 that was when I needed to also pull data from the day before so I used OR instead of AND since I needed either date to match I ran SELECT * FROM log_in_attempts WHERE login_date = '2022-05-09' OR login_date = '2022-05-08' and this returned 75 login attempts across those two days

Then I moved into investigating logins that did not originate in Mexico since the country field had entries with both MEX and MEXICO I had to use NOT combined with LIKE and the pattern MEX% to catch both variations I ran SELECT * FROM log_in_attempts WHERE NOT country LIKE 'MEX%' and this returned 144 login attempts made outside of Mexico

After analyzing the login data I switched over to the employees table for the remaining tasks first I needed employees in the Marketing department located in the East building so I combined AND with LIKE running SELECT * FROM employees WHERE department = 'Marketing' AND office LIKE 'East%' and the first username returned was elarson

On top of that my team needed employees in either the Finance or Sales department for a separate update so I ran SELECT * FROM employees WHERE department = 'Finance' OR department = 'Sales' making sure to write out the full department condition on both sides even though it was the same column and the first username returned in the Sales department was lrodriqu

Finally I needed everyone who was not in the Information Technology department since that department had already been updated so I ran SELECT * FROM employees WHERE NOT department = 'Information Technology' and this returned 161 employees who are not in the Information Technology department

Queries I used throughout this lab

- WHERE login_time > '18:00' AND success = FALSE to combine a time and status filter
- WHERE login_date = 'X' OR login_date = 'Y' to match either of two dates
- WHERE NOT country LIKE 'MEX%' to exclude a pattern instead of matching one
- WHERE department = 'Marketing' AND office LIKE 'East%' to combine department and location
- WHERE department = 'Finance' OR department = 'Sales' to match either department
- WHERE NOT department = 'Information Technology' to exclude a specific department

This lab showed me how much more precise I can get with SQL once I start combining conditions with AND OR and NOT instead of relying on a single filter since real investigations almost always depend on more than one factor at the same time like a failed login combined with a specific time or a department combined with a specific building location

— Completed as part of the Google Cybersecurity Certificate program.