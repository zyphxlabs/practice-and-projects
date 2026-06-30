# Brute Force Attack Incident Report — Google Cybersecurity Certificate

## Course
Google Cybersecurity Certificate — Course 3 Detect and Respond to Cybersecurity Incidents

## Scenario
In todays work I completed  a scenario where I completed duties of  a cybersecurity analyst for yummyrecipesforme.com a website that sells recipes and cookbooks a former employee turned hacker used a brute force attack to get into the web host by repeatedly entering known default passwords for the admin account until they guessed the right one. Once they got in they changed the source code of the website and embedded a javascript function that prompted visitors to download and run a file After doing this the hacker also changed the admin password so the website owner got locked out.

## What I found
To investigate I set up a sandbox environment and ran tcpdump while loading yummyrecipesforme.com myself so I could observe the traffic. The first thing I saw in the log was a DNS request from my machine on port 52444 going out to dns.google.domain asking for the A record of yummyrecipesforme.com. The DNS server replied back with the IP address 203.0.113.22.

After this when I came to the part where the browser connects directly to the website that was when things started to make sense. My machine on port 36086 sent a SYN flag to yummyrecipesforme.com.http and the server responded with a SYN ACK confirming the connection. Then I saw the GET request HTTP GET / HTTP/1.1 being sent which lines up with the website loading and prompting the download of the executable file. This is the point where the malware gets delivered to the visitor.

About two minutes later in the timestamps I noticed a second DNS request this time for greatrecipesforme.com which resolved to a completely different IP address 192.0.2.17. Right after that my machine started a new connection on port 56378 directly to greatrecipesforme.com.http with the same SYN handshake process repeating and another GET request being sent. That was when I confirmed the malware redirected the browser away from the real website to the fake one.

The protocol involved at the application layer for both connections was HTTP and the DNS protocol was used both times to resolve the domain names before the HTTP connections were made.

## Impact on the organization
This incident allowed a malicious actor to take over the admin panel of a customer facing website and use it to distribute malware to real customers. Multiple customers contacted the helpdesk saying their computers slowed down after running the downloaded file and that the website address changed on them. The website owner also lost access to their own admin panel because the hacker changed the password after gaining entry. This is a serious problem because customers trusted the site for something as simple as downloading a recipe and instead got their machines compromised.

## Root cause
The web host admin account was still using a default password which is how the hacker was able to brute force their way in so easily. On top of that there were no controls in place to limit login attempts or detect repeated failed logins which is a huge problem I observed.

## Recommendation
- Limit the number of login attempts allowed before locking the account temporarily
- This is effective because it directly stops a brute force attack from being able to keep guessing passwords indefinitely
- It also gives the team a clear signal when an account is being targeted since repeated lockouts would trigger an alert

This needs the most urgent attention since the admin account is still vulnerable to the same type of attack happening again if the default password and lack of login limits are not addressed.

— Completed as part of the Google Cybersecurity Certificate program.