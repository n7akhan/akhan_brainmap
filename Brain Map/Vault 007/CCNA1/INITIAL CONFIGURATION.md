Initial configurations varies from device to device.
The first configuration is for a router!

# *==**ROUTER**==* 

1) Change to **enable** to **privilege mode**. Press "en" and then ***"configure terminal (conf t)"
2) Change **Hostname** by typing "***hostname***" and setting up host name usually R#
3) Change security settings and set up passwords. Type ***enable secret (you password)*** to set up password
4) Encrypt the password now. Type ***"service password-encryption"***
5) For physical connection set up console line. Type ***line console 0***, then set up password by typing ***"password (your password)"*** then type ***"login"*** to save the login, then type ***"logging synchronous"***.
6) Set up interfaces for the router. Type in ***"int gig 0/0"*** then proceed to set up the IP address by typing ***"ip address"*** and then the sub-netmask. Then type in ***"no shutdown"*** so that the interface stays up online. For example 192.168.1.1 255.255.255.0
7) Good idea is to copy the running config and save it by typing in ***"copy start run config"***

# ==***SWITCH***===

1) Change to **enable** to **privilege mode**. Press "en" and then ***"configure terminal (conf t)"
2) Change **Hostname** by typing "***hostname***" and setting up host name usually S#
3) Change security settings and set up passwords. Type ***enable secret (you password)*** to set up password
4) Encrypt the password now. Type ***"service password-encryption"***
5) For physical connection set up console line. Type ***line console 0***, then set up password by typing ***"password (your password)"*** then type ***"login"*** to save the login, then type ***"logging synchronous"***.
6) Set up VLAN for the Switch. Type in ***int vlan 1 "*** then proceed to set up the IP address by typing ***"ip address"*** and then the sub-netmask. Then type in ***"no shutdown"*** so that the interface vlan stays up online. For example 192.168.1.1 255.255.255.0
7) Good idea is to copy the running config and save it by typing in ***"copy start run config"***



| **1)** | **en>>conft**                                                       |
| ------ | ------------------------------------------------------------------- |
| **2)** | **hostname S# or R#**                                               |
| **3)** | **enable secret ccna**                                              |
| **4)** | **service password-encryption**                                     |
| **5)** | **line console 0 >> password ccna >> login >> logging synchronous** |
| **6)** | **set up interface gig or VLAN >> ip >> subnet >> no shutdown**     |
| **7)** | **copy running-config startup-config**                              |

