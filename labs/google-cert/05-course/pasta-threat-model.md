# PASTA Threat Modeling Lab - Google Cybersecurity Certificate (Course 5)

## What I did

For this lab I worked through a PASTA threat modeling exercise for a sneaker company shopping application. PASTA has seven stages that walk through business objectives all the way to risk analysis and my job was to fill out each stage for this specific app.

## Defining business and security objectives

I started by listing out the specific business requirements for the app. Users can create member profiles either internally or by connecting external accounts and the app has to process financial transactions. Since payments are involved the app also needs to be compliant with PCI-DSS which shapes a lot of the decisions that come later.

## Defining the technical scope

Next I looked at the technologies the application actually uses which included API PKI SHA-256 and SQL. APIs stood out to me the most here since they facilitate data exchange between customers partners and employees and handle a lot of sensitive data while connecting different systems together. That said I noted that specific details about which APIs are actually being used should be looked at before prioritizing one technology over another since a larger attack surface makes APIs more prone to vulnerabilities.

## Decomposing the application

For this stage I reviewed the sample data flow diagram to understand how the different components of the app communicate with each other. This step is really about seeing how the app works under the hood and how current security controls are implemented across those communication paths.

## Threat analysis

After this when I came to the threat analysis stage that was when things started to look bad. I identified injection as a threat since the app relies on SQL and injection attacks are extremely common against SQL databases. I also flagged session hijacking as a threat since the app passes cookies between multiple layers which opens the door for that kind of attack if not handled carefully.

## Vulnerability analysis

Looking at vulnerabilities that connect to those threats I found a lack of prepared statements which directly ties back to the injection risk since without prepared statements the SQL database is much easier to exploit. I also identified a broken API token as a vulnerability which is a real problem given how much sensitive data flows through the APIs in this app.

## Attack modeling

For this stage I reviewed the sample attack tree diagram which models how user data could be exploited based on the threats and vulnerabilities identified in the earlier stages. This step really shows how a lack of prepared statements and a broken API token arent just theoretical problems but can actually be chained together into a real attack path.

## Risk analysis and impact

To wrap up the assessment I listed out four security controls that could reduce the risk identified throughout the process:

- SHA-256
- Incident response procedures
- Password policy
- Principle of least privilege

## What I took away from this

Going through all seven stages showed me how threat modeling connects each piece together starting from a simple business requirement all the way to a specific vulnerability like a broken API token. This needs the most urgent attention since payment processing combined with a larger API attack surface means even a small gap like missing prepared statements could turn into a serious breach if its not addressed early.

— Completed as part of the Google Cybersecurity Certificate program.