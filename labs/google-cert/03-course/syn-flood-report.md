# Network Attack Incident Report — Google Cybersecurity Certificate

## Course
Google Cybersecurity Certificate — Course 3 Detect and Respond to Cybersecurity Incidents

## Scenario
So I worked through a scenario where I am a security analyst for a travel agency and the company website went down one afternoon I got an automated alert about a problem with the web server So now when I tried to visit the site myself I got a connection timeout error then From there I had to figure out what was going on using a Wireshark log of the traffic going to and from the server.

## What I found
After analyzing the log I noticed a large number of TCP SYN requests coming from one single IP address 203.0.113.0. At first this IP completed a normal handshake with the server but then it just kept sending more SYN requests over and over without ever finishing the connection which was strange so I concluded this as a red flag because things started to seems bad and the server was reserving resources for each of these half open connections and it was not able to keep up.

While this was happening I could still see legitimate employee traffic going through for a little while coming from IP addresses in the 198.51.100.0 range Employees were still able to load the sales page early on But as the attacker kept flooding the server with more and more SYN packets the legitimate traffic started failing and their request was dropped  I started seeing RST ACK packets sent back to employees and eventually a 504 Gateway Time-out error showed up in the log. After this when I came to the part where the server stopped responding to legitimate traffic completely that was when I knew this was a serious denial of service condition.

Since all the malicious traffic came from a single IP address 203.0.113.0 I identified this as a direct DoS SYN flood attack and not a DDoS since a DDoS would come from multiple sources in different locations

## Impact on the organization
This attack took the company website offline which meant employees could not access the sales page to look up vacation packages for customers It also meant customers could not browse the site at all during the outage For a travel agency that relies on its website to advertise sales and promotions this is a direct hit to business operations and could lead to lost sales and damaged trust with customers if it happens again or for longer

## Immediate actions taken
- Took the web server offline temporarily so it could recover and return to normal operation
- Configured the firewall to block the attacking IP address 203.0.113.0
- Flagged that this block is only a short term fix since the attacker could spoof a different IP to get around it

## Recommendations going forward
- Implement rate limiting on incoming SYN requests so one source cannot overwhelm the server
- Look into SYN cookies or similar mitigation so the server does not commit resources until the handshake is verified
- Set up alerting policy so abnormal SYN traffic gets flagged faster next time
- Continue monitoring the 203.0.113.0 IP range in case the attacker tries again from a nearby address

This needs the most urgent attention since the same type of attack could happen again at any time if the underlying mitigation is not put in place.

— Completed as part of the Google Cybersecurity Certificate program.