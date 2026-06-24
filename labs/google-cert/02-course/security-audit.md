# Conduct a Security Audit

**Google Cybersecurity Certificate — Course 2: Play It Safe: Manage Security Risks**


---

## What This Was About

So the given scenario was about an Botium toy company that operate online and they were growing fast but they had no security plans in place so the company manager decieded to take action to keep them secure so she planned an internal audit so she they can assess what they had and where they lack  and whether their policies rule etc align with regulations or not

My job was to  first analyze their scope goals and risk assessment reports  then go through a controls and compliance checklist and mark what was in place and what wasn't. Risk score was 8 out of 10 which is pretty high

---

## What They Had

First after analyzing I observed that firewall was there antivirus too and it was being monitored regularly. Physical side was fine as well  locks on everything CCTV up and running and fire detection systems in place. Legacy systems were being monitored but with no real schedule. A password policy existed too but it was so weak it barely counted

---

## What Was Missing

After this when I came to the part which they lack that was when things started to seems bad. No encryption at all so customer credit card data was just sitting there unprotected as plain text. No IDS is  in place  so nobody would even know if someone was already inside the network or not . No backups and no disaster recovery plan too  which means one serious incident and the whole business stops

On top of that least privilege and separation of duties were never implemented so every single employee had access to all internal data including cardholder data and customer PII which is a huge problem I observed 

---

## Compliance Gaps

**PCI DSS** — pretty much failed across the board. Unauthorized access to card data encryption not in place password management weak. This needs the most urgent attention

**GDPR** — they had a 72 hour breach notification plan and privacy policies were enforced which was good but customer data was not properly secured or classified so still partially failing

**SOC** — data integrity and availability were fine but user access policies were not established and sensitive data was not being kept confidential

---

## What I Would Fix First

- Least privilege and separation of duties  as currently everyone literally every single person working are  having access to everything is the most immediate risk because even a small mismanagment or bad intentions can shutdown whole business
- Encryption will be the second thing I will work on as  unencrypted credit card data is a direct PCI DSS violation
- IDS  this will be the third task I will do as they are completely blind to anything happening on their network literally no record of whats going on in their network
- Backups and disaster recovery  is the other major issue need to be addressed because  one incident away from total shutdown
- Password management system  is also a major concern as the policy exists but nothing enforcing it anyone can use any password of their will and wish 
- Asset classification  last but not the least will be the thing i do as it is currently hard to manage risk when you don't know what matters most

---

*Completed as part of the Google Cybersecurity Certificate program.*