# Network Topology Implementations in Mininet 

This project is a hands-on journey using Mininet to build various network topologies, serving as a foundation for practical experience and deeper exploration of advanced networking and SDN implementations. 

## Contents

### Topologies 
- [Linear Topology](https://github.com/CynicDog/network-topology-implementations-in-mininet/blob/main/1_Topologies/README.md#1-linear-topology)

### Network Security and Access Control 
- [Layer 2 Network Isolation](https://github.com/CynicDog/network-topology-implementations-in-mininet/tree/main/2_Network_Security_Access_Control#1-layer-2-network-isolation-within-single-switch-vlans) 
- [Inter-VLAN Routing](https://github.com/CynicDog/network-topology-implementations-in-mininet/tree/main/2_Network_Security_Access_Control#2-inter-vlan-routing-within-a-network-with-three-subnets)
- [Spanning Tree Protocol in Open vSwitches](https://github.com/CynicDog/network-topology-implementations-in-mininet/tree/main/2_Network_Security_Access_Control#3-spanning-tree-protocol-in-open-vswitches)

### Traffic Engineering and QoS 

### Network Function Virtualization

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

## Software Defined Networking (Coursera | The University of Chicago) 
*by Prof. Nick Feamster*  

<details><summary>Below are my key takeaways from the course.</summary>

<details><summary><h3>Course Overview</h3></summary>

### Software Defined Networking (SDN) Overview

**Definition:**  
Software Defined Networking (SDN) is a network architecture that separates the **data plane**, which forwards traffic, from the **control plane**, which determines how traffic is routed.

**Key Features:**  
1. **Separation of Planes:**  
   - The **data plane** consists of programmable switches.  
   - The **control plane** consists of controllers and applications that manage traffic forwarding.  
   - This separation allows centralized control of network behavior via a high-level control program.

2. **Comparison with Conventional Networking:**  
   - Traditional networks integrate hardware with specific software, limiting flexibility and innovation.  
   - SDN decouples these components, enabling easier upgrades and customizations.  

3. **Architecture:**  
   - The **data plane** handles traffic forwarding.  
   - The **control plane** communicates with the data plane using standardized interfaces like OpenFlow.  
   - High-level applications manage tasks such as load balancing and security.

**Historical Context:**  
- SDN was inspired by challenges in configuring distributed networks where independent device-specific configurations led to bugs and unpredictability.  
- Centralized control points, such as the Routing Control Platform (RCP), simplified network management.  
- The concept evolved into architectures like the 4D architecture, with distinct layers for data, discovery, dissemination, and decision-making.  

**Infrastructure Components:**  
1. **Control Plane:**  
   - Centralized logic for traffic forwarding based on policies.  
   - Operates independently from hardware devices.  
2. **Data Plane:**  
   - Comprises programmable switches controlled by the control plane.

**Advantages of SDN:**  
1. **Simplified Coordination:** Centralized programs enable easier coordination of network devices.  
2. **Improved Evolvability:** Decoupling hardware and software allows independent updates and innovations.  
3. **Enhanced Reasoning:** High-level control programs make network behavior easier to understand and manage.  
4. **Adoption of Computer Science Principles:** Techniques from software engineering and testing can be applied to networking.  

**Applications:**  
SDN is utilized in various domains, including data centers, backbone networks, enterprise networks, internet exchange points, and home networks.  

<details><summary><h3>Quiz</h3></summary>

### Q. Which of the following are true about Classless Interdomain Routing (CIDR)?

A. CIDR slowed the rate of Internet routing table growth because prefixes no longer had to be allocated in fixed-size blocks. ✅ 
> CIDR introduced variable-length subnet masks, which allowed more efficient IP address allocation and reduced the growth rate of routing tables.  

B. In an Internet forwarding table with CIDR, there can only be one unique matching entry for any given IP address.
> This is incorrect. In CIDR-based forwarding, multiple entries may match a given IP address, and the router selects the longest prefix match.

C. The prefix length for a CIDR prefix can be anywhere in the range from 0 to 32 bits. ✅
> This is correct. CIDR supports prefix lengths ranging from 0 to 32 bits, offering flexibility in IP address allocation.

D. The only sizes for an IP address allocation before CIDR were 8, 16, or 24 bits.
> This is incorrect. Before CIDR, IP address allocation was based on Class A, Class B, and Class C addressing, with different divisions between the network and host portions. Classful addressing had more complex rules, with Class A using 8 bits for the network portion, Class B using 16 bits, and Class C using 24 bits. It wasn't just limited to fixed-size blocks.

---

### Q. Which of the following are true about how DNS lookups work?

A. If your local DNS resolver caches an NS record for google.com for multiple days, all clients who use that DNS resolver will continue using the same IP address to reach Google’s web server until that NS record expires.  
> This is incorrect. An NS record does not directly resolve to an IP address but points to the authoritative name servers. Cached NS records only ensure that subsequent queries for google.com will be directed to those name servers.

B. An NS-record query for a DNS lookup will return the name(s) of the authoritative name server(s) for that domain. ✅  
> An NS record provides the names of the authoritative name servers for a domain, which are responsible for providing the domain's IP or other record types.  

C. A DNS A-record query for google.com will only return a single IP address at a time.  
> This is incorrect. DNS A-record queries often return multiple IP addresses for a domain to support load balancing or redundancy.  

D. All DNS PTR records are maintained by a single organization in-addr.arpa.  
> This is incorrect. PTR records, used for reverse DNS lookups, are maintained by various organizations, often delegated by IP block owners.  

E. An MX-record query for a DNS lookup will return the IP address of the mail server for that domain.  
> This is incorrect. An MX record returns the hostname of the mail server, not its IP address. Further queries are needed to resolve the hostname to an IP.  

---

### Q. Which of the following are true about traffic control with BGP?

A. A network operator can use the BGP local preference attribute to control outbound traffic from his or her AS to a destination. ✅  
> The **local preference** attribute influences the selection of outbound paths within an AS by prioritizing preferred routes to a destination.  

B. A network operator can use BGP AS path prepending to control outbound traffic from his or her AS to a destination.  
> This is incorrect. **AS path prepending** is used to manipulate the AS path length seen by external networks, primarily to influence inbound traffic, not outbound traffic.  

C. A network operator can use the BGP local preference attribute to control inbound traffic from his or her AS to a destination.  
> This is incorrect. The **local preference** attribute is only applicable within an AS and cannot directly influence inbound traffic.  

D. A network operator can use BGP AS path prepending to control inbound traffic from his or her AS to a destination. ✅  
> **AS path prepending** increases the AS path length for specific routes, making them less attractive to external networks, thereby influencing inbound traffic.  

---

### Q. Which of the following are true about layering?

A. The transport layer uses port numbers. ✅  
> This is correct. The **transport layer** (Layer 4) uses **port numbers** to identify specific processes or services running on devices for communication, such as **TCP** and **UDP**.

B. The destination address in the link layer header is always the address of the next layer-3 node along an end-to-end IP path.  
> This is incorrect. The **link layer** (Layer 2) address is typically the **MAC address** of the device directly connected to the sender or receiver, not necessarily the next hop in the IP path.

C. The network layer has only a single protocol in widespread use today, representing what we call the “narrow waist”. ✅  
> This is correct. The **network layer** (Layer 3) is commonly dominated by **IP** (Internet Protocol), which acts as the "narrow waist" of the network stack, with a single protocol (IPv4 or IPv6) in widespread use.

D. The network layer guarantees reliable, in-order delivery of packets.  
> This is incorrect. The **network layer** (Layer 3), particularly **IP**, does not guarantee **reliable, in-order delivery**. These guarantees are handled by higher layers like the **transport layer** (e.g., TCP).

---

### Q. Which of the following are **not true** about packet switching?

A. Traffic running over a packet-switched network between two endpoints will never be dropped by intermediate nodes along the path. ✅  
> This is incorrect. **Packet-switched networks** can drop packets if there is congestion or insufficient resources at intermediate nodes.

B. A user of a packet-switched network might occasionally get a “busy signal” if there are too many users on the network. ✅
> This is incorrect. In a **packet-switched network**, users do not experience "busy signals"; instead, they may experience **increased latency** or **packet drops** during congestion.

C. Traffic running over a packet-switched network between two endpoints will always experience predictable latency. ✅  
> This is incorrect. **Latency** in packet-switched networks varies depending on congestion, routing, and other dynamic factors, making it unpredictable.

D. Once a connection is established between two endpoints in a packet-switched network, the end-to-end route cannot change, or the connection must be re-established. ✅  
> This is incorrect. **Packet-switched networks** dynamically route packets, and the route can change without requiring a re-establishment of the connection.

---

### Q. Which of the following are true about content distribution networks?

A. Content distribution networks typically redirect Web clients to a nearby Web cache by rewriting the IP address of packets sent from the client to the IP address of the nearby Web cache.  
> This is **incorrect**. **CDNs** usually redirect traffic to nearby caches through **DNS resolution** rather than by rewriting the IP addresses in the packets. The client is directed to a CDN server with a more optimal response time.

B. Content distribution networks can improve the performance that a client sees by reducing the network latency between the client and the content that it is downloading. ✅  
> This is **correct**. **CDNs** cache content closer to end users, reducing the distance data must travel and **lowering latency**.

C. Content distribution networks can reduce transit expenses for a content provider by enabling much of the provider’s content to be served from a nearby network, sometimes even from a cache that is within the client’s own network. ✅  
> This is **correct**. By using **distributed caches** at edge locations, **CDNs** can reduce the load on origin servers and minimize **transit costs** by serving content locally.

D. Real-time content such as video streams cannot be distributed from a content distribution network.  
> This is **incorrect**. **CDNs** can efficiently deliver **real-time content** such as **live video streams** by utilizing adaptive streaming technologies and edge servers to reduce latency and buffering.

---

### Q. Which of the following are true about 802.11 wireless medium access control?

A. A wireless sender can avoid causing a collision at the receiver by performing a “carrier sense” to determine whether any other sender wants to transmit at the time that it wishes to send a packet.  
> This is incorrect. **Carrier sense** helps avoid collisions at the sender, but it cannot guarantee the receiver is collision-free due to the **hidden terminal problem**.

B. Disabling RTS/CTS necessarily lowers the effective throughput of the wireless network, since more collisions will occur at the receiver without RTS/CTS enabled.  
> This is incorrect. While disabling **RTS/CTS** can increase the risk of collisions, it does not necessarily lower throughput because RTS/CTS introduces overhead, and its impact depends on network conditions.

C. Only wireless networks can have collisions at the receiver; such collisions are not possible on wired Ethernet networks.   
> This is incorrect. Wired Ethernet networks can also experience collisions in older, shared-media setups (e.g., hub-based Ethernet), but these are less common in modern switched networks.

D. Using RTS/CTS (“request to send”, “clear to send”) control reduces the overall achievable throughput of the wireless network. ✅  
> This is correct. **RTS/CTS** reduces collisions but introduces additional control frame overhead, lowering the network's effective throughput.

---

### Q. Which of the following are true about video streaming?

A. A larger playout buffer at the client allows the client more time to recover from lost packets. ✅  
> This is correct. A larger **playout buffer** enables the client to smooth out any interruptions due to packet loss, helping maintain continuous playback.

B. Since UDP provides no reliable delivery guarantees, a video streaming application that uses UDP as its transport cannot recover from any packet loss in the video stream.  
> This is incorrect. **UDP** does not guarantee delivery, but a video streaming application can implement its own error recovery mechanisms, such as forward error correction or packet retransmission, to recover from some packet loss.

C. Using TCP for video streaming could result in larger delays between transmission and playout than streaming the same video with UDP. ✅  
> This is correct. **TCP** introduces additional overhead due to connection establishment, congestion control, and retransmission, leading to **larger delays** compared to **UDP**, which is faster but less reliable.

D. Using UDP to stream a video instead of TCP is appropriate if the client is more concerned about low delay and interactivity than it does about receiving a high-quality stream. ✅  
> This is correct. **UDP** is often used for **real-time streaming** (e.g., video, VoIP) because it prioritizes **low latency** over reliability, which is beneficial for interactive applications, even if it results in some packet loss.

---

### Q. Which of the following are true about TCP?

A. A TCP sender controls its sending rate by adjusting the number of unacknowledged packets that can be sent over the network at any time. ✅ 
> This is correct. **TCP** uses a **sliding window** mechanism to control its sending rate. The sender can only send as many packets as the receiver's advertised window and the congestion window allow.

B. TCP’s congestion avoidance algorithm causes the sender to reduce its sending rate by a factor of two when it sees a packet loss. ✅  
> This is correct. **TCP** employs **congestion control** mechanisms like **slow start** and **congestion avoidance**, where it reduces the sending rate by half (multiplicative decrease) when it detects packet loss, typically through **timeout** or **duplicate acknowledgments**.

C. A TCP sender and receiver use a “three-way hand shake” both to setup and to terminate the TCP connection.  
> This is incorrect. The **three-way handshake** is used to **establish** a **TCP connection**, not to terminate it. The connection termination is performed using a **four-way handshake**.

D. TCP guarantees that the receiver sees the same in-order stream of bytes that the sender transmitted. ✅  
> This is correct. **TCP** provides **reliable, in-order delivery** of data, ensuring that the receiver receives the bytes in the exact order they were sent by the sender, even if packets are delayed or lost and retransmitted.

---

### Q. Which of the following are true about the denial of service attacks (and defenses)?

A. In a “SYN Flood” attack, each TCP SYN packet that a victim receives causes it to set up TCP connection state. ✅  
> This is correct. In a **SYN flood** attack, the attacker sends numerous **SYN packets** to the victim with a **spoofed** source IP address. The victim attempts to establish TCP connections but is unable to complete them, consuming its resources and leaving it in a half-open state.

B. If every network on the Internet performed stateless ingress filtering to defend against source IP spoofing, the DNS reflection attack would not work. ✅ 
> This is correct. Stateless ingress filtering helps prevent source IP spoofing by checking that packets entering a network have a source IP address that matches the network from which they were received. In the case of a DNS reflection attack, this filtering would prevent attackers from sending DNS queries with spoofed source IP addresses (i.e., victim addresses), making it ineffective.

C. A “DNS Reflection” attack requires the attacking client to “spoof” the source IP address of the packet containing the DNS request. ✅  
> This is correct. In a **DNS reflection** attack, the attacker **spoofs** the source IP address of the DNS request to be that of the victim. The DNS server then responds to the victim, overwhelming it with unsolicited traffic.

D. If every network on the Internet performed stateless egress filtering to defend against source IP address spoofing, the DNS reflection attack could not be carried out.  
> This is incorrect. **Stateless egress filtering** ensures that packets leaving a network do not have a source IP address that was not assigned within the network. However, **DNS reflection** attacks can still occur even with egress filtering because the attacker is not directly sending packets from its own IP but instead using the victim's IP in the spoofed request.

</details>

</details>

<details><summary><h3>Module 1 - History and Evolution of Software Defined Networking</h3></summary>

## The Central Controls 

### Timeline of SDN Development
The timeline of SDN extends from the 1980s to the present. Understanding its history provides insights into the origins of SDN principles and their relationship to existing architectural themes in packet-switched computer networks. These themes often trace back to earlier systems, including the telephone network.

### Key Chapters in SDN History
SDN history can be categorized into four main chapters:
1. **Evolution of Supporting Technologies**  
   This includes programmable data planes and the separation of control and data planes, detailing their origins and advancements.
2. **Control and Data Plane Separation**  
   The historical development and evolution of communication channels between networks.
3. **Control Channel Convergence**  
   The emergence of unified standards, such as OpenFlow, which consolidate control and data plane interactions.
4. **Network Virtualization**  
   This is often referred to as the "killer app" for SDN.

### Evolution of Supporting Technologies

#### Origins of Central Network Control
The concept of central network control emerged in the early 1980s. AT&T's *Network Control Point (NCP)* exemplified this, marking a significant shift from earlier paradigms where control and data planes operated together. This earlier model, known as **in-band signaling**, transmitted both data (e.g., voice) and control over the same channel.

- **In-Band Signaling Characteristics**  
  - Frequencies such as 2600 Hz reset phone trunk lines.
  - Pulses were used to route calls and establish circuits.

While simple, this system was brittle and insecure. For instance, devices like Steve Wozniak's *blue box* exploited these vulnerabilities to manipulate phone networks.

#### Introduction of Network Control Point (NCP)
In response to these limitations, AT&T developed the NCP, which separated signaling from voice and data. Key advancements included:
1. Deployment of on-demand services, such as 800-number routing.
2. Faster introduction of new services by leveraging a centralized control point that interfaced with backend databases.

The NCP architecture enabled:
- Elimination of in-band signaling, reducing operational costs.
- Efficient allocation of resources by monitoring circuit status (busy/idle).
- Rapid service development through exposed primitives, such as collecting digits or managing billing records.

An early envisioned service was the *person locator*, where a user could register their location in an NCP database. Calls to a generic number would then route to the user's current location. This functionality laid the foundation for modern 800-call routing.

#### Benefits of Centralized Control
The advantages of central control included:
1. A network-wide vantage point for direct observation of behavior.
2. Independent evolution of infrastructure, data, and services.

## History of Active Networks  

### Emergence and Motivation  
Active networks, developed in the 1990s, introduced the concept of programmable routers and switches that could perform computations on packets in transit. Unlike traditional routers that only forward packets, active routers could execute user-defined operations. This innovation was driven by challenges in integrating new technologies, addressing redundant processes in protocol layers, and supporting rapid deployment of new services.  

Traditional networks struggled with innovation due to the long cycle from prototype to deployment, often taking years. Active networks aimed to overcome these barriers by allowing programmable nodes where routers could dynamically execute new services, enabling faster experimentation and user-driven innovation.  

### Supporting Technologies  
The rise of active networks coincided with advancements in safe mobile code execution, such as Java applets and specialized operating systems like Exokernel and SPIN. These technologies provided the foundation for implementing active network capabilities securely and efficiently.  

### Two Approaches to Active Networks  
Active networks followed two main approaches:  
1. **Capsule-Based Execution**  
   - Packets carried executable programs to be run on each router they traversed.  
   - This model allowed custom operations per packet but required routers to support execution environments.  

2. **Programmable Switches**  
   - Code was pre-installed on routers, enabling custom processing of packets based on header fields.  
   - This approach, focusing on selective programmability, resembled modern SDN concepts.  

### Notable Projects  
Several projects explored active network concepts:  
- **ANTS (MIT)**: Used Java capsules for packet processing.  
- **SwitchWare (Penn)**: Introduced programmable switches and switchlets.  
- **Smart Packets (BBN)**: Focused on network management through active methods.  
- **NetScript (Columbia)**: Developed a language for programmable packet pipelines.  

### Decline and Legacy  
Despite its potential, active networks did not gain widespread adoption. Factors included high hardware costs, limited applications, and a lack of user-friendly deployment models. The emphasis on end-user programmability rather than operational needs also contributed to its decline.  

However, active networks laid the foundation for modern SDN principles by introducing programmable data planes and dynamic control. Concepts like programmable switches and modular processing influenced SDN and its applications in virtualization and middlebox unification. Today, the lessons from active networks continue to shape network programmability efforts.  

## Network Virtualization  

### Overview  
Network virtualization refers to the abstraction of physical network infrastructure into multiple logical, isolated networks. It allows different users or services to operate independently within their own virtual networks, even though they share the same physical resources. This approach supports better resource management, isolation, and customization, enabling organizations to optimize their networks for various use cases without interference between virtual networks.

### Early Developments  
The early groundwork for network virtualization came from technologies like **Virtual LANs (VLANs)**, which enabled multiple logical networks to share the same physical infrastructure. VLANs allowed network administrators to segment networks logically without requiring additional hardware.  

In the late 1990s, **Tempest architecture** further advanced the concept by introducing the idea of "switchlets," which allowed different controllers to independently manage logical switches on a shared physical switch. This was a step toward the modern **Software-Defined Networking (SDN)** model, where control is separated from data forwarding.

### Benefits and Challenges 
- **Benefits:**  
  - **Flexibility in Resource Allocation:** Virtual networks can be customized according to specific needs, enabling different configurations on the same physical network.  
  - **Faster Service Deployment:** With virtual networks, new network services or protocols can be deployed quickly without needing new hardware or extensive reconfiguration of existing infrastructure.  
  - **Enhanced Isolation and Security:** Each virtual network is isolated from others, ensuring that a failure or security breach in one network doesn't affect others running on the same physical infrastructure.  

- **Challenges:**  
  - **Management Complexity:** Coordinating and managing virtual networks across shared infrastructure can be complex, requiring sophisticated tools to ensure proper resource allocation and security.  
  - **Virtualization Overhead:** The process of abstracting and virtualizing networks introduces additional computational and memory overhead, which can affect performance.

### Key Virtualization Architectures  

1. **Tempest Architecture and Switchlets**  
   - The **Tempest architecture** emerged in the late 1990s, aiming to decouple control and data planes in networking hardware.  
   - **Switchlets** were an important component of Tempest, allowing for programmable and dynamic control of switches. Each switchlet acted as a separate module that could be independently programmed and managed.  
   - This model allowed multiple network operators to share a physical switch, each with their own virtualized control, while still maintaining a high level of flexibility and efficiency.  
   - The Tempest architecture influenced early SDN concepts by showing how networks could be managed through software-driven solutions, with modular components working together to provide customized networking services.
     
2. **VINI (Virtual Network Infrastructure)**  
   - Launched in 2006, VINI allowed researchers and developers to create virtual network topologies for experimentation.  
   - It used tunneling protocols and software routers such as **XORP** and **Click** to enable realistic network conditions in a controlled environment.  
   - VINI’s architecture helped bridge the gap between laboratory experiments and real-world network deployment, allowing new routing software to be tested on virtual networks before scaling to physical networks.

3. **Cabo (Concurrent Architectures are Better than One)**  
   - Cabo proposed a separation between infrastructure providers and service providers.  
   - ISPs (Infrastructure Service Providers) could share physical routers while service providers (e.g., network operators or enterprises) could innovate and manage their own virtual networks on top of this shared infrastructure.  
   - An example project, **FON**, allowed individuals to share their wireless bandwidth with others in exchange for services or commercial use. It demonstrated the potential of sharing network resources through a virtualized model while maintaining secure isolation between users.

### Influence on SDN  
Network virtualization directly influenced the development of **Software-Defined Networking (SDN)** by introducing several key concepts:  
- **Logical Abstraction:** Network virtualization showed how networks could be abstracted into logical entities (virtual networks) on top of shared physical infrastructure, laying the foundation for SDN’s abstraction of control and data planes.  
- **Separation of Control and Data Planes:** The concept of decoupling the management and forwarding layers of a network, initially explored through virtualized networks, became a core principle of SDN.  
- **Dynamic Programmability:** Network virtualization enabled user-driven experimentation and innovation, which eventually led to SDN’s dynamic, software-driven approach to network configuration and management.

### Legacy  
While early network virtualization projects faced challenges such as high hardware costs and scalability issues, they laid the groundwork for modern networking paradigms. Many of the ideas, such as **programmable switches** and **modular processing**, were influential in the development of SDN and modern networking technologies like **Network Functions Virtualization (NFV)** and **cloud-based networking**. The lessons learned from network virtualization continue to shape the evolution of network programmability and the use of virtualization in data center and cloud environments today.

## The Evolution of Control in Packet-Switched Networks

### Timeline of Control Channel Evolution
The development of separate control and data planes in networking traces back to early innovations in packet-switched network management. The history is shaped by key developments such as the *FORCES protocol*, *Routing Control Platforms (RCP)*, and the rise of open hardware, which set the stage for modern SDN (Software-Defined Networking) practices.

### Key Phases in Control Plane Evolution
The evolution of control mechanisms in packet-switched networks can be divided into several significant phases:
1. **FORCES Protocol and Early Standardization**  
   Early attempts at separating control functions through standardized protocols like FORCES.
2. **Hijacking Existing Protocols**  
   Using pre-existing protocols (e.g., BGP) for control in network routing.
3. **Emergence of Open Hardware and OpenFlow**  
   The push towards more flexible control architectures via open standards and hardware, including OpenFlow.

### FORCES Protocol and the First Attempt at a Separate Control Plane

#### The FORCES Protocol (2003)
Developed by the Internet Engineering Task Force (IETF), the *Forwarding and Control Element Separation (FORCES)* protocol was one of the first attempts at creating a separate control channel for managing packet-switched networks. The protocol standardized the interaction between multiple control elements and forwarding elements, which are responsible for packet forwarding, metering, shaping, and traffic classification.

- **Key Features of FORCES:**
  - A separate control channel, the *FORCES Interface*, was established for managing forwarding elements.
  - Multiple control elements could interact with forwarding elements to dictate their behavior.

#### Challenges with FORCES
Despite its promise, the FORCES protocol faced challenges:
- **Hardware Standardization**: It required vendors to adopt a specific standard and deploy new hardware, which slowed down its widespread adoption.
- **Integration with Existing Networks**: The need for custom hardware made it less feasible for many existing networks, similar to earlier issues in active network projects.

### Hijacking Existing Protocols for Control

#### Routing Control Platform (RCP)
The *Routing Control Platform* took a different approach by using existing network protocols, particularly the *Border Gateway Protocol (BGP)*, as a control channel. This allowed network operators to manage routing decisions without the need to introduce new protocols.

- **How RCP Worked:**
  - An RCP computed routes centrally and used BGP to push these routing decisions into the routers’ forwarding tables.
  - Routers believed they were communicating with other routers, but in fact, the routing decisions were being controlled centrally by the RCP.

#### Benefits and Limitations of RCP
- **Ease of Deployment**: Since it leveraged existing BGP protocols, the RCP did not require new hardware or a full network redesign.
- **Control Constraints**: The system was limited by the capabilities of BGP and couldn’t extend control to a wider range of network behaviors beyond routing.

### Open Hardware and OpenFlow

#### The Rise of OpenFlow
The breakthrough came with *OpenFlow*, which took advantage of existing hardware but exposed the flow table interfaces of switches, allowing a separate controller to program these tables. OpenFlow’s approach eliminated the need for custom hardware while offering much more flexibility than previous solutions.

- **Key Concept of OpenFlow:**
  - A separate controller communicates with the switch’s flow table to install forwarding table entries that control how packets are handled.
  - It allowed vendors to open up their hardware to third-party software controllers, enabling a broader range of network configurations and innovations.

### Summary of Control Plane Evolution

- **Decoupling Control and Data Planes**: The separation of the control and data planes, initially exemplified by early systems like FORCES, was key to enabling more flexibility and faster innovation in network management.
- **Limitations of Existing Protocols**: While protocols like BGP helped facilitate centralized control, they were still bound by the constraints of what those protocols could support.
- **The Impact of Open Hardware**: OpenFlow’s success stemmed from the availability of open hardware interfaces that allowed for greater control flexibility without the need for proprietary hardware.

## The Intellectual History of Software-Defined Networking (SDN)

### Origins and Evolution  
Although SDN has gained momentum in recent years, its roots trace back over 20 years. The term *software-defined networking* was introduced in 2009, but many foundational ideas originate from earlier technologies, including phone networks. The progression of SDN can be categorized into three pivotal stages:  
1. **Active Networking**: Introduced programmable networks.  
2. **Control and Data Plane Separation**: Defined open interfaces between planes.  
3. **OpenFlow and Network Operating Systems**: Pioneered widespread adoption of programmable infrastructure.  

### Active Networking  
Active networking emerged during a time of increasing Internet use and diverse applications. It represented the first attempt to make networks programmable, driven by reduced computing costs and researcher ambitions.  

The core contributions of active networking were:  
- Programmable functions within the network.  
- Network virtualization.  
- A vision for unified middlebox orchestration, later realized through *network functions virtualization (NFV)*.  

However, myths surrounded this stage:  
- Many assumed end users would program packets themselves, though this scenario was rare.  
- Some believed active networking required packets to carry Java code. In reality, alternative models resembled modern SDN architectures.  

### Control and Data Plane Separation  
This stage marked a shift toward solving practical network management challenges, such as traffic engineering. Efforts like *ForCES* and the *Routing Control Platform* exemplified progress.  

**Key Contributions**:  
1. Logically centralized control through open interfaces to routers and switches.  
2. Distributed state management techniques for network controllers.  

**Addressing Misconceptions**:  
While some believed logically centralized control violated fate-sharing, this principle was already relaxed in traditional protocols like OSPF and BGP. Surprisingly, separating control and data planes enabled cleaner approaches to distributed state management.  

### The Rise of OpenFlow  
The breakthrough came with *OpenFlow*, which took advantage of existing hardware but exposed the flow table interfaces of switches, allowing a separate controller to program these tables. OpenFlow’s approach eliminated the need for custom hardware while offering much more flexibility than previous solutions.  

- **Key Concept of OpenFlow**:  
  - A separate controller communicates with the switch’s flow table to install forwarding table entries that control how packets are handled.  
  - It allowed vendors to open up their hardware to third-party software controllers, enabling a broader range of network configurations and innovations.  

Myths about OpenFlow included the belief that controllers must be physically centralized or handle the first packet of every flow. In reality, most deployments use distributed controllers, and OpenFlow supports varying rule granularity.  

### Lessons Learned  
The history of SDN highlights the delicate balance between *vision* and *pragmatism*. OpenFlow succeeded because it bridged ambitious programmability with practical hardware support. Moving forward, SDN concepts are expanding to programmable data planes and commodity servers, continuing to build on this balance.  

<details><summary><h3>Tutorial</h3></summary>

### Install VirtualBox 
Install VirtualBox at [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads) to create and manage virtual machines on your system.  

### Install Vagrant 
Install Vagrant at [https://developer.hashicorp.com/vagrant/install?product_intent=vagrant](https://developer.hashicorp.com/vagrant/install?product_intent=vagrant) to automate the provisioning and management of virtual machine environments.

### Clone a course project repository 
```bash
PS C:\Users\cynicdog> git clone https://github.com/noise-lab/Coursera-SDN.git && cd Coursera-SDN 
```

### Copy the course virtual machine image 
```bash
PS C:\Users\cynicdog\Coursera-SDN> vagrant up
```

### Connect to the image 
```bash
PS C:\Users\cynicdog\Coursera-SDN> vagrant ssh 
```

### Install mininet 
```
vagrant@coursera-sdn:~$ sudo apt-get mininet 
```

### Exit the virtual machine 
```
vagrant@coursera-sdn:~$
PS C:\Users\cynicdog\Coursera-SDN> vagrant halt 
```
 
</details>

<details><summary><h3>Quiz</h3></summary>

### Q. Which of the following constituted advantages to AT&T's elimination of in-band signaling from the phone network in the 1980s?

A. **Introduction of new services** ✅  
> **Correct.** Eliminating in-band signaling allowed AT&T to introduce new services like 800 number routing, which required separate, out-of-band signaling channels to be effective. This separation made it easier to innovate with new telephony services.

B. **Easier configuration and management**  
> **Incorrect.** While eliminating in-band signaling offered benefits in flexibility, the change itself did not directly simplify configuration or management. In fact, it introduced the need for more sophisticated signaling systems, such as SS7 (Signaling System 7), which required careful configuration.

C. **Reduction of expenditures** ✅  
> **Correct.** Removing in-band signaling allowed for more efficient use of the available bandwidth and infrastructure, potentially lowering costs over time. Additionally, by centralizing and automating signaling processes, operational costs were reduced.

D. **Improved security**  
> **Incorrect.** Eliminating in-band signaling didn't directly improve security. While moving signaling traffic to out-of-band systems might reduce some risks, security improvements were not a primary advantage.

---

### Q. What types of functions were enabled by active networks?

A. Code running on end hosts (e.g., machines sending and receiving packets) could modify packet contents.  
> Incorrect. Active networks enabled programmability, allowing end hosts to modify packet contents dynamically, but they primarily focused on network nodes like routers and switches for packet processing.

B. Code installed on nodes in the network (e.g., at routers and switches) could process packets. ✅  
> Correct. Active networks allowed network nodes like routers and switches to execute custom code, providing flexibility in packet processing.

C. Packets carrying code in the payload could be executed on intermediate nodes in the network (e.g., routers, switches). ✅  
> Correct. Active networks introduced the concept of executable code within packets, enabling intermediate nodes to execute the code and perform network functions.

D. A single node in the network could perform more than one function on a packet or stream of packets (e.g., firewalling, followed by load balancing). ✅  
> Correct. Active networks allowed nodes to perform multiple functions on packets, such as combining firewalling with load balancing.

E. All routers in the network needed to support active networks for active networks to be deployable.  
> Incorrect. Active networks could be implemented in a partial manner, and not all routers needed to support active network functionalities for the system to be deployable.

--- 

### Q. Which of the following is true about network virtualization?

A. Network virtualization allows multiple service providers to share the same underlying physical infrastructure. ✅  
> Correct. Network virtualization enables multiple tenants or service providers to operate independently while sharing the same physical network resources.

B. Network virtualization was invented in the late 2000s to support the migration of virtual machines in data centers.  
> Incorrect. Network virtualization existed before the late 2000s and was not specifically invented for virtual machine migration; it has broader applications, including supporting network slicing and multi-tenancy.

C. Virtual networks can be realized by dividing switch forwarding tables based on fields in the packet header (e.g., IP address and port). ✅  
> Correct. Network virtualization often uses fields in packet headers, such as IP addresses and ports, to isolate and manage virtual networks within shared physical infrastructure.

D. Network virtualization requires every router and switch in the network to run custom technology supporting virtualization.  
> Incorrect. While network virtualization may benefit from specific support in switches and routers, it does not mandate that every device in the network be customized.

E. Network virtualization requires the instantiation of virtual machines at each intermediate node (e.g., switch, router) in the network.  
> Incorrect. Network virtualization does not require virtual machines at intermediate nodes; it can be implemented using software-defined networking (SDN) or other techniques that do not rely on virtual machines.

--- 

### Q. Which of the following are true about various systems developed for central control of packet-switched networks?

A. The RCP could be deployed within a single ISP network, without coordination across multiple ISPs. ✅  
> Correct. The Routing Control Platform (RCP) was designed to operate within a single ISP network and did not require coordination across multiple ISPs.

B. The OpenFlow protocol requires vendors to expose the details of how they implement flow table maintenance in their switches.  
> Incorrect. OpenFlow abstracts the details of flow table maintenance from the vendors, allowing different switches to support OpenFlow without exposing proprietary implementations.

C. Ethane's initial goal was to support authentication of hosts in enterprise networks. ✅  
> Correct. Ethane was developed with the aim of providing a secure framework for host authentication in enterprise networks.

D. The FORCES protocol is deployed on most major routers and switches today.  
> Incorrect. The FORCES protocol is not widely deployed on major routers and switches today; it was still experimental and not broadly adopted in practice.

E. The Routing Control Platform requires changes to existing routers to support central control.  
> Incorrect. The Routing Control Platform (RCP) did not require significant changes to existing routers but instead worked within the existing infrastructure with some integration.

--- 

### Q. Which three artifacts and lessons that active networks affected the development of software-defined networks?

A. **centralized control**  
> **Incorrect.** Active networks were not primarily focused on centralized control. They emphasized programmability and flexibility at the network nodes, which is different from the centralized control architecture that SDN uses.

B. **programmable functions** ✅  
> **Correct.** Active networks introduced the concept of **programmable functions** at the network nodes (e.g., routers, switches), enabling the dynamic modification of packets and routing. This programmability influenced the development of SDN, where network functions are also made programmable.

C. **packet headers** ✅  
> **Correct.** Active networks allowed for more flexible processing of packet headers, influencing SDN's ability to manipulate packet headers dynamically for better control and management of network traffic.

D. **demultiplexing** ✅  
> **Correct.** Active networks introduced flexible packet processing, which led to **demultiplexing** techniques in SDN. This allows packets to be processed based on multiple criteria, enabling more efficient traffic management and routing in SDN.

E. **distributed state management**  
> **Incorrect.** While active networks dealt with node programmability, the concept of **distributed state management** is more closely associated with SDN, where centralized control is used to manage and distribute state information across the network. Active networks were not specifically focused on distributed state management.

</details>

</details>

<details><summary><h3>Module 2 - Control and Data Plane Separation</h3></summary>

## Hands-On with Mininet: Detailed Overview

### Setting Up and Testing Simple Topologies

Mininet allows you to emulate simple network setups to test connectivity. For example, setting up three hosts connected to a single switch involves:

- Launching Mininet using the `mn` command with specific options:
  - `--topo` to define the topology (`single,3` for one switch with three hosts).
  - `--test pingall` to test connectivity between all hosts.
    
    ```bash
    vagrant@coursera-sdn:~$ sudo mn --test pingall --topo single,3
    ```
    
- Mininet automatically:
  1. Creates the network.
  2. Adds a default controller and the switch.
  3. Links hosts to the switch and configures them.
  4. Runs a connectivity test (`pingall`).
  5. Stops the emulation.

This demonstrates how quickly you can validate network setups with Mininet’s built-in capabilities.

### Mininet Command-Line Options

Mininet provides versatile command-line options for defining networks:

- **`--topo`**:  
  Specifies the topology at startup, e.g., `single,3` for one switch and three hosts.  
- **`--switch`**:  
  Defines the switch type; defaults to Open vSwitch but allows custom switches.  
- **`--controller`**:  
  Sets the controller type. By default, Mininet uses a simple hub-like controller.

These options simplify the creation of custom topologies directly from the command line.

### Exploring Topology Types

Mininet supports diverse topologies to suit different use cases:

1. **Minimal Topology**:  
   - Two hosts and one switch.  
   - Useful for basic connectivity tests.

     ```bash
     vagrant@coursera-sdn:~$ sudo mn --topo minimal
     ```

2. **Linear Topology**:  
   - Four hosts and four switches in sequence.  
   - Links each host to its respective switch, with switches connected linearly.

     ```bash
     vagrant@coursera-sdn:~$ sudo mn --topo linear,4
     ```

3. **Tree Topology**:  
   - A hierarchical arrangement of switches and hosts.  
   - Configurable depth and fan-out.

     ```bash
     vagrant@coursera-sdn:~$ sudo mn --topo tree,depth=2,fanout=2
     ```

In all cases, Mininet handles the creation of nodes, links, and network emulation, ensuring consistency and reliability.

### Writing Custom Topologies in Python

Mininet's Python API enables the creation of detailed and flexible network setups. Python scripting allows you to parameterize and automate topology generation.

<details><summary><code>1_linear_topo.py</code></summary>
<br>
	
```python
#!/usr/bin/python
from mininet.net import Mininet

def run():
        net = Mininet()

        # Creating nodes in the network
        c0 = net.addController()
        h0 = net.addHost('h0')
        h1 = net.addHost('h1')
        s0 = net.addSwitch('s0')

        # Creating links between nodes in network (2-ways)
        net.addLink(h0, s0)
        net.addLink(h1, s0)

        # Configuration of IP addresses in interfaces
        h0.setIP('192.168.1.1', 24)
        h1.setIP('192.168.1.2', 24)

        net.start()
        net.pingAll()
        net.stop()

if __name__ == '__main__':
        run()
```

</details>

<details><summary><code>2_linear_topo_advanced.py</code></summary>
<br>

```python
#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):

	"Single Switch connected to `n` hosts"
	def __init__(self, n=2, **opts):

		# Initialize topology and default options
		Topo.__init__(self, **opts)
		switch = self.addSwitch('s1')

		# Register hosts 
		for h in range(n):
			host = self.addHost('h%s' % (h + 1))
			self.addLink(host, switch)

"Create and test a simple network"
def run():
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo)
	net.start()
	dumpNodeConnections(net.hosts)
	net.pingAll()

	# Run a command on a host `h1` 
	h1_ifconfig = net.get('h1').cmd('ifconfig')
	print(h1_ifconfig)

	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	run() 
```

</details>


### Advanced Customization

Mininet supports additional customization options:

1. **Interactive CLI**:  
   - Add `CLI(net)` to pause the script and enter Mininet's command line.
   - Explore node connections, run ping tests, or execute system commands (e.g., `ifconfig`).

2. **Custom Node Configuration**:  
   - Assign IP addresses or other properties using methods like `host.setIP()`.

3. **Link Properties**:  
   - Control bandwidth, delay, packet loss, and queue sizes using `addLink()` options.

4. **Dynamic Topologies**:  
   - Use loops or conditional logic in Python to generate complex networks.

### File System Behavior in Mininet

Mininet’s lightweight OS virtualization shares the file system across all virtual hosts:

- Files created or modified by one host are visible to others.
- File operations follow standard Python methods.

This can be leveraged for inter-host communication or logging within emulated networks.

### Diagnostic Tools

Mininet offers built-in tools to inspect and debug networks:

- **`dumpNodeConnections()`**:  
  Displays connections of all nodes in the network.  
- **System commands**:  
  Run commands like `ifconfig` on specific nodes for detailed information.  

Diagnostics are crucial for understanding and troubleshooting complex setups.

### Summary and Next Steps

This lesson covered:

- Basic and advanced topologies (minimal, linear, tree).
- Using Mininet’s CLI and Python scripting for setup and testing.  
- Customizing links, nodes, and controllers.  
- File system sharing and diagnostic tools.

Future topics will include:

- Advanced performance measurements.
- Configuring custom controllers and switches.
- Exploring network behavior under different configurations.

Mininet’s flexibility makes it a powerful tool for network simulation and experimentation.

## Control and Data Plane Separation  

### Overview  
Control and data plane separation decouples the logic that governs network behavior from the components that forward traffic. This approach brings both opportunities and challenges, particularly around network evolution, centralized control, and management.

### Control Plane vs. Data Plane  
- **Control Plane:**  
  - Manages forwarding behavior (e.g., routing protocols, firewall rules, load balancing).  
  - Acts as the "brain" of the network, making traffic flow decisions.  
- **Data Plane:**  
  - Forwards traffic according to control plane instructions (e.g., IP forwarding, switching).  
  - Can be implemented in hardware or software, such as in software routers.

### Why Separate the Planes?  
- **Independent Evolution:**  
  - The control plane can evolve without being restricted by hardware limitations, enabling network logic upgrades without needing to replace physical devices.  
- **Centralized Control:**  
  - Centralized software can manage the entire network, simplifying tasks like network management, troubleshooting, and debugging.

### Opportunities in Control and Data Plane Separation  
- **Data Centers:**  
  - Facilitates virtual machine migration across data centers, maintaining network consistency even when traffic patterns change.  
  - Example: Yahoo uses a central controller to program network switches, ensuring seamless migrations and dynamic path updates.  
- **Denial of Service (DoS) Protection:**  
  - Enables control over traffic flows, like inserting null routes into routers to mitigate attack traffic, as demonstrated by AT&T.

### Challenges  
- **Scalability:**  
  - A single control element may need to manage thousands of forwarding elements, creating potential performance bottlenecks.  
- **Reliability and Security:**  
  - If the controller fails or is compromised, the forwarding elements may continue operating, but the network’s correct behavior could be at risk.

## Benefits of Control and Data Plane Separation: Overview and Examples

### Introduction to the Module  
This module explores the **opportunities and challenges** brought by separating the control and data planes. The focus in this lesson is on how this concept benefits networks in **two key domains**:
1. **Wide-Area Networks (WANs)**: Enhanced routing services for maintenance, egress selection, and security.  
2. **Data Center Networks**: Improved cost efficiency and management flexibility.

### Example 1: Benefits in Wide-Area Networks  

#### **Improved Routing Services**  
Traditional interdomain routing protocols, like Border Gateway Protocol (BGP), have limited flexibility in policy configuration. For instance:
- Route selection follows a rigid, predefined process.
- Auxiliary data like route reputation or time-based metrics is hard to incorporate.

With separation, a centralized controller can directly manage the forwarding plane, enabling more nuanced routing decisions based on richer policies. Examples include:

1. **Planned Maintenance**  
   - Use a centralized controller, such as the Routing Control Platform (RCP), to reroute traffic away from an egress router under maintenance (e.g., switch from Egress 1 to Egress 2).
   - This approach is more direct compared to traditional networks, which require cumbersome manual updates to routing protocols like OSPF.

2. **Custom Egress Selection for Customers**  
   - RCP enables routing based on customer-specific policies.  
   - Example: Traffic from one customer can be routed to a specific data center, while traffic from another customer goes to a different one—something infeasible with destination prefix-based BGP.

3. **Enhanced Security**  
   - Anomaly detection systems can identify suspicious routes and prioritize secure, familiar ones.  
   - The controller ensures all routers in the autonomous system prefer safe routes, overcoming BGP's inability to incorporate such external reputation data.

### Example 2: Benefits in Data Center Networks  

#### **Simplified Management Through Flexible Addressing**  
Balancing **Layer 2 (L2)** and **Layer 3 (L3)** networking in large-scale data centers is challenging:  
- **L2**: Simpler setup but poor scalability (e.g., broadcast traffic limits).  
- **L3**: Better scaling but higher administrative overhead (e.g., manual configuration of routing protocols like OSPF).

With control-plane separation, a **fabric manager** or centralized controller introduces a novel approach to addressing in data centers. The key idea is to **reuse MAC addresses** but **reassign them** to reflect the hosts' positions in the network topology. This topology-aware addressing achieves the following:

1. **Use of Layer 2 (L2) Addressing**: Simplifies network setup by maintaining a flat addressing scheme.  
2. **Topology-Aware Pseudo-MAC Addresses (P-MACs)**: Hosts are assigned MAC addresses dependent on their location, enabling scalability and efficient routing.  
3. **Dynamic ARP Query Handling**: The fabric manager intercepts ARP requests, mapping traditional IP addresses to the new P-MACs seamlessly.  

This setup allows the network to combine the **administrative simplicity of L2 networks** with the **scaling advantages of L3 routing**, creating a balanced solution for managing large-scale data centers.

### Broader Opportunities  

Control and data plane separation introduces **dynamic and innovative solutions** for network challenges:  
- **Campus/Enterprise Networks**: Dynamic access control for users and devices.  
- **Research and Development**: Enabling experimentation with new network services (e.g., OpenFlow case studies).  

These use cases illustrate how this separation simplifies management, enhances scalability, and fosters innovation across network types.

## Key Challenges in Control and Data Plane Separation  

1. **Scalability**:
   - **RCP's Approach**:
     - **Eliminating Redundancy**: Stores a single copy of each route and uses pointers to represent duplicates.
     - **Accelerating Lookups**: Maintains indexes to identify routers affected by changes, reducing unnecessary recomputation.
     - **Selective Protocol Handling**: Focuses only on inter-domain routing to simplify operations.
   - **ONIX's Approach**:
     - **Partitioning**: Tracks only subsets of network state and uses consistency protocols across partitions.
     - **Aggregation**: Employs hierarchical controllers, with a top-level controller overseeing multiple sub-controllers.

2. **Reliability**:
   - **RCP**:
     - Uses replication with "hot spare" RCP servers that run in parallel and synchronize to maintain consistent routing decisions.
     - Ensures correct operations by using inputs and algorithms identically across replicas.
   - **ONIX**:
     - Handles failures through replication and distributed coordination protocols.
     - Leaves recovery from network failures to the applications themselves, recommending reliable communication methods like multi-path routing.

3. **Consistency**:
   - Ensures route assignments are consistent even during failures or partitions.
   - **RCP**:
     - Relies on internal gateway protocols (e.g., OSPF, IS-IS) to compute state only for reachable partitions, avoiding inconsistencies.
   - **ONIX**:
     - Uses distributed protocols to synchronize state across replicas, ensuring consistency across the network.

<details><summary><h3>Quiz</h3></summary>

### Q. Which of the following are examples of control plane operations?

A. Computing a shortest path routing tree ✅  
> **Correct.** The control plane is responsible for making decisions about the network's routing and forwarding, including computing paths such as the shortest path routing tree used by routing protocols.

B. Determining that a user's MAC address is authentic before allowing it to send traffic on the network ✅  
> **Correct.** This is a control plane operation that involves security and authentication mechanisms like port security or 802.1X, which control access to the network.

C. Load balancing traffic across two output ports based on the hash of each packet's source IP address  
> **Incorrect.** Load balancing is a data plane operation, as it involves forwarding packets based on real-time traffic conditions and is handled by network devices like switches and routers.

D. Rate-limiting traffic so that the overall sending rate does not exceed a certain throughput  
> **Incorrect.** Rate-limiting is a data plane operation, which controls the actual flow of traffic through the network, based on predefined limits or policies.

E. Determining the forwarding path that satisfies an access control policy ✅  
> **Correct.** The control plane is involved in determining the policies for forwarding traffic, such as applying security or access control lists (ACLs) that influence how packets are handled and forwarded in the network.

--- 

### Q. What are some of the reasons for separating the control and data planes?

A. Independent evolution of technologies for the data and control plane ✅  
> **Correct.** Separating the control and data planes allows each to evolve independently, enabling different technologies to be optimized for their specific roles. The control plane can focus on network decisions, while the data plane handles fast packet forwarding.

B. Ability to scale to much larger networks  
> **Incorrect.** While separating the control and data planes can contribute to more efficient scaling, it's not a primary reason for the separation itself. Other factors like network architecture and the use of distributed control also play a role in scalability.

C. Easier reasoning about network behavior ✅  
> **Correct.** With the control and data planes separated, it's easier to understand and manage network behavior. The control plane handles the logic and decision-making, while the data plane handles packet forwarding, simplifying the design and troubleshooting process.

D. No single point of failure or target of attack
> **Incorrect.** Separation of planes doesn't eliminate a single point of failure. In fact, control plane failures or vulnerabilities could still impact the entire network, although such risks can be mitigated with redundancy and security practices.

E. Vendor-independence (being able to separate the hardware that is running in the network from the logic that determines network behavior) ✅  
> **Correct.** This separation allows networks to adopt hardware from different vendors while keeping the control logic centralized and independent, leading to greater flexibility and reducing vendor lock-in.

---

### Q. What could be the operational steps behind AT&T's IRSCP (a commercial version of the Routing Control Platform) for detecting malicious traffic?

A. The end host changes its IP address so that it is no longer the target of the attack traffic  
> **Incorrect.** While changing the IP address can mitigate the effects of certain attacks, it doesn't directly involve the IRSCP, which focuses on traffic detection and routing changes rather than host-specific solutions.

B. A measurement system detects an attack, identifies the entry point of the attack, and instructs a controller to install a null route to drop traffic at the entry point where attack traffic is originating ✅  
> **Correct.** This describes a valid operational step of the IRSCP. The system detects an attack, locates the entry point, and then drops the malicious traffic at that point by installing a null route to prevent further damage.

C. A measurement system detects an attack, identifies the entry point of the attack, and instructs a controller to re-route traffic through a deep-packet inspection device  
> **Incorrect.** While deep-packet inspection can help detect malicious traffic, IRSCP typically focuses on mitigating the attack by dropping traffic through null routing, not rerouting it for inspection.

D. A victim end host sends an alert to an on-path firewall about the source and nature of an attack, at which point the firewall installs a null route to drop the traffic at the entry point where the attack is originating  
> **Incorrect.** This operational step involves interaction between a victim and a firewall, but IRSCP doesn't typically rely on victim-end host alerts. The system focuses on network-wide detection and mitigation.

E. The controller sees all traffic passing through the network, detects an attack, and installs a null route to drop traffic at the entry point where the attack traffic is originating 
> **Incorrect**. While the controller can detect traffic, it does not have visibility into all traffic passing through the network. The process typically involves measurement systems detecting attacks and the controller taking action based on that input, not by observing all traffic directly.

---

### Q. What are some example network management applications that become easier with control and data plane separation?

A. Improved logging capabilities  
> **Incorrect.** While logging is an important network function, control and data plane separation doesn't directly impact logging. This is more related to network monitoring and troubleshooting, which is independent of the plane separation.

B. Forecasting of network capacity 
> **Incorrect.** Control plane separation allows for better abstraction of network behavior, making it easier to forecast network capacity as traffic management can be more flexible and centralized.

C. Customer-controlled egress selection ✅  
> **Correct.** With control and data plane separation, customers can have more influence over routing decisions, including the selection of egress points, as control decisions can be centralized while the data plane handles traffic forwarding.

D. Planned maintenance of an edge router ✅  
> **Correct.** Separating the control and data planes enables easier management of network maintenance tasks, such as planned maintenance of edge routers. The control plane can adjust traffic flows without affecting the operation of the data plane directly.

E. Improved interdomain routing security ✅  
> **Correct.** Separation of control and data planes facilitates more effective management of interdomain routing, improving security through better routing protocols and centralized control that can enforce security policies across domains.

--- 

### Q. What are some of the motivations for using Layer-2 forwarding in a data center?

A. Better security properties  
> **Incorrect.** Layer-2 forwarding alone doesn't inherently provide better security properties. Security features such as access control lists (ACLs) or encryption are more relevant to improving security.

B. Better scaling properties  
> **Incorrect.** Layer-2 forwarding may not inherently provide better scalability, especially in larger networks where Layer-3 forwarding is often used for more efficient routing and scaling.

C. Better load balancing properties  
> **Incorrect.** Load balancing is typically a feature of Layer-3 routing protocols or network design techniques, not Layer-2 forwarding. 

D. Ability to use existing routing protocols to establish paths between hosts  
> **Incorrect.** Layer-2 forwarding doesn't use traditional Layer-3 routing protocols, as it operates below the IP layer and uses MAC addresses for traffic forwarding, not IP addresses.

E. Easier configuration/administration, since there is no need to number hosts or configure subnets ✅  
> **Correct.** Layer-2 forwarding simplifies network configuration by eliminating the need to assign IP addresses to hosts or configure subnets, making it easier to set up and manage a network at a basic level.

---

### Q. How does the separation of the control and data plane make networking in data centers easier?

A. A network controller can permit the renumbering of end hosts to have topology-dependent Layer 2 MAC addresses ✅  
> **Correct.** The separation allows for dynamic control of host addresses, including the ability to adjust MAC addresses according to the network topology without impacting the data plane, making management more flexible.

B. The separation allows fewer switches to be used in the data center topology, thus lowering costs  
> **Incorrect.** While the separation of the planes offers various benefits, it doesn't inherently reduce the number of switches in the data center. The number of switches is determined by the network's scale and design, not the plane separation.

C. All routes can be controlled and monitored from a central point of control ✅  
> **Correct.** With the control and data planes separated, all routing decisions can be centralized and managed from a single control point, providing better monitoring and management of network paths.

D. The control plane allows traffic to be forwarded using Layer 2 addresses, thus allowing automatic load balance across the topology  
> **Incorrect.** The control plane itself doesn't directly perform traffic forwarding or load balancing; it provides the instructions for the data plane to do so. Traffic forwarding based on Layer 2 addresses is typically handled by the data plane, not the control plane.

E. Virtual machines can be migrated within the network without renumbering entire portions of the network or re-assigning network services to different IP addresses ✅  
> **Correct.** The separation allows for virtual machine migrations to be handled more seamlessly, as the control plane can manage the necessary adjustments without the need for changes in network-wide configurations or IP address assignments.

---

### Q. What are some examples of problems that can arise from consistency problems in the control plane, where a network has multiple controller replicas?

A. Inability to respond to link failures**
> **Incorrect.** Controller replicas typically maintain synchronized state, so link failure responses are not directly impacted by consistency issues in the control plane.

B. Incorrect operation when one controller fails
> **Incorrect.** Controller replicas are designed to provide fault tolerance, so one controller's failure usually doesn't cause incorrect operation, as long as the remaining controllers are in sync and take over the responsibilities.

C. Incorrect security policies ✅  
> **Correct.** Consistency issues between controller replicas can result in mismatched security policies being applied across the network, potentially leading to vulnerabilities or inconsistent enforcement of network security rules.

D. A flood of traffic at the controller  
> **Incorrect.** This issue is more related to controller resource limits or misconfiguration, not necessarily a result of consistency problems across controller replicas.

E. Forwarding loops ✅  
> **Correct.** Inconsistent control plane data can lead to forwarding loops, where packets circulate endlessly due to conflicting or outdated forwarding information being propagated across the network.

--- 

### Q. What are some approaches to coping with inconsistency across controller replicas?

A. Running a consistency protocol across controller replicas. ✅  
> **Correct.** A consistency protocol ensures that all controller replicas have the same view of the network state, preventing issues caused by inconsistent data.

B. Keeping a "hot spare" replica that has a complete view of the network's state. ✅  
> **Correct.** A "hot spare" replica can take over if the active controller fails, ensuring there is no loss of network state and reducing the chance of inconsistency.

C. Only keeping a subset of the network state in memory at any time.  ✅  
> **Correct.** This allows for less potential for inconsistency and is the approach used by Onix.

D. Having multiple controllers install forwarding table entries on the same router and resolving the conflict on the router itself.  
> **Incorrect.** Allowing multiple controllers to modify forwarding table entries on the same router can introduce conflicts and complexity, which could worsen consistency problems instead of solving them.

E. Using different controllers for independent parts of the network. ✅  
> **Correct.** Segmenting the network into parts that are managed by different controllers reduces the scope of potential inconsistency, as each controller only handles a smaller, isolated portion of the network. 

---

### Q. What are some approaches to coping with scalability challenges associated with control and data plane separation?

A. Caching forwarding decisions in the data plane to reduce traffic at the controller. ✅  
> **Correct.** Caching forwarding decisions locally in the data plane reduces the load on the controller, minimizing traffic and improving scalability.

B. Eliminating redundant data structures. ✅  
> **Correct.** Eliminating redundancy in data structures can improve system efficiency, thereby reducing memory usage and improving scalability by optimizing how data is stored and processed.

C. Only performing control-plane operations for a limited set of network operations. ✅
> **Correct.** RCP, for example, only performs control-plane operations for BGP routing.

D. Running multiple controllers, and having each controller only manage a part of the network. ✅  
> **Correct.** Distributing control-plane responsibilities across multiple controllers allows each one to handle a portion of the network, enhancing scalability by reducing the load on a single controller.

E. Sending all traffic through the controller to minimize forwarding decisions that the routers and switches must make.
> **Incorrect.** Sending all traffic through the controller would actually increase the load and reduce scalability, as it would centralize traffic management and create bottlenecks.

---

### Q. Which property guarantees that each RCP replica continues to install correct forwarding state in the network data plane, even in the case of a partition in the data plane?

A. Running the network from a single high-level control plane guarantees that network partitions and loops never occur in the first place.
> **Incorrect.** While a centralized control plane may reduce the chances of network partitions, it does not guarantee that partitions or loops won’t happen, especially in large-scale networks.

B. The controller cannot see many of the routers in the network anyway, so there is no way for it to install incorrect routing state in the routers that it is not connected to.  
> **Incorrect.** This assumption doesn't solve the issue of network partitions. Even if the controller can't see certain routers, partitions can lead to inconsistent forwarding states in the network.

C. The controllers are partitioned from the network routers, and the routers will fall back to running a distributed routing protocol.  
> **Incorrect.** If the controller is partitioned, routers may not receive updates, and falling back to distributed routing protocols may not guarantee consistent state across the entire network.

D. Each controller has a complete view of the portion of the network that it is controlling, and therefore can guarantee consistent routing within that partition. ✅  
> **Correct.** Since each controller has a complete view of its controlled portion of the network, it can ensure that routing decisions remain consistent even in the case of a network partition.

</details>

## Routing Control Platform (RCP)

### Introduction  
The Routing Control Platform (RCP) separates control and data planes to enhance routing in autonomous systems (AS). It uses the Border Gateway Protocol (BGP) as a control channel to compute and manage forwarding decisions centrally. This approach simplifies configuration, improves convergence, and reduces routing loops.

### Problems with BGP  
> **BGP Issues**:  
- Converges slowly or fails to converge entirely.  
- Causes routing loops and misconfigurations.  
- Makes traffic engineering complex and network-wide policies hard to enforce.  

BGP's fundamental problem is its decentralized nature. Each router operates with partial information, relying on interactions with other routers. Additionally, BGP interacts unpredictably with Interior Gateway Protocols (IGPs), further complicating routing.  

### RCP Overview  
The RCP addresses BGP’s limitations by centralizing route computation:  
- Represents an AS as a single logical entity.  
- Computes routes for all routers in the AS using a complete view of the topology.  
- Eliminates the need for routers to calculate their own paths.  

In full deployment, RCPs in different ASes communicate to exchange routes, but benefits are achievable even in incremental phases.  

### Deployment Phases  

#### **Phase 1: Single AS Deployment**  
- A single AS deploys an RCP.  
- The RCP learns iBGP routes and IGP topology.  
- Routers follow centrally computed paths, enabling policies like pinning egress points during topology changes.

**Example Application**:  
Ensuring consistent egress selection during IGP link failures, preventing unintended traffic shifts.  

#### **Phase 2: AS-wide Policy**  
- The RCP extends to manage eBGP routes from neighboring ASes.  
- Aggregates or refines IP prefixes for efficient routing.  
- Resolves overlapping prefixes safely, determining which routers require specific routes.

**Example Application**:  
Efficient aggregation while avoiding misrouting caused by overly generic prefixes.  

#### **Phase 3: Full Inter-AS Deployment**  
- All ASes deploy RCPs, communicating via an inter-AS protocol (potentially replacing BGP).  
- Enables advanced routing applications and innovations in traffic engineering.

**Example Application**:  
Enhanced network management with flexible routing, replacing BGP for more robust and scalable inter-domain communication.  

### Key Advantages of RCP  
1. **Simplified Configuration**: Centralized policy management eliminates router-specific configurations.  
2. **Loop Freedom**: Complete AS-wide views prevent persistent forwarding loops.  
3. **Faster Convergence**: Routes converge quicker due to consistent decision-making.  
4. **New Applications**: Supports advanced traffic engineering and other innovations.

By centralizing control and enabling a complete view of AS routes, the RCP transforms routing from a fragmented process to a coherent, efficient system.  

## 4D Network Architecture  

### Introduction  
The 4D Network Architecture separates traditional router functions into distinct planes to simplify and centralize network management. By isolating decision-making from the data plane, it enables operators to manage networks more effectively and align operations with high-level objectives.  

### Key Goals of 4D Architecture  
> **Goals**:  
- Achieve network-wide objectives rather than focusing on individual routers.  
- Provide centralized visibility for coherent decision-making.  
- Enable direct control of the data plane, simplifying operations like forwarding and traffic management.  

Traditional distributed routing protocols like OSPF and BGP have limitations in achieving these goals. They rely on routers making independent decisions, leading to inefficiencies, misconfigurations, and slow convergence.  

### Components of the 4D Architecture  

#### **1. Data Plane**  
- Responsible for forwarding packets based on pre-installed tables.  
- Implements low-level operations like filtering and buffering.  

#### **2. Dissemination Plane**  
- Facilitates communication between the decision and data planes.  
- Disseminates routing information and forwarding rules.  

#### **3. Decision Plane**  
- Centralized system that computes network-wide paths and policies.  
- Optimizes traffic engineering, security policies, and failover mechanisms.  

#### **4. Discovery Plane**  
- Collects real-time information on network topology and traffic.  
- Feeds data to the decision plane for dynamic adjustments.  

### Example Applications  

#### **Traffic Engineering**  
The discovery plane collects network load information, and the decision plane computes optimized paths to balance traffic. The dissemination plane ensures routers update their forwarding tables accordingly.  

#### **Access Control**  
Operators define policies for reachability. The decision plane calculates these policies and updates Access Control Lists (ACLs) across routers. Because the decision plane sees both traffic engineering and access control it can perform decisions that optimize traffic load while still respecting reachability constraints.

### Advantages  
1. **Simplified Management**: Centralized control replaces distributed protocols, reducing operational complexity.  
2. **Faster Response**: Centralized intelligence adapts quickly to topology changes or failures.  
3. **Enhanced Policy Enforcement**: Consistent implementation of traffic engineering and security policies.  

### Impact on Networking  
The 4D Network Architecture laid the foundation for Software-Defined Networking (SDN). By demonstrating the benefits of separating control and data planes, it inspired innovations that now define modern network management.  

<details><summary><h3>Quiz</h3></summary>

### Q. What are some of the reasons that it is difficult to deploy improvements to BGP?

A. **BGP is implemented in hardware, so deploying changes to BGP requires changes on the timescale of hardware development cycles.**  
> **Incorrect.** While BGP's deployment can be influenced by hardware, this is not typically cited as a primary reason for difficulty in deploying improvements.

B. **Changes are necessarily incremental because of the large installed base of routers that already run BGP.** ✅  
> **Correct.** The widespread adoption of BGP means that changes must be made incrementally to avoid disrupting the existing network infrastructure.

C. **Deploying changes to BGP requires coordination across potentially tens of thousands of ASes in the Internet.** ✅  
> **Correct.** Since BGP is a core protocol used across many ASes, any change requires significant coordination across the entire Internet.

D. **Only a few vendors implement BGP, and deploying changes requires convincing those vendors to change the protocol.**  
> **Incorrect.** While a few vendors may be prominent, BGP is widely supported across many vendors, and changes are not necessarily dependent on a few vendors.

E. **Deploying changes requires coordination in standards bodies such as the IETF.** ✅  
> **Correct.** Changes to BGP often require formal approval and standardization through organizations like the IETF, making the process slow and complex. 

---

### Q. Which of the following are true about the RCP?

A. **In Phase 1 of RCP deployment, a single AS can benefit from deploying RCP even if no other ASes deploy RCP.** ✅  
> **Correct.** Phase 1 allows an AS to benefit from deploying RCP independently, even without other ASes adopting it.

B. **In an RCP deployment, routers no longer have to compute routes.** ✅  
> **Correct.** The RCP controller computes all the routes on behalf of the routers in the AS, so routers no longer need to make independent routing decisions.

C. **In Phase 1 of RCP deployment, the RCP controller for an AS sees all routes for all destinations that an AS learns from neighboring ASes.**  
> **Incorrect.** The RCP controller only communicates with the AS's border routers and sees only the best route chosen by each router, not all routes from neighboring ASes.

D. **In Phase 1 of RCP deployment, there is no need for ASes to use BGP to exchange routes.**  
> **Incorrect.** BGP is still used for route exchange between ASes in Phase 1 of RCP deployment.

E. **The RCP controller operates just like a route reflector would, selecting a single best route for each destination for all client routers.**  
> **Incorrect.** The RCP controller does not operate like a route reflector. It can select different best routes for different client routers depending on the network’s needs.

---

### Q. Which of the following are true about network management with BGP, in the absence of RCP?

A. **BGP's interaction with the underlying routing IGP routing protocol can result in persistent forwarding loops.** ✅  
> **Correct.** BGP can lead to forwarding loops, especially due to its interaction with IGPs, causing persistent routing issues.

B. **Implementing network-wide policy sometimes causes the routers themselves to have to carry state.** ✅  
> **Correct.** Network-wide policies, like traffic engineering or routing adjustments, can require routers to maintain additional state, which was discussed in the decomposed configuration state example.

C. **Each router operates and makes decisions based only on a local view of network state.** ✅  
> **Correct.** In BGP, each router makes its decisions based on its own view of the network, without considering the global state, which is one of the challenges RCP addresses.

D. **BGP routing has a single point of failure.**  
> **Incorrect.** While BGP routing can be affected by failures, it doesn't have a single point of failure because multiple ASes and routers participate in routing decisions.

E. **It is not possible to perform traffic engineering with conventional BGP.**  
> **Incorrect.** Traffic engineering can be achieved with conventional BGP through techniques like BGP attributes, but it may not be as flexible or efficient as some alternative methods.

---

### Q. Which of the following is true about the second phase of RCP deployment?

A. **The second phase of RCP deployment offers potential benefits such as reduced routing table size.** ✅  
> **Correct.** In the second phase, routing table size is reduced through route aggregation, as discussed in the lesson.

B. **In the second phase of RCP deployment, ASes do not need to use BGP to exchange routes with one another.**  
> **Incorrect.** BGP is still used to exchange routes, but the nature of the exchanges changes with the introduction of the RCP controller.

C. **In the second phase of deployment, the RCP controller sees all routes for every destination that neighboring ASes advertise.** ✅  
> **Correct.** The RCP controller establishes external BGP sessions with neighboring ASes, allowing it to see all advertised routes.

D. **The second phase of deployment requires fewer BGP sessions at the RCP controller than the first phase, thus improving scalability of the controller.**  
> **Incorrect.** The second phase actually requires more BGP sessions, as the RCP controller peers directly with neighboring ASes.

E. **The second phase of RCP deployment requires no coordination with neighboring ASes.**  
> **Incorrect.** Coordination with neighboring ASes is still necessary in the second phase, particularly for establishing BGP sessions.

---

### Q. In terms of the parlance of the 4D architecture, which protocol serves as the "dissemination plane" for the RCP?

A. **Spanning Tree Protocol**  
> **Incorrect.** Spanning Tree Protocol is a layer 2 protocol for preventing loops in Ethernet networks and is not related to the dissemination plane in this context.

B. **Internal BGP** ✅  
> **Correct.** Internal BGP (iBGP) is used within an Autonomous System (AS) to disseminate routing information between routers, making it the dissemination plane in the 4D architecture for RCP.

C. **External BGP**  
> **Incorrect.** While External BGP (eBGP) is responsible for inter-AS communication, iBGP handles the dissemination of routing information within an AS in the context of RCP.

D. **The Internal Gateway Protocol (IGP)**  
> **Incorrect.** IGPs like OSPF or EIGRP work within an AS, but they are not the dissemination plane for RCP.

E. **LLDP**  
> **Incorrect.** LLDP is a neighbor discovery protocol and does not handle dissemination of routing information in RCP.

---

### Q. What are some of the stated goals of simplifying the control plane in the 4D architecture?

A. **Simpler management systems** ✅  
> **Correct.** Simplifying the control plane can lead to more straightforward management systems by reducing the complexity of controlling and configuring network behavior.

B. **Inherent robustness of control plane**  
> **Incorrect.** While simplifying the control plane can improve overall functionality, inherent robustness is not explicitly listed as a goal in the 4D architecture.

C. **Simpler routers and switches** ✅  
> **Correct.** Simplification of the control plane enables the use of "whitebox" switches, which are simpler, less costly devices with fewer proprietary dependencies.

D. **Faster innovation** ✅  
> **Correct.** By removing the reliance on proprietary vendors and standards bodies like the IETF, the 4D architecture can foster faster innovation in networking.

E. **Improved security**  
> **Incorrect.** Security is not explicitly cited as a stated goal of simplifying the control plane in the 4D architecture.

---

### Q. What are some examples of how a separate decision plane can amortize system overhead?

A. **Maintaining a single table in memory of AS paths that are learned across all BGP sessions in the AS, and using references into that table for specific routers (and routing decisions), to save memory.** ✅  
> **Correct.** This optimization helps reduce memory usage by centralizing the AS path information and referencing it rather than duplicating it across multiple routers.

B. **If secure BGP were deployed, verifying the signatures on the AS paths of routes received from neighbors.** ✅  
> **Correct.** Since many AS paths will be common, the decision plane can verify signatures once, amortizing the computational cost over multiple routers.

C. **Keeping track of topology information.** ✅  
> **Correct.** With a separate decision plane, individual routers no longer need to maintain detailed topology information, as this is centralized.

D. **Performing route computation on behalf of all the routers in the AS.**  
> **Incorrect.** While the decision plane centralizes route computation, it does not inherently reduce the overhead of the computation itself.

E. **Performing inbound traffic engineering on a set of links in a coordinated fashion.**  
> **Incorrect.** This task is related to traffic management but does not directly relate to reducing system overhead.

---

### Q. What are some examples of network-wide objectives that could be achieved by the decision plane in the 4D architecture?

A. **Counting the volume of video streaming traffic across a peering link**  
> **Incorrect.** This is more related to monitoring and does not fall under the decision plane's responsibilities.

B. **Ensuring predictable behavior for planned maintenance events** ✅  
> **Correct.** The decision plane can coordinate traffic rerouting or other actions to ensure that network behavior remains predictable during maintenance.

C. **Balancing traffic load across a network** ✅  
> **Correct.** The decision plane can make centralized decisions to distribute traffic efficiently across the network, achieving load balancing.

D. **Ensuring that connectivity is not interrupted when a link or router fails** ✅  
> **Correct.** The decision plane can quickly adapt the routing to avoid disruptions, ensuring high availability.

E. **Provisioning a BGP peering session to a neighbor AS**  
> **Incorrect.** This task is typically handled by individual routers, not the decision plane.

---

### Q. Which plane is responsible for installing state into the data plane (e.g., FIB entries, ACLs)?

A. **Decision plane**  
> **Incorrect.** The decision plane is responsible for making decisions about network behavior but not for installing those decisions into the data plane.

B. **None of the above**  
> **Incorrect.** The correct answer is the dissemination plane, which installs state into the data plane.

C. **Discovery plane**  
> **Incorrect.** The discovery plane is responsible for discovering network topology and neighbors, not for installing state into the data plane.

D. **Data plane**  
> **Incorrect.** The data plane processes the traffic based on the state, but it does not install state itself.

E. **Dissemination plane** ✅  
> **Correct.** The dissemination plane is responsible for taking decisions made by the decision plane and installing the necessary state, such as FIB entries and ACLs, into the data plane.

---

### Q. Which plane is responsible for path selection and traffic engineering?

A. **Discovery plane**  
> **Incorrect.** The discovery plane is responsible for discovering network topology and neighbors, not for path selection or traffic engineering.

B. **Decision plane** ✅  
> **Correct.** The decision plane is responsible for making decisions about path selection and traffic engineering, based on network state and policies.

C. **None of the above**  
> **Incorrect.** The decision plane is the correct choice for path selection and traffic engineering.

D. **Dissemination plane**  
> **Incorrect.** The dissemination plane installs the state, like FIB entries, into the data plane, but it is not responsible for path selection or traffic engineering.

E. **Data plane**  
> **Incorrect.** The data plane processes traffic based on the decisions made by the decision plane, but it does not handle path selection or traffic engineering.

</details>

</details>

</details>
