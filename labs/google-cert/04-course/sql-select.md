# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Use SELECT FROM and ORDER BY to query the organization database

I worked through this lab to practice running SQL queries against the organization database using the machines and log_in_attempts tables to find devices that needed updates and to check login activity for anything unusual

I started with SELECT * FROM machines to pull all the data from the machines table and got back 200 rows which included device_id operating_system email_client OS_patch_date and employee_id for every device in the system

After this when I came to narrowing things down that was when I ran SELECT device_id, email_client FROM machines to focus only on the email client running on each device and the third row returned showed Email Client 2

Then I ran SELECT device_id, operating_system, OS_patch_date FROM machines to check the operating systems and their last patch dates since old patch dates are exactly how you identify vulnerable machines that could be exploited and the first entry showed a patch date of 2021-09-01

After analyzing the machines table I moved into the log_in_attempts table to look for unusual login activity I ran SELECT event_id, country FROM log_in_attempts to check where login attempts were coming from and confirmed no login attempts were made from Australia which mattered because a login from outside expected regions like the United States Canada or Mexico would be a red flag for credential theft

Next I ran SELECT username, login_date, login_time FROM log_in_attempts to check login times since attackers often log in at unusual hours like 3am assuming no one will notice and the username returned in the fifth row was jrafael

I also ran SELECT * FROM log_in_attempts to get the full picture of all login attempts across every column which showed me scanning 200 rows manually is doable for learning but not realistic for a real breach with millions of entries which is why the WHERE clause will matter later to filter out noise instead of scanning everything by hand

On top of that I used ORDER BY to organize the login data properly I ran SELECT * FROM log_in_attempts ORDER BY login_date and the first record returned had a username of ivelasco with a login date of 2022-05-08 then I added login_time to the ORDER BY clause so it would sort by date first and then by time for any entries on the same date and the first record returned this time had a username of bsand with a login time of 00:19:11

Queries I used throughout this lab

- SELECT * FROM machines to pull all device data
- SELECT device_id, email_client FROM machines to narrow to specific columns
- SELECT device_id, operating_system, OS_patch_date FROM machines to check patch dates
- SELECT event_id, country FROM log_in_attempts to check login locations
- SELECT username, login_date, login_time FROM log_in_attempts to check login timing
- SELECT * FROM log_in_attempts ORDER BY login_date, login_time to sort chronologically

This lab gave me my first real practice writing SQL queries and showed me how something as simple as sorting login attempts by date and time or checking which country a login came from can immediately surface red flags that would be almost impossible to catch by just eyeballing raw data especially once the dataset gets bigger than 200 rows

— Completed as part of the Google Cybersecurity Certificate program.