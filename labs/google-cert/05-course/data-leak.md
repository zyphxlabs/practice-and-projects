# Data Leak Worksheet Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I worked for an educational technology company that built an app to help teachers automatically grade assignments. My job was to look into a data leak of internal business plans that ended up on social media and figure out what went wrong then recommend how to fix it using NIST SP 800-53 AC-6 as the reference point for least privilege.

## What happened in the incident

A sales manager shared access to a folder of internal only documents with their team during a meeting. The folder had files tied to a new product that had not been publicly announced yet along with customer analytics and promotional materials. After the meeting the manager never revoked access to that folder but did warn the team to wait for approval before sharing the promotional materials with anyone outside the company.

Later during a video call with a business partner one of the sales reps forgot that warning completely. The rep meant to send a link to just the promotional materials so the partner could share them with their own customers but ended up sending a link to the entire internal folder by mistake. The business partner had no idea and posted that link straight to their companys social media page thinking it was just the promotional stuff.

## What I found

After this when I came to the part which they lack that was when things started to seem bad. The manager forgot to revoke access after the meeting which left the door open and then the rep made a simple mistake by grabbing the wrong link. On top of that there was no system in place to catch this before it went out the door which tells me the company was relying on people remembering warnings instead of having actual controls enforced.

I also reviewed NIST SP 800-53 AC-6 as part of this and it addresses least privilege by stating that only the minimal access needed to complete a task should be given to users. It focuses on enforcing this through processes user accounts and roles so nobody is operating with more privilege than what their job actually requires.

## My recommendations

- Restrict access to sensitive resources based on user role so the sales team never has access to internal only files in the first place
- Automatically revoke access to information after a period of time so folders like this dont stay open after a meeting ends

## Why these fixes matter

If access had been restricted by role the sales rep would never have had the internal folder available to share by accident in the first place. And if access expired automatically after the meeting the manager forgetting to revoke it manually wouldnt have mattered since the system would have handled it. This needs the most urgent attention since right now the company is depending on people not making mistakes instead of building controls that account for human error.

— Completed as part of the Google Cybersecurity Certificate program.