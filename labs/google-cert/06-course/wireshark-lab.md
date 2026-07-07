## Wireshark Packet Analysis Lab

**Course:** Google Cybersecurity Certificate - Course 6 Sound the Alarm Detection and Response


This lab was about using wireshark to inspect packet data and apply filters to sort through network traffic. Started off by opening the sample pcap file and just getting a feel for how the interface lays things out

### Exploring The Data

After opening the file I noticed the packet list uses colors to help you classify traffic quickly. Light blue was for DNS traffic and green was for a mix of TCP and HTTP. When I scrolled down looking for a packet where the info column starts with Echo (ping) request I found the protocol for that one was ICMP

### Filtering By IP Address

Applied the filter ip.addr == 142.250.1.139 and the list dropped down to just two colors light pink for ICMP and light green for TCP and HTTP. Opened the first TCP packet and drilled into the subtrees starting with Frame then Ethernet II then Internet Protocol Version 4 then Transmission Control Protocol. Found that the TCP destination port for this packet was port 80 which makes sense since it was the initial web request to an HTTP site

### Source And Destination Filters

Then I used ip.src == 142.250.1.139 to only see traffic coming from that address and ip.dst == 142.250.1.139 to only see traffic going to it. After that I filtered by the ethernet MAC address eth.addr == 42:01:ac:15:e0:02 and when I opened the first packet in that filtered list the Internet Protocol Version 4 subtree showed the protocol as TCP

### DNS Packet Analysis

Filtered udp.port == 53 to isolate DNS traffic since DNS runs on port 53. In the first packet under the Domain Name System query subtree the queried website was opensource.google.com. Then I checked the fourth packet and expanded the Answers section which showed the IP address 142.250.1.139 tied to that same domain

### TCP Packet Analysis

Filtered tcp.port == 80 since thats the default web traffic port. Opened the first packet in that list and the destination IP was 169.254.169.254. Went through the Internet Protocol Version 4 subtree and found the Time to Live value was 64 the Header Length was 20 bytes and the Destination Address was 169.254.169.254 as well. Also checked the Frame subtree and the Frame Length came out to 54 bytes

After that I ran tcp contains "curl" to search for packets with specific payload text and it filtered down to packets containing web requests made using the curl command

### Key Takeaways

- coloring rules in wireshark make it way faster to spot different traffic types at a glance
- ip.addr ip.src and ip.dst filters let you narrow down traffic from either direction or both
- DNS traffic can be isolated with udp.port == 53 and you can see both the query and the answer
- tcp contains lets you search for specific text inside the packet payload which is useful for finding things like commands or credentials

— Completed as part of the Google Cybersecurity Certificate program.