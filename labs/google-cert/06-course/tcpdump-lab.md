## Capturing And Viewing Network Traffic With Tcpdump

**Course:** Google Cybersecurity Certificate - Course 6 Sound the Alarm Detection and Response


This lab was about using tcpdump inside a linux environment to capture and filter network traffic. Started off logged in as the analyst user on a linux terminal and worked through identifying interfaces capturing live traffic and then reading back a saved capture file

### Identifying Network Interfaces

Ran sudo ifconfig first to see what interfaces were available on the machine. The output showed eth0 as the ethernet interface along with lo for loopback. Since eth0 had the actual network details like inet address and mac address that was the one I used for the rest of the lab. Also tried sudo tcpdump -D as another way to list available interfaces which is useful on systems that dont have ifconfig installed

### Inspecting Live Traffic

Ran sudo tcpdump -i eth0 -v -c5 to capture 5 packets straight off the eth0 interface with verbose output. The -i flag tells tcpdump which interface to listen on and -v gives more detailed info about each packet like tos ttl offset flags and protocol type. When I looked at the output I could see the timestamp first then the ip addresses and ports involved then the tcp flags and sequence numbers. Noticed the P flag which means push meaning the packet was pushing data out and the period next to it representing the ack flag

### Capturing Traffic To A File

After that I moved on to actually saving captured data instead of just streaming it. Used sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap & to capture 9 packets of port 80 traffic in the background and write it to a file called capture.pcap. The -nn flag disables ip and port name resolution which is important from a security standpoint because looking up names could tip off an attacker that theyre being investigated. Then ran curl opensource.google.com to actually generate some http traffic for tcpdump to catch. Verified the file was created using ls -l capture.pcap and saw the done message confirming the capture finished

### Filtering The Captured File

Once the file was saved I used sudo tcpdump -nn -r capture.pcap -v to read back the packet header data with verbose detail. This showed source and destination ip addresses along with ports like 172.17.0.2:46498 talking to 146.75.38.132:80. Then ran sudo tcpdump -nn -r capture.pcap -X to view the same capture but in hexadecimal and ascii format which is something analysts use during malware or forensic analysis to spot patterns or anomalies in the raw data

That was when it really clicked for me how tcpdump gives you full control over live traffic versus just reading saved captures and how the -nn flag matters way more than I first thought from a security perspective

### Key Takeaways

- ifconfig or tcpdump -D can both be used to identify available network interfaces
- -i sets the interface -v gives verbose detail and -c limits how many packets get captured
- -nn should always be used when investigating since it avoids dns and port lookups that could alert an attacker
- -w saves a capture to a file and -r reads it back later for filtering and analysis
- -X shows hex and ascii output which helps with spotting anomalies during forensic work

— Completed as part of the Google Cybersecurity Certificate program.