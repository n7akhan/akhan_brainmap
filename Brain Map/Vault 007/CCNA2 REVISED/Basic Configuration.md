

**To Restore a Switch or Router to Default Configuration**  
 S1# **delete vlan.dat** (hit ‘enter’ to accept defaults) [Note: Only do this on a switch]  
 S1# **erase startup-config** (hit ‘enter’ to accept defaults [Router or Switch])  
 S1# **reload** (answer ‘no’ if asked to save current config [Router or Switch])  
 

**Router / Switch Basic Configuration**  
 R1# **configure terminal** (enter global configuration mode)  
 R1(config)# **hostname NAME** (configure the NAME of the Router or Switch)  
 R1(config)# **service password-encryption** (encrypt all passwords – except secret)  
 R1(config)# **enable secret PASSWORD** (make the privilege level password ‘PASSWORD’)  
 R1(config)# **no** **ip** **domain-lookup** (suppress DNS attempt when a command is mistyped)  
 R1(config)# **banner** **motd** **MESSAGE** (create a MESSAGE that will display when logging in)

  
 R1(config)# **line console 0** [zero] (enter the console connection configuration mode)  
 R1(config-line)# **password** **PASSWORD** (make the user level password ‘PASSWORD’)  
 R1(config-line)# **login** (instruct the router that you want it to check for a password)  
 R1(config-line)# **logging synchronous** (assists by keeping command entry more orderly)  
 R1(config-line)# **exec-timeout 0 0** [zeroes] (no timeout while configuring the router)

 R1(config)# **line** **vty** **0 4** [zero 4] (configure the same options as line console above)  
 S1(config)# **line** **vty** **0 15** [zero 15] (configure the same options in a switch)

 R1# **copy running-configuration startup-configuration** (save config in NVRAM)  
 R1(config)# **!** (remark – makes no configuration changes)  
 

To Enable Management

**For Switch Management Interface Configuration**  
 S1(config)# **interface** **vlan** **1** (create a virtual host on the switch)  
 S1(config-if)# **description** _**Management**_ **interface** for this switch (optional description)  
 S1(config-if)# **ip** **address 192.168.100.50 255.255.255.0** (assign an IP address)  
 S1(config-if)# **ipv6 address 3ffe:b00:c18:1::3/64** (assign IPv6 address – if needed)  
 S1(config-if)# **no shut** (must turn it on)  
 

S1(config-if)# **exit** (leave interface config and return to global config)  
 S1(config)# **ip** **default-gateway 192.168.100.1** (must be on same subnet as Mngt interface)  
 S1(config)# **enable secret class** (must have an enable password for remote access)  
 S1(config)# **line** **vty** **0 15** (switches may have 16 VTY connections at once)  
 S1(config-line)# **password cisco** (must set a login password for telnet to be possible)  
 S1(config-line)# **login** (tell the VTY ports to ask for password from remote user)

 S1(config-line)# **logging synchronous** (avoid screen tear from messaging)  
 S1(config-line)# **transport input telnet** (allows only telnet for remote config – default)

**SSH Access**

 S1(config)# **hostname {hostname}**

 S1(config)# **ip domain-name {domain}  
**

 S1(config)# crypto key generate rsa

2048

 S1(config)# **username {username} secret {password}  
**

 **S1(config-line)# transport input ssh**

 **S1(config-line)# login local**