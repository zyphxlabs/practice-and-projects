## Suricata IDS Rule Creation And Log Analysis

**Course:** Google Cybersecurity Certificate - Course 6 Sound the Alarm Detection and Response

This lab was about exploring how suricata rules work and running one against sample traffic to see how alerts get generated and logged. Started off in the home analyst directory where a custom.rules file and a sample.pcap file were already sitting there waiting to be used

### Breaking Down The Custom Rule

Ran cat custom.rules to see what the rule actually looked like and it came back as alert http $HOME_NET any -> $EXTERNAL_NET any with msg GET on wire flow established to server content GET http_method sid 12345 rev 3. Once I broke it down I realized a signature is really just three parts an action a header and rule options. The action here was alert which just means suricata inspects the traffic and sends out a notification if it matches nothing gets dropped or blocked with an alert action alone

The header part was http $HOME_NET any -> $EXTERNAL_NET any and that defines the protocol and the direction of traffic being watched. In this lab $HOME_NET was defined as the 172.21.224.0/20 subnet and the arrow shows traffic going from that home network out to the external network. The word any just means it catches traffic on any port

Then came the rule options part which had msg flow content http_method sid and rev packed in with semicolons. The msg option is just the text that prints when the alert fires which was GET on wire in this case. The flow option made sure it only matched packets going from client to server and content GET told suricata to specifically look for the word GET in the http method field. sid 12345 is the unique id for this exact rule and rev 3 tells you its the third revision of that signature

### Triggering The Rule And Checking Fast Log

Before running anything I checked ls -l /var/log/suricata and confirmed the folder was empty which made sense since suricata hadnt run yet. Then ran sudo suricata -r sample.pcap -S custom.rules -k none to process the sample pcap file against the custom rule. The -r flag points to the input pcap -S tells it which rules file to use and -k none disables checksum checks since it wasnt needed for a sample capture file

After that when I listed the suricata log folder again there were now four files sitting there including fast.log and eve.json. Ran cat /var/log/suricata/fast.log and got two alert lines back both showing GET on wire with timestamps 11/23/2022-12:38:34.624866 and 11/23/2022-12:38:58.958203 along with the source and destination ip and port info like 172.21.224.2:49652 going to 142.250.1.139:80

### Digging Into Eve Json

That was when I moved on to the eve.json file which is way more detailed than fast.log since it stores everything in json format. Running cat on it directly was pretty messy to read so I used jq . /var/log/suricata/eve.json | less instead which formatted it way better. Checked the severity property for the first alert and it came back as 3

Ran jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json to pull just the fields I actually cared about instead of scrolling through everything. The destination ip for the last event in the file was 142.250.1.102 and the alert signature for the first entry was GET on WIRE. I also learned about the flow_id field here which groups packets that belong to the same network flow together so you can pull every log tied to one specific flow using jq select flow_id

### Key Takeaways

- a suricata signature is made up of an action a header and rule options separated by semicolons
- alert just notifies while drop reject and pass actually affect whether traffic goes through
- fast.log gives you a quick readable alert summary but eve.json has the full detailed json data
- jq is really useful for pulling specific fields out of eve.json instead of reading raw output
- flow_id lets you correlate all the logs that belong to the same network flow

— Completed as part of the Google Cybersecurity Certificate program.