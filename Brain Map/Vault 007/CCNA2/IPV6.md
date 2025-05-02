- 128 bits, separated among 8 groups, 2 bytes per group
- We use semi colons **:** instead of periods as seen in ipv4

# IPV6 RULES

F00D: CAFE : 0000 : 0000 : 0000 : 0000 : 0000: 0001

**RULE 1** : We can remove leading zeros!
- F00D : CAFE : 0 : 0 : 0 : 0 : 0 : 1 
**RULE 2 :** We can remove **ALL CONTIGUOUS ZEROS** by replacing them with a ::
- F00D : CAFE : : 1

==**We can only do this ONCE to avoid ambiguity**==

FF: 0 : 0 : 0 : 1 : 0 : 0 : 1 -----------> FF : : 1 : 0 : 0 : 1 or FF : 0 : 0 : 0 : 1 : : 1



