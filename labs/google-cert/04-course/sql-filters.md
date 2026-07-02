# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Apply filters to SQL queries using WHERE and LIKE

I worked through this lab to practice adding filters to SQL queries so I could pull specific information out of the organization database instead of scanning through every row manually

Before writing any queries I ran DESCRIBE machines and DESCRIBE employees to check the structure of both tables and confirm the exact column names and data types I would need to use in my SELECT statements

I started with SELECT device_id, operating_system FROM machines to get a list of all organization machines and their operating systems and this returned 200 rows total from the machines table

After this when I came to filtering for a specific operating system that was when I ran my first query using WHERE I used SELECT device_id, operating_system FROM machines WHERE operating_system = 'OS 2' to find only the machines running OS 2 since those needed an update and this returned 80 machines in the database using that operating system

Then I moved into the employees table to find people in specific departments I ran SELECT * FROM employees WHERE department = 'Finance' and the employee_id of the first row returned was 1003 after that I modified the query to SELECT * FROM employees WHERE department = 'Sales' and found there are 33 employees working in the Sales department

After analyzing the department data my team needed to identify which employee used a specific office since a machine in South-109 had an issue I ran SELECT * FROM employees WHERE office = 'South-109' and found the employee using that machine has the user ID jlansky so they could be alerted directly about the issue

On top of that my team then found out the issue was actually affecting the entire South building not just one office so I used the LIKE operator with a wildcard to broaden the search I ran SELECT * FROM employees WHERE office LIKE 'South%' using the percent sign as a fill in the blank so it would match any office starting with South like South-109 or South-210 and the first employee listed in the South building belongs to the Finance department

Queries I used throughout this lab

- DESCRIBE machines and DESCRIBE employees to check table structure before querying
- SELECT device_id, operating_system FROM machines to list all machines
- WHERE operating_system = 'OS 2' to filter machines by operating system
- WHERE department = 'Finance' and WHERE department = 'Sales' to filter employees by department
- WHERE office = 'South-109' to find a specific office
- WHERE office LIKE 'South%' to match all offices in the South building using a wildcard

This lab showed me how much faster it is to use WHERE and LIKE to filter data directly in the query instead of pulling everything and scanning it by hand especially in a real scenario like this one where I needed to quickly find which machines needed updates and which employees needed to be alerted about an issue affecting their building

— Completed as part of the Google Cybersecurity Certificate program.