# Network Security and Access Control

## 1. Layer 2 Network Isolation within Single Switch VLANs 

### Execution 
Run `l2_network_isolation.py` script on mininet VM. 

### Report

<details>
<summary><h4>Network connection in the same VLAN (<code>h1</code> to <code>h4</code>)</h4></summary>

```bash
mininet> h1 ping -c 3 h4
PING 172.16.1.3 (172.16.1.3) 56(84) bytes of data.
64 bytes from 172.16.1.3: icmp_seq=1 ttl=64 time=0.188 ms
64 bytes from 172.16.1.3: icmp_seq=2 ttl=64 time=0.035 ms
64 bytes from 172.16.1.3: icmp_seq=3 ttl=64 time=0.039 ms
```

</details> 

<details>
<summary><h4>Network connection across different VLANs (<code>h1</code> to <code>h2</code>)</h4></summary>

```bash
mininet> h1 ping -c 3 h2
connect: Network is unreachable
```

</details> 

<details>
<summary><h4>ARP Table for <code>h1</code></h4></summary>

```bash
mininet> h1 arp -a
? (172.16.1.3) at 12:7d:cf:b1:12:9b [ether] on h1-eth0.10
```

</details> 

<details>
<summary><h4>ARP Table for <code>h2</code></h4></summary>

 ```bash
mininet> h2 arp -a
```
> Gives no output, which confirms that h2 has not resolved any ARP entries.

</details> 

## 2. Inter-VLAN Routing within a network with three subnets  

### Execution 
Run `l2_network_isolation.py` script on mininet VM. 

### Network Topology Scenario

In this network configuration, three subnets are defined within a LAN, each assigned to a specific VLAN. The subnets are:

- **Subnet for VLAN 10**: `172.16.1.0/26`
- **Subnet for VLAN 20**: `172.16.1.64/26`
- **Subnet for VLAN 30**: `172.16.1.128/26`

The topology consists of two switches, Switch `s1` and Switch `s2`, each connected to three hosts. The hosts connected to Switch `s1` are:

- Host `h1` with IP address `172.16.1.2` (VLAN 10)
- Host `h2` with IP address `172.16.1.66` (VLAN 20)
- Host `h3` with IP address `172.16.1.130` (VLAN 30)

The hosts connected to Switch `s2` are:

- `Host h4` with IP address `172.16.1.3` (VLAN 10)
- `Host h5` with IP address `172.16.1.67` (VLAN 20)
- `Host h6` with IP address `172.16.1.131` (VLAN 30)

Switch `s1` and Switch `s2` are interconnected through a trunk link, allowing VLAN traffic to flow between them. Additionally, Switch `s2` connects to a Linux Router `(r1)`, which facilitates inter-VLAN routing for communication across different subnets.

### Report 

<details>
<summary><h4>Network connections </h4></summary>

```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 X
h2 -> h1 h3 h4 h5 h6 X
h3 -> h1 h2 h4 h5 h6 X
h4 -> h1 h2 h3 h5 h6 X
h5 -> h1 h2 h3 h4 h6 X
h6 -> h1 h2 h3 h4 h5 X
r1 -> h1 h2 h3 h4 h5 h6
*** Results: 14% dropped (36/42 received)
```
> The hostname resolution failure for the router node from end hosts is expected. We can optionally edit the `/etc/hosts` file for each end host.

</details> 

<details>
<summary><h4>Router Routing Table Configuration</h4></summary>

```bash
mininet> r1 route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
172.16.1.0      0.0.0.0         255.255.255.192 U     0      0        0 r1-eth0.10
172.16.1.64     0.0.0.0         255.255.255.192 U     0      0        0 r1-eth0.20
172.16.1.128    0.0.0.0         255.255.255.192 U     0      0        0 r1-eth0.30
```

</details> 

<details>
<summary><h4>Router Interface Configuration </h4></summary>

```bash
mininet> r1 ifconfig
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

r1-eth0   Link encap:Ethernet  HWaddr fe:01:0b:3a:da:9b
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:219 errors:0 dropped:0 overruns:0 frame:0
          TX packets:215 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:20210 (20.2 KB)  TX bytes:19614 (19.6 KB)

r1-eth0.10 Link encap:Ethernet  HWaddr fe:01:0b:3a:da:9b
          inet addr:172.16.1.1  Bcast:172.16.1.63  Mask:255.255.255.192
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:74 errors:0 dropped:0 overruns:0 frame:0
          TX packets:72 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:5488 (5.4 KB)  TX bytes:6552 (6.5 KB)

r1-eth0.20 Link encap:Ethernet  HWaddr fe:01:0b:3a:da:9b
          inet addr:172.16.1.65  Bcast:172.16.1.127  Mask:255.255.255.192
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:73 errors:0 dropped:0 overruns:0 frame:0
          TX packets:72 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:5404 (5.4 KB)  TX bytes:6552 (6.5 KB)

r1-eth0.30 Link encap:Ethernet  HWaddr fe:01:0b:3a:da:9b
          inet addr:172.16.1.129  Bcast:172.16.1.191  Mask:255.255.255.192
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:72 errors:0 dropped:0 overruns:0 frame:0
          TX packets:71 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:5376 (5.3 KB)  TX bytes:6510 (6.5 KB)
```

</details> 

<details>
<summary><h4>Switch Configuration and VLAN Trunks </h4></summary>

```bash
mininet> s1 ovs-vsctl show
063b1597-ee6f-47f2-b09f-cf8e06c009e0
    Bridge "s1"
        Controller "tcp:127.0.0.1:6653"
            is_connected: true
        fail_mode: secure
        Port "s1"
            Interface "s1"
                type: internal
        Port "s1-eth3"
            Interface "s1-eth3"
        Port "s1-eth4"
            trunks: [10, 20, 30]
            Interface "s1-eth4"
        Port "s1-eth1"
            Interface "s1-eth1"
        Port "s1-eth2"
            Interface "s1-eth2"
    Bridge "s2"
        Controller "tcp:127.0.0.1:6653"
            is_connected: true
        fail_mode: secure
        Port "s2-eth1"
            Interface "s2-eth1"
        Port "s2-eth3"
            Interface "s2-eth3"
        Port "s2-eth4"
            trunks: [10, 20, 30]
            Interface "s2-eth4"
        Port "s2-eth2"
            Interface "s2-eth2"
        Port "s2"
            Interface "s2"
                type: internal
        Port "s2-eth5"
            Interface "s2-eth5"
    ovs_version: "2.5.9"
```
  
</details> 

<details>
<summary><h4> ARP Table for Host <code>h1</code></h4></summary>

```bash
mininet> h1 arp -a
? (172.16.1.1) at fe:01:0b:3a:da:9b [ether] on h1-eth0.10
? (172.16.1.3) at 22:e6:49:31:ac:af [ether] on h1-eth0.10
```

</details> 
