
# HSRP (Hot Standby Router Protocol) Explained!

## What is HSRP?
**HSRP** is a Cisco redundancy protocol that allows multiple routers to act as a single **default gateway** for hosts. It ensures **high availability** by having backup routers ready to take over if the active one fails.

---

## Virtual Router

HSRP creates a **Virtual Router** with:
- A **Virtual IP** (used as default gateway by hosts)
- A **Virtual MAC** (used in ARP responses)

```text
+------------------------+
|   Virtual Router       |
|------------------------|
| Virtual IP: 192.168.1.1|
| Virtual MAC: Auto-gen  |
+------------------------+
```

---

## Roles in HSRP

| Role        | Description                              |
|-------------|------------------------------------------|
| Active      | Forwards traffic, owns Virtual IP/MAC    |
| Standby     | Backup, ready to take over if Active fails |
| Listen      | Other routers in the group, no action    |

---

## How Election Works

- **Priority** value decides who becomes Active.
- Default = 100; higher is better.
- **Tie-breaker**: Higher IP address wins.

```text
+--------+------------+-----------+
| Router | Priority   | Role      |
+--------+------------+-----------+
| R1     | 110        | Active    |
| R2     | 100        | Standby   |
| R3     | 90         | Listening |
+--------+------------+-----------+
```

---

## What is Preemption?

- Allows a higher-priority router to **take over** when it comes back online.
- Must be **enabled manually**.

```bash
standby 1 preempt
```

---

## Basic HSRP Configuration

### Router R1
```bash
interface g0/0
 ip address 192.168.1.2 255.255.255.0
 standby 1 ip 192.168.1.1
 standby 1 priority 110
 standby 1 preempt
```

### Router R2
```bash
interface g0/0
 ip address 192.168.1.3 255.255.255.0
 standby 1 ip 192.168.1.1
 standby 1 priority 100
 standby 1 preempt
```

---

## HSRP State Transitions

```text
Initial -> Listen -> Speak -> Standby -> Active
```

---

## Summary

- Virtual IP is the gateway for hosts.
- Active router forwards traffic.
- Standby takes over if Active fails.
- Priority and preemption decide roles.

---

