## Incident Handler's Journal Full Log

**Course:** Google Cybersecurity Certificate - Course 6 Sound the Alarm Detection and Response


This is my full incident handlers journal covering four entries logged throughout the course along with my reflections at the end. Each entry documents an activity or tool I worked with as I went through detection and response concepts

### Entry 1 Documenting A Ransomware Incident


This incident happened in two phases detection and analysis then containment eradication and recovery. For the detection and analysis part the organization contacted several outside organizations for technical assistance once the ransomware was discovered. For containment the company shut down their computer systems but since they couldnt handle eradication and recovery alone they had to bring in outside help as well

Who an organized group of unethical hackers
What a ransomware security incident
Where at a health care company
When Tuesday 9 00 am
Why the incident happened because unethical hackers were able to access the companys systems using a phishing attack after gaining access the attackers launched their ransomware on the companys systems encrypting critical files the attackers motivation appears to be financial because the ransom note they left demanded a large sum of money in exchange for the decryption key

- How could the health care company prevent an incident like this from occurring again
- Should the company pay the ransom to retrieve the decryption key

### Entry 2 Analyzing A Packet Capture File


For this one I used wireshark to analyze a packet capture file. Wireshark is a network protocol analyzer with a graphical interface and its valuable because it lets security analysts capture and analyze network traffic which helps with detecting and investigating malicious activity

I had never used wireshark before this so I was pretty excited going into it. At first glance the interface felt overwhelming honestly but I could immediately see why its such a powerful tool once you understand whats going on inside all that traffic

### Entry 3 Capturing My First Packet


For this entry I used tcpdump to capture and analyze network traffic. Tcpdump is a network protocol analyzer thats accessed through the command line and just like wireshark its valuable because it lets you capture filter and analyze network traffic

I was still pretty new to the command line at this point so using it to capture and filter traffic was a real challenge. I got stuck a couple times because I used the wrong commands but after slowing down and carefully following the instructions and redoing a few steps I finally got through it and captured the traffic successfully

### Entry 4 Investigating A Suspicious File Hash


For this activity I used VirusTotal which analyzes files and urls for malicious content like viruses worms and trojans. Its a really useful tool when you want to quickly check if something like a file or website has already been reported as malicious by the community. I used it here to analyze a file hash that ended up being reported as malicious

This incident occurred in the detection and analysis phase. The scenario put me in the role of a security analyst at a SOC investigating a suspicious file hash after it was flagged by the security systems and I had to dig deeper to figure out if it was a real threat

Who an unknown malicious actor
What an email sent to an employee contained a malicious file attachment with the sha 256 file hash of 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b
Where an employees computer at a financial services company
When at 1 20 pm an alert was sent to the organizations SOC after the intrusion detection system detected the file
Why an employee was able to download and execute a malicious file attachment via email

- How can this incident be prevented in the future
- Should we consider improving security awareness training so employees are more careful with what they click on

### Reflections

Looking back the tcpdump activity was the one that challenged me the most. Im still new to the command line so learning the syntax for a tool like that was a big learning curve for me. I felt frustrated at first because I wasnt getting the right output but after redoing the activity I figured out where I went wrong and that taught me to slow down and read instructions carefully instead of rushing through

My understanding of incident detection and response has changed a lot since starting this course. At the beginning I had a basic idea of what detection and response meant but I didnt really grasp how complex it actually is. As I went through the course I learned about the incident lifecycle the importance of having solid plans processes and people in place and the different tools used along the way

If I had to pick the tool or concept I enjoyed the most it would be network traffic analysis. It was my first time working with protocol analyzer tools so it was both challenging and exciting at the same time. Being able to capture and analyze network traffic in real time was genuinely fascinating to me and its made me want to keep building my skills with these kinds of tools going forward

— Completed as part of the Google Cybersecurity Certificate program.