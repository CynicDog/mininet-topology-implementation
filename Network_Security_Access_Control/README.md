# Network Security and Access Control

## 1. Network Isolation within Single Switch VLANs 

### Report

- Network connection in the same VLAN (h1 to h4):
```bash
mininet> h1 ping -c 3 h4
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=3.35 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.233 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.038 ms
```

- Network connection across different VLANs (h1 to h2):
```bash
mininet> h1 ping -c 3 h2
connect: Network is unreachable
```

- ARP Table for h1:
```bash
mininet> h1 arp -a
? (10.0.0.2) at a6:f4:1e:17:e7:6e [ether] on h1-eth0.10
```

- ARP Table for h2:
```bash
mininet> h2 arp -a
```
> Gives no output, which confirms that h2 has not resolved any ARP entries.

### Execution 
<details> 
  <summary> Run <code>single_switch_vlan_topology.py</code> script for a network isolation configuration in single switch VLAN environment as below </summary>
  <br> 
  
  ```bash
  root@mininet-vm:/home/mininet# python single_switch_vlan_topology.py
  *** Creating network
  *** Adding controller
  *** Adding hosts:
  h1 h2 h3 h4
  *** Adding switches:
  s1
  *** Adding links:
  (h1, s1) (h2, s1) (h3, s1) (h4, s1)
  *** Configuring hosts
  h1 h2 h3 h4
  *** Starting controller
  c0
  *** Starting 1 switches
  s1 ...
  *** Starting CLI:
  ```
</details>

