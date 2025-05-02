You would want to have your router ship ip address through DHCP service and having a Router do that will help the network instead of a server. 


# ==***ROUTER DHCP***==
1) Go into R1 to exclude low and high ip address the ones you don't want to be used. ***"ip dhcp excluded-address"*** so now you put the router address and then till the limit you want to exclude. For example ==***192.168.1.1 (Router IP address) .. 192.168.1.99***== this says that address between range of .1 to .99 cannot be used for dhcp. Now you exclude the upper addresses, for example ==***192.168.1.151 ..192.168.1.254 (minus the broadcast 192.168.1.255)==
2) Now you need to create a pool and fill in some information the needed information are pool name, default router, dns server and network address. ***"ip dhcp pool {poolname}"*** then ***"default-router{ip address}"*** then ***"dns-server"*** then ***"network {ip address and subnet address}


| **1)** | **ip dhcp excluded-address low ip high ip**                                                                                  |
| ------ | ---------------------------------------------------------------------------------------------------------------------------- |
|        | **ip dhcp excluded- address low ip high ip**                                                                                 |
| **2)** | **ip dhcp pool {poolname} >> default-router{ip address}>>dns-server{ip address} >> network {ip address and subnet address}** |

# ==***IP ROUTING 

For example, If you have ==network 1== with ***IP address of 192.168.1.0***, and another ==network 2== with ***IP address of 192.168.2.0*** and another ==network 3== with ***IP address of 192.168.3.0 /30 (POINT TO POINT) connected with serial 0/0/0.

***HOW DO YOU CONNECT ==NETWORK 1 & NETWORK 2== THROUGH NETWORK 3's SERIAL***

#############################################################
	```
```
1) R1(config)#***ip route 192.168.2.0 255.255.255.0 s0/0/0***. This tells the router in network 1 to connect to network 2's network 2.0.
2) R2(config)#***ip route 192.168.1.0 255.255.255.0 s0/0/0***. This tells the router in network 2 to connect to network 1's network 1.0.

```
**YOU MUST TELL THE INTERFACE AFTER THE COMMAND TO TELL WHICH INTERFACE TO GO TO


# ==***HOW TO SET UP LAST RESORT GATEWAY***==

**The reason we would set a last resort gateway instead of statically setting up a router with a network IP because this can all traffic HAS a path and is not dropped. 

```
R1(config)#: ip route 0.0.0.0 0.0.0.0 {interace (serial)0/0/0}
```

