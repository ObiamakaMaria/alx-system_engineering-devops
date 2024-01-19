Incident Summary:
 
On 18th of December, 2023 at 3:45 pm GMT,  an incident occurred where SSH access to my server was lost after enabling the Uncomplicated Firewall (UFW) 
without allowing SSH traffic explicitly. This resulted in a permanent loss of connectivity to the  server  until at 4:50 pm when it was later resolved .
This issue resulted to a lack of access to my server as I couldn't ssh into my server anymore because the ufw prevented traffic from my server as it was not enabled. This was a personal server so no other individual or group was affected.
The rootcause was that I didn’t allow  SSH traffic  on ufw  before enabling it

Timeline of Events:

The issue was detected  at 3:45 pm when I tried SSHing into my server after I enabled ufw. Attempted SSH access failed due to the lack of an explicit rule
allowing SSH traffic.
At 3:50 pm , after the loss of connectivity I initiated investigation.
At 4:00 pm,   I  Identified the recognized that the ufw misconfiguration was the root cause.
As part of seeking for solution, I started typing the challenge I had on google went through some resources but couldn’t get the help I needed as they was not a solution to recovering my server. 
Intially.  when I couldn’t  SSH into my server I wasn’t  really aware of what happened but , it was from reading some articles and  resources  that I discovered
 what actually caused the issue.
I reached out to my peer and friend from the same cohort and she said I could request for a new server.I proceeded to the intranet page to request for a 
newserver and the new server was active with juts few seconds of my request.


Corrective Measures:

•	Immediate Resolution
•	Established an alternative means of access to the server, such as console access or out-of-band management, to regain control.
•	Temporarily disabled UFW to restore SSH connectivity.
•	UFW Rule Correction:
•	Added an explicit rule to allow SSH traffic before re-enabling UFW:
•	Updated documentation to emphasize the importance of allowing SSH traffic when enabling UFW.


Preventive Measures:

•	Automation of Firewall Configuration
•	Implemented automated scripts or configuration management tools to             ensure that SSH rules are automatically configured when enabling the firewall.
•	Rule Ordering Verification:
•	Established a practice of verifying the order of firewall rules to ensure that the SSH allow rule precedes any deny rules.
•	Double-Check Configuration Changes:
•	Implemented a peer review process for critical configuration changes, particularly those related to firewall settings.
•	Introduced a checklist to verify that SSH access rules are explicitly configured before enabling UFW.
        


