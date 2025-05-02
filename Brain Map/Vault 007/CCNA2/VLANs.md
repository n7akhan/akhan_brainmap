VLANs are not a simple process but a necessary one to ease the management of your network

- VLANs are completely separate from physical networks. 
- VLANs allow you to **segment networks**
	- <span style="color:rgb(0, 176, 240)">without regard for physical locations</span>
	- <span style="color:rgb(0, 176, 240)">each VLANs are separate logical networks</span>
- VLANs improve network performance by separating large broadcast domain into smaller ones
	- <span style="color:rgb(0, 176, 240)">if a packet is sent from a device on a VLAN all devices in the VLAN receive that frame but devices in others DO NOT </span>
	- <span style="color:rgb(0, 176, 240)">So this helps with performance and you don't hear other traffic.</span> 
# WHY VLANS
+ **SMALLER BROADCAST DOMAINS**
	+ <span style="color:rgb(0, 176, 240)">Reduces the number of devices in a broadcast domain</span>
	
+ **IMPROVED SECURITY
	+ <span style="color:rgb(0, 176, 240)">ONLY users in the same VLAN can communicate together.</span>
	+ <span style="color:rgb(0, 176, 240)">ONLY users in the same VLAN can communicate without the services of a router</span>
	
+ **IMPROVED IT EFFICIENCY
	+ <span style="color:rgb(0, 176, 240)">The smaller the networks the more efficient it cant be. </span>
	+ <span style="color:rgb(0, 176, 240)">Can name VLANs different name to make it better to understand.</span>

+ **REDUCE COST
	+ <span style="color:rgb(0, 176, 240)">Reduce the cost of network upgrades </span>

+ **BETTER PERFORMANCE
	+ <span style="color:rgb(0, 176, 240)">Smaller broadcast reduces unnecessary network traffic</span>
	
+ **SIMPLER PROJECT AND APPLICATION MANAGEMENT**

# VLAN TYPES
+ **DEFAULT**
	+ <span style="color:rgb(0, 176, 240)">Cannot be renamed or deleted. </span>
	+ <span style="color:rgb(0, 176, 240)">All ports are assigned to VLAN1 by default</span>
	+ <span style="color:rgb(0, 176, 240)">Native VLAN1 </span>
```
Switch# show vlan brief //shows you all the vlans and the ports
```
+ **DATA VLAN
+ **NATIVE VLAN**
	+ <span style="color:rgb(0, 176, 240)">User traffic VLAN gets tagged by</span> **VLAN ID** <span style="color:rgb(0, 176, 240)">when it is sent to another switch through</span> **TRUNK PORTS & ACCESS PORTS**
+ **MGMT VLAN**
+ **VOICE VLAN**
	+ <span style="color:rgb(0, 176, 240)">Uses VLAN 150</span> 
