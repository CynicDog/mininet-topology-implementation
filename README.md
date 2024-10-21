# Network Topology Implementations in Mininet 

This project is a hands-on journey using Mininet to build various network topologies, serving as a foundation for practical experience and deeper exploration of advanced networking and SDN implementations. 


## Environment Setup 

### Versions 
| **Component**              | **Details**        |
|----------------------------|--------------------|
| **OS**                     | Windows            |
| **Hypervisor**             | VirtualBox         |
| **Network Emulation Tool** | Mininet v2.3.0     |
| **Terminal Emulator**      | PuTTY v0.81        |
| Python                     | Python 2.7.12      | 

### Installations  

#### VirtualBox 
Go to package download page ([https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)) and install a package that suits for your OS. 

#### Mininet 
Go to the VM image download page ([https://github.com/mininet/mininet/releases/](https://github.com/mininet/mininet/releases/)) and download the zip file that matches your system architecture and the Ubuntu version compatible with VirtualBox. 

#### PuTTY 
Go to PuTTY's download page ([https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)) and download an installer package. 

### Emulate Ubuntu Server Terminal with PuTTY (Connect to Mininet via PuTTY) 
You need to configure the host-only Ethernet adapter to enable direct communication between the Mininet VM and the host machine, allowing PuTTY to connect using the assigned IP address. 
> [!NOTE]  
> VirtualBox's host-only network adapter is a virtual network interface in VirtualBox (or other hypervisors) that allows the VM (your Mininet VM) to communicate only with the host machine (your physical computer).

Here's the step to connect to Mininet via PuTTY: 

1. Open the VirtualBox application by running the downloaded Mininet image (an executable OVF file), then navigate to the main Tools menu and select Host Network Manager.
2. Click the Add button to create a new host-only network adapter, then switch to the DHCP Server tab to enable the DHCP server for the adapter. You should see an adapter configuration that looks like this:
   ```
   NAME                                        IPv4 Prefix       IPv6 Prefix     DHCP Server
   VirtualBox Host-Only Ethernet Adapter       192.168.56.1/24                   Enabled
   VirtualBox Host-Only Ethernet Adapter #2    192.168.64.1/24                   Enabled 
   ```
   
3. Go to the Mininet VM settings, navigate to the Network section, click the Adapter 2 tab, and connect it to the host-only adapter you created (`VirtualBox Host-Only Ethernet Adapter #2`). If the Mininet VM is running, you won't be able to add a new adapter, so make sure that the Mininet VM is completely turned off. 
4. Run the Mininet VM, and find the internet address of Mininet's primary network interface `eth0` as below:
   ```
   mininet@mininet-vm:~$ ifconfig
   eth0     Link encap:Ethernet  HWaddr 08:00:27:b3:40:bb
            inet addr:192.168.64.3  Bcast:192.168.64.255  Mask:255.255.255.0
            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            RX packets:106 errors:0 dropped:0 overruns:0 frame:0
            TX packets:78 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:17114 (17.1 KB)  TX bytes:15468 (15.4 KB)
  
   lo       Link encap:Local Loopback
            inet addr:127.0.0.1  Mask:255.0.0.0
            ... 
   ```
5. Open PuTTY and connect to the IP address `192.168.64.3` using port 22. When prompted, log in with the username and password, both set to `mininet`. That's it! 

</details>


## Contents 

### Topologies 
- [Linear Topology](https://github.com/CynicDog/network-topology-implementations-in-mininet/blob/main/1_Topologies/README.md#1-linear-topology)

### Network Security and Access Control 
- [Layer 2 Network Isolation](https://github.com/CynicDog/network-topology-implementations-in-mininet/tree/main/2_Network_Security_Access_Control#1-layer-2-network-isolation-within-single-switch-vlans) 
- [Inter-VLAN Routing](https://github.com/CynicDog/network-topology-implementations-in-mininet/tree/main/2_Network_Security_Access_Control#2-inter-vlan-routing-within-a-network-with-three-subnets)
- [Spanning Tree Protocol in Open vSwitches](https://github.com/CynicDog/network-topology-implementations-in-mininet/tree/main/2_Network_Security_Access_Control#3-spanning-tree-protocol-in-open-vswitches)

### Traffic Engineering and QoS 

### Network Function Virtualization
