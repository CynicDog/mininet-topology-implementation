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

### Scenario

In this network configuration, three subnets are defined within a LAN, each assigned to a specific VLAN. The subnets are:

- **Subnet for VLAN 10**: `172.16.1.0/26`
- **Subnet for VLAN 20**: `172.16.1.64/26`
- **Subnet for VLAN 30**: `172.16.1.128/26`

The topology consists of two switches, Switch `s1` and Switch `s2`, each connected to three hosts. The hosts connected to Switch `s1` are:

- Host `h1` with IP address `172.16.1.2` (VLAN 10)
- Host `h2` with IP address `172.16.1.66` (VLAN 20)
- Host `h3` with IP address `172.16.1.130` (VLAN 30)

The hosts connected to Switch `s2` are:

- Host `h4` with IP address `172.16.1.3` (VLAN 10)
- Host `h5` with IP address `172.16.1.67` (VLAN 20)
- Host `h6` with IP address `172.16.1.131` (VLAN 30)

Switch `s1` and Switch `s2` are interconnected through a trunk link, allowing VLAN traffic to flow between them. Additionally, Switch `s2` connects to a Linux Router (`r1`), which facilitates inter-VLAN routing for communication across different subnets.

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

## 3. Spanning Tree Protocol in Open vSwitches 

### Execution 
Run `spanning_tree_protocol.py` script on mininet VM. 

### Scenario 

In this network configuration, there are four switches (`s1`, `s2`, `s3`, `s4`), with `s3` designated as the root bridge.

The MAC addresses of each switch are as follows:

- `s1`: `52:54:00:0f:ad:ab` (STP root path cost of 2, with the lowest MAC address)
- `s2`: `52:54:00:13:cf:9a` (STP root path cost of 4)
- `s3`: `52:54:00:16:5d:53` (STP root path cost of 0, set as the root bridge)
- `s4`: `52:54:00:1d:d2:3a` (STP root path cost of 2)

Although `s1` has the lowest MAC address, to ensure `s3` becomes the root bridge, the Bridge ID (BID) of `s3` should be set to `4096`, while the other switches should be set to `32768`.

There are two end hosts: `h1` is connected to the root bridge (`s3`), and `h2` is connected to `s2`.

### Report 

<details><summary><h4> Summary and STP status on switches </h4></summary>

```bash
mininet> s1 ovs-vsctl list Bridge 
_uuid               : 2261433c-8058-477f-a18f-64413d1afb69
auto_attach         : []
controller          : [9f7a463e-f655-4101-8f6f-a13991237e1d]
...
name                : "s2"
netflow             : []
other_config        : {datapath-id="0000000000000002", disable-in-band="true", dp-desc="s2", hwaddr="52:54:00:13:cf:9a", stp-priority="32768"}
ports               : [6d46c147-8a76-499d-ae29-9ff6438d3d6a, 7c9e802d-7c8d-4a03-ae21-fa83985b3ff8, e809a256-4dc2-4a1b-ae51-5d03f6bc60ec, f53f452f-2a6e-4863-bfbd-b4be50c8ae87]
protocols           : []
rstp_enable         : false
rstp_status         : {}
sflow               : []
status              : {stp_bridge_id="8000.52540013cf9a", stp_designated_root="1000.525400165d53", stp_root_path_cost="4"}
stp_enable          : true

_uuid               : b3fcc945-9120-4b04-9c72-721a5dd42cab
auto_attach         : []
controller          : [796d35e9-2148-470e-a397-e7953c8a7a91]
...
name                : "s1"
netflow             : []
other_config        : {datapath-id="0000000000000001", disable-in-band="true", dp-desc="s1", hwaddr="52:54:00:0f:ad:ab", stp-priority="32768"}
ports               : [37bfad50-c221-4ad0-9522-dccaf5b0c78e, 5538fe9e-6dcd-4db5-8335-a24fdeaf7018, ab580c08-a36c-4f0e-b914-56987490d9f4, d0cdbc07-a430-4985-b7f6-280f373bb0bf]
protocols           : []
rstp_enable         : false
rstp_status         : {}
sflow               : []
status              : {stp_bridge_id="8000.5254000fadab", stp_designated_root="1000.525400165d53", stp_root_path_cost="2"}
stp_enable          : true

_uuid               : 46f3752a-6ec7-41ad-b053-3190f9efd109
auto_attach         : []
controller          : [f0fe5228-a9f0-4778-ba23-980f58999e4d]
...
name                : "s3"
netflow             : []
other_config        : {datapath-id="0000000000000003", disable-in-band="true", dp-desc="s3", hwaddr="52:54:00:16:5d:53", stp-priority="4096"}
ports               : [7b1905c7-d412-4d24-b30e-7a6bb33106f8, 8553a44b-7c8c-41dc-8433-a8a32d0e1b13, c2eeb12b-cb95-4615-9beb-1febee3c335e, cb7c66ec-fb03-4805-9fe4-0317d3972ac7]
protocols           : []
rstp_enable         : false
rstp_status         : {}
sflow               : []
status              : {stp_bridge_id="1000.525400165d53", stp_designated_root="1000.525400165d53", stp_root_path_cost="0"}
stp_enable          : true

_uuid               : 335684e7-7921-41ef-b649-35a731e3291a
auto_attach         : []
controller          : [616ba894-a583-484a-bb0b-691115b91877]
...
name                : "s4"
netflow             : []
other_config        : {datapath-id="0000000000000004", disable-in-band="true", dp-desc="s4", hwaddr="52:54:00:1d:d2:3a", stp-priority="32768"}
ports               : [1c8b9954-7cb7-432d-a797-97c0961a42bb, 224ff46f-4d00-4bfa-940b-400a9d8570fd, aa496a4b-f53f-4731-9d97-e8269b759d3c, ff3f8e29-5fb3-48f9-aa71-4b5bceaf49a4]
protocols           : []
rstp_enable         : false
rstp_status         : {}
sflow               : []
status              : {stp_bridge_id="8000.5254001dd23a", stp_designated_root="1000.525400165d53", stp_root_path_cost="2"}
stp_enable          : true

```
> The root bridge `s3` has the lowest `stp_root_path_cost` of zero and the `stp_bridge_id` matches the `stp_designated_root` (`1000.525400165d53`). Additionally, `s3`'s `stp_priority` is set to `1000`, which is lower than the default `8000` priority of the other switches, further confirming that `s3` is the root bridge.

