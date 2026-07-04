# Vulnerability Assessment Report Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I wrote up a vulnerability assessment report for a database server dated 1st January 20XX. The server runs a powerful CPU with 128GB of memory on the latest version of Linux and hosts a MySQL database management system. It connects to other servers on the network using IPv4 and relies on SSL slash TLS encrypted connections for security. My job was to look at the current access controls and assess the risk around them.

## The scope and purpose

The scope of this assessment was focused specifically on the current access controls of the system and covered a period of three months from June 20XX to August 20XX. I used NIST SP 800-30 Rev 1 to guide the risk analysis for this report. The purpose of the server itself is to act as a centralized system storing customer campaign and analytic data which later gets used to track performance and personalize marketing efforts. Since this data feeds directly into marketing operations securing it properly is critical.

## What I found in the risk assessment

After this when I came to the part where I broke down the threat sources that was when things started to look bad. A hacker obtaining sensitive information through exfiltration scored a 3 for likelihood and a 3 for severity landing on a risk score of 9 which is the highest out of everything I looked at. An employee disrupting mission critical operations scored a 2 for likelihood and a 3 for severity giving a risk score of 6. A customer altering or deleting critical information scored lower at a 1 for likelihood and a 3 for severity coming out to a risk score of 3.

The approach I took considered the data storage and management procedures of the business as a whole. I based the likelihood scores on how open the access permissions were across the system and weighed severity against how much each incident would disrupt day to day operations.

## My remediation strategy

- Implement authentication authorization and auditing mechanisms so only authorized users can access the database server
- Use strong passwords role based access controls and multi factor authentication to limit user privileges
- Encrypt data in motion using TLS instead of SSL since TLS is the more secure option
- Set up IP allow listing to corporate offices so random users from the internet cant connect to the database

## What I took away from this

The hacker threat scoring a 9 out of a possible 9 tells me this needs the most urgent attention out of everything in this report. Between the open access permissions and the fact that SSL was still being used instead of TLS there were clear gaps that could let sensitive customer and campaign data walk right out the door if nothing changes.

— Completed as part of the Google Cybersecurity Certificate program.