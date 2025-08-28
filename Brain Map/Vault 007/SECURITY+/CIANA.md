
# **Confidentiality

**Refers to the protection of information from unauthorized individual entity or process.**

+ Keep information safe from prying eyes and provide for people who are authorized.
+ Keeps business proprietary stuff hidden
+ Keep data safe within regulations! 

**HOW TO ACHIEVE CONFIDENTIALITY**
1) Encryption
	- Process of converting data into code to prevent unauthorized access. Scrambles it into ciphertext 
2) Physical Security
	- Used to ensure confidentiality for physical types of data and for digital information contained on servers and workstations. Filing cabinets, finger scanners and such
3) Access Controls
	- Ensures only authorized personnel can access certain types of data. Adding credentials to files and permissions
4) Data Masking 
	 - Method that involves obscuring data within a database to make it inaccessible for authorized users while retaining the real data's authenticity and use for authorized users. When a credit card number is stored you can mask the first 12 digits out of the 16.
5) Training and Awareness
	- Conduct regular training on the security awareness best practices that employees can use to protect the organizations sensitive data. 


**PROTECTING DATA FROM BEING SEEN BY STRANGERS! THINK ==ENCRYPTION==!!!**

==========================================================
# **Integrity

Helps to ensure that information remains accurate and unchanged in its state unless intentionally modified by authorized users

Verifies the accuracy and the trustworthiness of the data over the entire life cycle.

**WHY IS  INTEGRITY IMPORTANT**
1) Ensure Data Accuracy
	- Most important! Good accurate data yields accurate and good results such as medical data or financial 
2) Maintain Trust
	- Maintain trust with users and systems and networks. If a bank account is compromised you wont trust it anymore. Customer retention 
3) Ensure System Operability
	- A compromised system with a breach of integrity can give us downtime and loss of business. 


**FIVES METHODS FOR HOW TO ACHIEVE INTEGRITY** 

1) Hashing
	- Process of converting data into a fixed sized value. If any changes occur out hash number will change dramatically. 
	- Hash Digest occurs when hash is occurred due to tampering, this leaves a digital fingerprint.
2) Access Controls
	- Ensure that only authorized individuals can modify data and reduce the risk of unintentional or malicious alterations. By setting up permissions and credentials. 
3) Digital Signatures
	 - User encryption to ensure integrity and authenticity.  
4) Checksums 
	- Method to verify the integrity of data during transmission. Comparing senders checksum with the received checksum to see if they are the same or not. 
5) Regular Audits
	- Involve reviewing's logs and operations to ensure that only authorized changes have been made and any discrepancies are addressed. 

**MAKES SURE THAT DATA REMAINS THE SAME ACCURATE THROUGH OUT ITS LIFECYCLE.** 
**INTEGRITY THINK ==HASING==!** 

==========================================================

# **Availability 

Used to ensure that information, systems and resources are accessible and operational when needed by authorized user. 

Making sure that services are always available! 


**ACHIEVING UPTIME**
99.9 = 3 nines = in the year we will be down for a maximum of 8.76 hours
99.999 = 5 nines = we will be down for only 5.26 minutes the whole year.

**WHAT AVAILABILTY ACHIEVES**
1) Ensure business continuity 
	- Ensures that business continues
2) Maintaining costumer trust
	- If we loose costumer through downtime you may loose trust and loose a costumer
3) Upholding reputation
	 - Down time hurts reputation of a company!

**HOW TO HAVE GOOD AVAILABILTY**
1) Redundancy 
	- Duplication of critical components or functions of a system with the intention of enhancing its reliability.
	- If something goes down you have a backup 

		==**TYPES OF REDUNDANCY**==
			1) Server redundancy = having multiple servers if one goes down or overloads
			2) Data Redundancy = storing in multiple places
			3) Network Redundancy = switch to different modes of network if one network goes down. 
			4) Power Redundancy = Having backup power!

**AVAILABILTY IS HAVING THINGS RUNNING ALWAYS! THINK ==REDUNDANCY==!** 

==========================================================

# **NON-REPUDIATION**

Focusing on providing undeniable proof in digital transactions

Think about getting something or data with a seal on it that you KNOW is from someone who has that specific seal! 

We use digital ==signature!== 

===============================================================
# **AUTHENTICATION 

Conducting identity verification

**5 COMMON AUTHENTICATION WAYS**

1) Something you know
	+ Relies on info that a use can recall
	+ Username or password
2) Something you have
	+ Physical items to authenticate
	+ employee ID
	+ OTPassword
3) Something you are
	+ Relies on the user providing a unique physical or behavioral characteristic of the person to validate that they are who they are.  
	+ Biometric authentication, facial scan
4) Something you do
	+ Relies on user to do a unique action to verify the user
5) Somewhere you are
	+  Relies on the user being in a certain geographic location before access is  granted.   
	+ Location based factor to allow privileges
	
	IF you have 2 of these factors then you have **TWO FACTOR AUTHENTICATION 2FA**
	IF you have 2 or more of the factors then its **MULTI FACTOR AUTHENTICATON MFA**

A solid authentication system makes it more secure and makes sure that no one can access our data.

# - Authorization

+ Permissions and privileges granted to users or entities after they have been authenticated. 
	+ you are authenticated to enter and building but then authorized to enter a room within that building.  
	1) **Protect sensitive data: It is only available for people with authorized credentials.
	2) **Maintain system integrity in organizations: No data alterations only authorized people can. 
	3) **Create more streamlines and user friendly experience: so its easier for user only 
	
	WHEN YOU THINK OF AUTHRIZATION THINK OF SET OF RULES AND POLOCIES THAT ARE USED TO DICTATE WHAT ACTIONS USERS CAN PERFORMS ONCE VERIFIED 

# -Accounting

+ Security measure that ensures all users activities are properly tracked and recorded  
	+ Keeps tracks on any logs from a user. 
	+ Seeing who is logging, use it to audit
	+ **AUDIT TRAIL: Chronological record of all user activities that can be used to trace changes, unauthorized access or anomalies. 
	+ **Regulatory Compliance: Maintains a record of all user activities. 
	+ **Forensic Analysis: uses details accounting and events logs that can help to how and why it happened. 
	+ **Resource Optimizations: See who is using what to make better resources decisions.
	+ **User Accountability: Keeps users in check
==========================================================

