You use SSH and Telnet (way less secure) to get into our switches and routers while being away from the device itself. 

# ==***SSH***==

1) Always start with a hostname. Type ***"hostname R1"***
2) Set up ip domain name by typing ***"ip domain-name R1.nettech"***
3) Generate crypto keys byte typing ***"crypto key generate rsa"*** it will ask for bits choose higher number like ***"4096"***
4) Set up username and secret password. Type ***"username admin (anyname) secret ccna (any password)"***
5) Set up VLAN for switch or Interfaces for Routers
6) Start up virtual link (vty). Type ***"line vty 0 15"*** for switches or 0 4 for routers. Turn on transport feature ***"transport input ssh"*** or telnet for less secure link.
7) You need to use local configs for logins, type in ***"login local"*** >> then exit

==***"YOU HAVE TO ENABLE SECRET AND SERVICE PASS ENCRYPTION TO REMOTELY LOGIN"***==



| **1)** | **hostname R1**                                        |
| ------ | ------------------------------------------------------ |
| **2)** | **ip domain-name R1.nettch**                           |
| **3)** | **crypto key generate rsa >> 4096**                    |
| **4)** | **username admin secret ccna**                         |
| **5)** | **set up VLAN and Router**                             |
| **6)** | **line vty 015 >> transport input ssh >> login local** |
| **7)** | **login local**                                        |
