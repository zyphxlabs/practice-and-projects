# Google Cybersecurity Certificate — Course 4: Tools of the Trade Linux and SQL

## Lab: Use APT to install and uninstall software

I worked through this lab using the analyst account already logged into the Bash shell and my job was to install and manage the Suricata and tcpdump network security applications using APT

First I confirmed APT was installed by just running apt in the shell and it printed the version 1.8.2.3 and usage info which told me it was already there by default since this is a Debian based system

After that I moved into installing Suricata using sudo apt install suricata and pressed enter to accept the default yes when prompted for dependencies then I verified it installed by running suricata directly and it showed version 4.1.2 with the usage options which confirmed it worked

Then I uninstalled Suricata using sudo apt remove suricata and when I ran suricata again afterward it gave me a bash error saying no such file or directory which confirmed the removal worked

Next I installed tcpdump using sudo apt install tcpdump and after that I ran apt list --installed to confirm both applications were showing correctly in the list

- tcpdump showed up as 4.9.3-1~deb10u2 amd64 installed
- suricata did not show up since I had already removed it at that point

After this when I came to the part where I had to reinstall suricata that was when things started to make more sense because I could actually see the before and after state of the package list

I reinstalled suricata with sudo apt install suricata again and ran apt list --installed one more time and this time both applications were confirmed installed

- suricata showed as 1:4.1.2-2+deb10u1 amd64 installed
- tcpdump showed as 4.9.3-1~deb10u2 amd64 installed

This lab gave me practical experience with installing uninstalling and listing applications using the APT package manager which is something I will use regularly as a security analyst working in Linux environments

— Completed as part of the Google Cybersecurity Certificate program.