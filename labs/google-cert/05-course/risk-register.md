# Risk Register Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I stepped into the role of a new hire on a cybersecurity team at a commercial bank. The team was building out a risk register to figure out which vulnerabilities needed attention first. I had to look at the banks operating environment then score five risks to the banks funds using likelihood and severity to come up with a priority score.

## The operating environment

The bank sits in a coastal area with low crime rates which sounds safe on paper but there is still a lot going on underneath. There are 100 on premise employees and 20 remote employees handling data every day. The customer base is 2000 individual accounts and 200 commercial accounts and the bank is marketed by a professional sports team along with ten local businesses in the community. On top of that there are strict financial regulations requiring the bank to secure its data and funds including having enough cash on hand each day to meet Federal Reserve requirements.

## What I found for each risk

Business email compromise stood out to me first since with 120 employees spread across on premise and remote work there is a lot of room for someone to get tricked into sharing confidential information. I scored this a 3 for likelihood since phishing and social engineering are so common now and a 2 for severity giving it a priority of 6.

Compromised user database was next and this one worries me because if customer data is poorly encrypted then all 2000 individual accounts and 200 commercial accounts are exposed. I gave this a 2 for likelihood and a 3 for severity landing on a priority of 6 since a breach here could destroy customer trust fast.

Financial records leak was similar in that a database server of backed up data being publicly accessible is not something that happens constantly but when it does the damage is massive. I scored likelihood a 2 and severity a 3 which also brings the priority to 6.

Theft in this case means the banks safe being left unlocked and honestly given the low crime rate in the area I scored likelihood a 1. Severity still needed a 2 since funds walking out the door is a real financial hit so priority came out to 2.

Supply chain disruption from delivery delays due to natural disasters made sense to score low on likelihood since the bank is coastal but this kind of event does not happen every day. I gave likelihood a 1 and severity a 2 for a priority of 2 as well.

## Notes on the environment risk factors

Security events are possible here because the bank handles funds and sensitive data across a large number of employees and customers while also being publicly promoted which increases visibility to attackers. Regulatory pressure to secure funds daily adds another layer where even a small disruption could cause compliance issues.

## Priorities going forward

- Business email compromise and compromised user database and financial records leak all scored a 6 so these need attention first
- Theft and supply chain disruption both scored a 2 so these can be monitored but are lower priority right now
- This needs the most urgent attention since three out of five risks tied for the highest score in this register

— Completed as part of the Google Cybersecurity Certificate program.