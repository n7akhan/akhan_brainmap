# Setup router-based DHCP
## Overview
## Configure LAN Interface
```ios
Router> enable 
Router# configure terminal
! Set hostname
Router(config)# hostname R1
R1(config)#
! Configure LAN interface (in this ex. g0/0)
R1(config)# int g0/0
! configure IP Address
R1(config-if)# description LAN GW
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shut
R1(config-if)# exit
```

## Configure the Exclusion
```
! Setup the exclusion pool
! SNMs are NOT needed
R1(config)# ip dhcp excluded-address {low ip address} {high ip address}
```

## Configure DHCP
```
! Create the pool
R1(config)# ip dhcp pool {pool name}
! Set the gateway ip
R1(dhcp-config)# default-router {Gateway IP Address}
! Set the network information
! Must include SNM
R1(dhcp-config)# network {Network Address} {SNM}
! *optional* Set the domain name IE netech.lab
R1(dhcp-config)# domain-name {domain name and suffix}
! *optional* Set the DNS server
R1(dhcp-config)# dsn-server {DNS IP Address}
! Save the DHCP configuration and exit
R1(dhcp-config)# exit
```