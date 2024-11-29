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

<details><summary><h2>Below are my key takeaways from the course.</h2></summary>

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

<details><summary><h3>Module 2: Control and Data Plane Separation</h3></summary>

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

</details>

</details>