</details>

<details><summary><h4>Interface details and status of ports</h4></summary>

```bash
mininet> s1 ovs-vsctl list Interface 

_uuid               : 96e35133-7105-467e-8b0f-4225b410abd5
admin_state         : up
bfd                 : {}
bfd_status          : {}
cfm_fault           : []
cfm_fault_status    : []
cfm_flap_count      : []
cfm_health          : []
cfm_mpid            : []
cfm_remote_mpids    : []
cfm_remote_opstate  : []
duplex              : full
error               : []
external_ids        : {}
ifindex             : 655
ingress_policing_burst: 0
ingress_policing_rate: 0
lacp_current        : []
link_resets         : 0
link_speed          : 10000000000    [1] 
link_state          : up
lldp                : {}
mac                 : []
mac_in_use          : "02:09:f1:3e:48:e3"
mtu                 : 1500
name                : "s3-eth2"
ofport              : 2
ofport_request      : 2
options             : {}
other_config        : {}
statistics          : {collisions=0, rx_bytes=73, rx_crc_err=0, rx_dropped=0, rx_errors=0, rx_frame_err=0, rx_over_err=0, rx_packets=2, tx_bytes=1290, tx_dropped=0, tx_errors=0, tx_packets=25}
status              : {driver_name=veth, driver_version="1.0", firmware_version=""}
type                : ""
```
> [1] The `link_state` indicates the current status of the interface; in the context of STP (Spanning Tree Protocol), this value helps determine if the interface is active (up) or blocked, reflecting its convergence state.

</details>

<details><summary><h4> Bridge Protocol Data Units (BPDUs) on a port of the root bridge (`s3-eth1`) </h4></summary>

```bash
mininet> s1 tcpdump -i s3-eth1 -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on s3-eth1, link-type EN10MB (Ethernet), capture size 262144 bytes
01:54:23.304472 STP 802.1d, Config, Flags [none], bridge-id 8000.52:54:00:0f:ad:ab.8002, length 35  [1]
01:54:23.304527 STP 802.1d, Config, Flags [none], bridge-id 1000.52:54:00:16:5d:53.8001, length 35  [2] 
01:54:23.805076 STP 802.1d, Config, Flags [none], bridge-id 1000.52:54:00:16:5d:53.8001, length 35
01:54:25.307852 STP 802.1d, Config, Flags [none], bridge-id 1000.52:54:00:16:5d:53.8001, length 35
01:54:27.313642 STP 802.1d, Config, Flags [none], bridge-id 1000.52:54:00:16:5d:53.8001, length 35
...
```
> [1] Advertisement from `s1` as a root bridge candidate. 
>
> [2] BPDU from the selected root bridge (`s3`), which has the lowest bridge ID (priority 1000).

</details>

<details>
<summary><h4>Network connection in the same VLAN</h4></summary>

```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)
```
> The test may not show results due to the time required for STP convergence before forwarding traffic. Wait for the STP convergence and test again if failed. 

</details> 
