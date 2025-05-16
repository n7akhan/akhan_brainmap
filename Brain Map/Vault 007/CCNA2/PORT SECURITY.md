
+ You wanna secure the ports of your switch at level 2
```
Switch> enable
Switch# configure terminal
Switch(config)# interface fastEthernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
```

+ When you want to see your port security brief you run a 
```
show port-security interface fastEthernet 0/1
```

+ This will show you
```
S1#show port-security interface fastEthernet 0/1
Port Security : Enabled
Port Status : Secure-up
Violation Mode : Shutdown
Aging Time : 0 mins
Aging Type : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses : 1
Total MAC Addresses : 0
Configured MAC Addresses : 0
Sticky MAC Addresses : 0
Last Source Address:Vlan : 0000.0000.0000:0
Security Violation Count : 0
```

+ To allow a certain amount of devices to connect to a specific port tracking them within MAC addresses
```
S1(config-if)#switchport port-security maximum {how ever many devices}
S1(config-if)#switchport port-security mac-address aaaa.bbbb.1234
S1(config-if)#switchport port-security mac-address sticky (THIS REMEMBERS TO CURRENT DEVICE MAC ADDRESS)
```