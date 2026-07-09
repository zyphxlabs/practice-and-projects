## File Hash Investigation Using VirusTotal

**Course:** Google Cybersecurity Certificate - Course 6 Sound the Alarm Detection and Response


This activity was about investigating a file hash using VirusTotal and identifying different types of indicators of compromise tied to it. Went through the Detection Details Relations and Behavior tabs to pull together a full picture of the file and confirm it was malicious

### Summary Of The File Hash

Looking under the Detection tab the Community Score and the security vendors analysis gave me a clear read on this file right away. Over fifty security vendors flagged this file as malicious which is a huge number and not something to brush off. Multiple vendors also categorized it specifically as Flagpro malware which I learned is a known malware used by advanced threat actors so this wasnt some random low level infection

### Identifying IoCs

After analyzing the Details Relations and Behavior tabs I was able to pull out several different types of indicators of compromise related to this file

- Domain name org.misecure.com is reported as a malicious contacted domain under the Relations tab in the VirusTotal report
- IP address 207.148.109.242 is listed under the Relations tab and this same address is tied back to the org.misecure.com domain in the DNS Resolutions section under the Behavior tab from the Zenbox sandbox report
- Hash value 287d612e29b71c90aa54947313810a25 is the MD5 hash listed under the Details tab in the VirusTotal report
- Network host artifact HTTP requests made to the org.misecure.com domain which shows up in the Network Communications section under the Behavior tab from both the Venus Eye Sandbox and Rising MOVES sandbox reports
- Tool input capture is listed in the Collection section under the Behavior tab from the Zenbox sandbox report and this is used by malicious actors to steal things like passwords and credit card numbers straight from user input
- TTP command and control is listed as a tactic under the Behavior tab from the Zenbox sandbox report which is how attackers keep a communication channel open between the infected system and their own system

That was when it really came together for me how many angles you can pull IoCs from just one file hash. It wasnt just one flag it was domains ip addresses a hash value network behavior tools and tactics all pointing back to the same malicious file

— Completed as part of the Google Cybersecurity Certificate program.