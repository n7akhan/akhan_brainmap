with descriptions for interfaces

# **SET UP SHH**

```
Router(config)#hostname R1
R1(config)#ip domain-name R1.homelab
R1(config)#crypto key generate rsa
R1(config)#username admin password class
R1(config)#line vty 0 4
R1(config-line)#transport input ssh
R1(config-line)#logging synchronous
R1(config-line)#login local
R1(config)#enable secret class
R1(config)#service password-encryption
```

**This basically sets up the SSH for inbound access**
**=============================================
# SET UP VLAN

==**ROUTER== set up
```
R1(config)#interface gigabitEthernet 0/0
R1(config-if)#ip address 192.168.1.1 255.255.255.0
R1(config-if)#no shutdown

This sets up the physical router with the IP

======================================================

R1(config)#interface gigabitEthernet 0/0.10
R1(config-subif)#encapsulation dot1Q 10
R1(config-subif)#ip address 192.168.10.1 255.255.255.0
R1(config-subif)#no shutdown
R1(config-subif)#description THIS IS VLAN 10 on GW

This sets up the VLAN 10 on GW
=======================================================

```

==**SWITCH== set up 
```
Switch(config)#hostname S1
S1(config)#interface gigabitEthernet 0/1
S1(config-if)#switchport mode trunk
S1(config-if)#switchport trunk allowed vlan 1,10
S1(config-if)#int vlan 10
S1(config-if)#vlan 10
S1(config-if)# ip address 192.168.10.2 255.255.255.0


This allows the interface pointed towards router to be like trunk and allow vlans

========================================================

S1(config)#interface fastEthernet 0/1
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 10
S1(config)#ip default-gateway 192.168.1.1

This makes it so that interface that the PC is connected to is looking for VLAN 10 TAGS
```

**This basically sets up vlan on router and switch. This makes switch have trunk ports pointed towards router and access ports towards PC's

===============================================

# SET UP DHCP ON ROUTER

```
R1(config)#ip dhcp excluded-address 192.168.1.1 192.168.1.99
R1(config)#ip dhcp pool x1
R1(dhcp-config)#default-router 192.168.1.1
R1(dhcp-config)#network 192.168.1.0 255.255.255.0

This makes it so that address after .99 can be used for DHCP

==========================================================

R1(config)#ip dhcp excluded-address 192.168.10.1 192.168.10.99
R1(config)#ip dhcp pool x10
R1(dhcp-config)#default-router 192.168.10.1
R1(dhcp-config)#network 192.168.10.0 255.255.255.0

This gives DHCP services to VLAN 10 PC's
```