**SPANNING TREE PROTOCOL (STP)**
+ Basically, STP makes paths for functioning of the network by creating bridges and pathways. 
+ It prevents loops in Ethernet networks by **blocking redundant links and make sure network stays loop free**
+ Uses BPDU (Bridge Protocol Data Unit Unit) to elect bridges and root ports, designated ports and alternate ports

**STP OPERATIONS**
1) **Elect the root bridge
	- <span style="color:rgb(0, 176, 80)">The switch with the lowest BID priority number, then that will be the ROOT bridge</span>
	- <span style="color:rgb(0, 176, 80)">If all switches had the same priority # then the lowest MAC address is the KING root bridge! </span>
2) **Elect the root part
	+ <span style="color:rgb(0, 176, 80)">Internal root path cost = how much it cost for each switch node to cost to get to the root</span>
	+ <span style="color:rgb(0, 176, 80)">The STA algorithm is used to select the best root PORT. Every non root switch will select the port, its the port closest to root bridge in terms of overall cost.</span>
3) **Elect the designated ports
	+ <span style="color:rgb(0, 176, 80)">All ports on the root bridge are designated ports.</span>
	+ <span style="color:rgb(0, 176, 80)">The root bridge switch will always have designated ports pointing outwards</span>
	+ <span style="color:rgb(0, 176, 80)">Ports going towards root bridge are root ports AND EVERY ROOT PORTS OPPOSITE IS DESIGNATED AND VICE VERSA</span>
4) **elect the alternate (blocked) ports
	+ <span style="color:rgb(0, 176, 80)">If a port is not root or designated port then they are blocked and made into backup port to PREVENT LOOPS</span>
5) .
