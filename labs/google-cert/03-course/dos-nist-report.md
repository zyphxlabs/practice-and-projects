# DoS Attack Incident Report Analysis — Google Cybersecurity Certificate

## Course
Google Cybersecurity Certificate — Course 3 Detect and Respond to Cybersecurity Incidents

## Summary
I worked through a scenario where I am a cybersecurity analyst for a multimedia company that offers web design graphic design and social media marketing services to small businesses. The organization experienced a DoS attack that compromised the internal network for two hours until it got resolved During the attack network services suddenly stopped responding because of an incoming flood of ICMP packets and normal internal traffic could not reach any network resources The incident management team responded by blocking the incoming ICMP packets taking non critical services offline and restoring the critical ones.

## Identify
After analyzing the situation I found that a malicious actor sent a flood of ICMP pings into the company network through a firewall that was not properly configured. That was when I realized this unconfigured firewall is what allowed the attacker to overwhelm the network in the first place. This is a denial of service attack and it affected the internal network services across the organization meaning normal employees lost access to the resources they needed to do their jobs for those two hours.

## Protect
After this when I came to the part where I looked at what was actually in place to prevent this that was when things started to seems bad because the firewall had no real configuration stopping this kind of traffic. The network security team has since implemented a few changes to protect against this happening again

- A new firewall rule to limit the rate of incoming ICMP packets
- Source IP address verification on the firewall to check for spoofed IP addresses on incoming ICMP packets
- An IDS/IPS system to filter out ICMP traffic based on suspicious characteristics

These changes need to be reviewed and updated regularly since attackers are always adjusting how they try to get around firewall rules.

## Detect
To detect similar attacks going forward I am recommending the team use network monitoring software to watch for abnormal traffic patterns especially sudden floods of ICMP packets coming from untrusted IP addresses. Combined with the IDS/IPS system this gives the team a way to catch the traffic early before it overwhelms the network again instead of finding out after services already went down.

## Respond
For the response side the incident management team already contained the issue by blocking the incoming ICMP packets and taking non critical services offline while restoring the critical ones first. Going forward the response plan should include immediately isolating the affected firewall or segment generating alerts to the security team the moment abnormal ICMP traffic is detected and documenting every step taken during the incident so it can be reviewed afterward. The team should also communicate with IT staff and any affected internal users as soon as the incident is contained.

## Recover
Since this incident did not involve data loss or corruption the recovery side mainly involved restoring normal network services once the malicious traffic was blocked. For future incidents like this the recovery plan should confirm all critical services are back online and functioning normally check that no other systems were affected during the two hour window and review logs afterward to confirm the firewall rules and IDS/IPS changes are actually working as intended.

## Reflections
On top of that the firewall not having any rules in place at all to begin with is a huge problem I observed since it left the entire network exposed to something as basic as an ICMP flood. This needs the most urgent attention going forward since a similar misconfiguration anywhere else on the network could lead to the exact same kind of outage.

— Completed as part of the Google Cybersecurity Certificate program.