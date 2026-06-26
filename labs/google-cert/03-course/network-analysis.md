# Network Traffic Analysis
**Google Cybersecurity Certificate — Course 3: Connect and Protect: Networks and Network Security**



## What This Was About

So in this activity  the given scenario was about a company that provides IT services for clients and several customers reported  their clients and customers complaint that they could not access the website www.yummyrecipesforme.com and  they were seeing the error "destination port unreachable" after waiting for the page to load 

Soo my job was to analyze the network traffic using tcpdump and  figure out which protocol was affected and then write up a report on what I found



## What I Did To Investigate

When I came to investigate I first tried visiting the website myself to expereince it myself  and got the same error that confirmed it was not just one user having a bad connection after that I loaded tcpdump and tried loading the page again while capturing the traffic so I could actually see what was happening at the packet level

After analyzing the log I could see the browser was sending UDP packets to the DNS server at 203.0.113.2 on port 53 trying to resolve www.yummyrecipesforme.com and instead of getting a DNS response back what came back were ICMP packets with the error message "udp port 53 unreachable" and that happened not once but three separate times across the log



## What The Log Showed

The first thing I observed was the timestamp 13:24:32.192571 which tells me the incident was happening at 1:24 p.m. The source IP sending the queries was 192.51.100.15 which is my machine and the destination was the DNS server at 203.0.113.2 The query had a flag A? which means it was requesting an A record( which is useed to resolve IPV4 adresses) to map the domain name to an IP address

After this when I came to the response lines that was when things started to seem bad The ICMP error "udp port 53 unreachable" was coming back every single time which means no service was listening on port 53 of that DNS server The DNS queries had nowhere to go so the browser never got an IP address and the website never loaded



## What Was Actually Wrong

- Port 53 unreachable on the DNS server  this is the port DNS runs on so without it the whole name resolution process breaks so it was major issue 
- UDP packets sent three times this was the second clear issue and the   all three  that was being sent came back with the same ICMP error  that  came back all three times
- No DNS response was ever received meaning the browser could never get the IP for the domain
- The website never loaded because HTTPS request could not even be formed without the IP address first



## Likely Cause and Next Steps

The most likely cause is that the DNS service stopped running on that server or most probably the  firewall rule is blocking UDP traffic to port 53 Either way the result is the same the DNS server is completely unreachable

This needs the most urgent attention because without DNS resolving the domain name nobody can reach the website at all Next steps would be checking the firewall configuration for any rules blocking port 53 and contacting the DNS server administrator to verify whether the service is still running and to check for any signs of an attack that may have taken it down



*Completed as part of the Google Cybersecurity Certificate program.*