# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Use SQL joins to connect the machines employees and log_in_attempts tables

I worked through this lab to practice using SQL joins to connect related tables in the organization database since a lot of real investigations need data pulled from more than one table at the same time

I started by running SELECT * FROM machines on its own just to confirm that table only had hardware information like device_id and operating_system with no employee names attached which showed me why a join was actually needed to connect machine data to a specific person

After this when I came to building the actual join that was when I used an inner join between machines and employees on the shared device_id column I ran SELECT * FROM machines INNER JOIN employees ON machines.device_id = employees.device_id and this returned 185 rows since an inner join only keeps rows where the device_id matches in both tables and drops anything that does not have a match on either side

Then I moved into testing a left join so I could see every machine even if it was not assigned to anyone I ran SELECT * FROM machines LEFT JOIN employees ON machines.device_id = employees.device_id and the last record returned had NULL in the username column which confirmed that machine was not currently assigned to an employee

After analyzing the left join results I flipped it around and ran a right join instead so I could see every employee even if they did not have a machine assigned to them I ran SELECT * FROM machines RIGHT JOIN employees ON machines.device_id = employees.device_id and the last record returned had a username of areyes confirming that employee showed up even without needing a matching machine record

On top of that I learned that most analysts actually prefer sticking with LEFT JOIN and just reordering the tables instead of switching to RIGHT JOIN since it reads more naturally left to right and avoids having to think backwards through the logic

Finally I needed to connect login activity to actual employees so I ran an inner join between employees and log_in_attempts using the shared username column instead of device_id I ran SELECT * FROM employees INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username and this returned 200 records showing every login attempt tied directly back to the employee who made it

Queries I used throughout this lab

- INNER JOIN machines and employees ON device_id to match machines to their assigned employee
- LEFT JOIN machines and employees ON device_id to keep every machine even without an assigned user
- RIGHT JOIN machines and employees ON device_id to keep every employee even without an assigned machine
- INNER JOIN employees and log_in_attempts ON username to connect login activity back to specific employees

This lab really tied together everything I had learned so far in SQL since being able to join tables on a shared column like device_id or username is exactly how a real investigation works when the information you need is split across multiple tables instead of sitting in one place

— Completed as part of the Google Cybersecurity Certificate program.