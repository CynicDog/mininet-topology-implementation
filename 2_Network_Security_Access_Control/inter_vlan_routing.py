#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import Host, Node

# Custom LinuxRouter class
class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)

        # Enable forwarding on the router
        self.cmd('sysctl net.ipv4.ip_forward=1')

        # Configure router sub-interfaces for inter-VLAN routing
        self.cmd('ifconfig %s 0' % self.defaultIntf())  # Resetting the base interface
        
        # Establish VLAN memberships 
        self.cmd('vconfig add %s 10' % self.defaultIntf())  # VLAN 10
        self.cmd('vconfig add %s 20' % self.defaultIntf())  # VLAN 20
        self.cmd('vconfig add %s 30' % self.defaultIntf())  # VLAN 30
        
        self.cmd('ifconfig %s.10 up' % self.defaultIntf())
        self.cmd('ifconfig %s.20 up' % self.defaultIntf())
        self.cmd('ifconfig %s.30 up' % self.defaultIntf())
        
        self.cmd('ifconfig %s.10 172.16.1.1 netmask 255.255.255.192' % self.defaultIntf())
        self.cmd('ifconfig %s.20 172.16.1.65 netmask 255.255.255.192' % self.defaultIntf())
        self.cmd('ifconfig %s.30 172.16.1.129 netmask 255.255.255.192' % self.defaultIntf())

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

# Custom VLANHost class
class VLANHost(Host):
    def config(self, vlan=100, **params):
        super(VLANHost, self).config(**params)

        intf = self.defaultIntf()

        # Remove IP address from the default interface
        self.cmd('ifconfig %s inet 0' % intf)

        # Add a VLAN interface to the host's interface with the specified VLAN id
        self.cmd('vconfig add %s %d' % (intf, vlan))

        # Assign the specified IP address to the new VLAN interface
        self.cmd('ifconfig %s.%d inet %s' % (intf, vlan, params['ip']))

        # Update the interface name to the VLAN version and map it in the host's interface list
        newName = '%s.%d' % (intf, vlan)
        intf.name = newName
        self.nameToIntf[newName] = intf

# Custom topology class
class MultiSwitchVlanTopo(Topo):
    def build(self):
        # Create switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')

        # Create hosts and connect them to the switches with VLANs
        # Hosts connected to switch1
        self.addHost('h1', cls=VLANHost, vlan=10, ip='172.16.1.2/26')  
        self.addHost('h2', cls=VLANHost, vlan=20, ip='172.16.1.66/26') 
        self.addHost('h3', cls=VLANHost, vlan=30, ip='172.16.1.130/26') 
        # Hosts connected to switch2
        self.addHost('h4', cls=VLANHost, vlan=10, ip='172.16.1.3/26') 
        self.addHost('h5', cls=VLANHost, vlan=20, ip='172.16.1.67/26') 
        self.addHost('h6', cls=VLANHost, vlan=30, ip='172.16.1.131/26') 

        # Connect hosts to switches
        for i in range(1, 4):
            self.addLink('h{}'.format(i), switch1)
        for i in range(4, 7):
            self.addLink('h{}'.format(i), switch2)

        # Connect switches
        self.addLink(switch1, switch2)

        # Connect s2 to router r1
        router = self.addNode('r1', cls=LinuxRouter)
        self.addLink(switch2, router)

def run():
    setLogLevel('info')
    topo = MultiSwitchVlanTopo()
    net = Mininet(topo=topo, waitConnected=True)

    # Start the network
    net.start()

    # Set default gateways for hosts
    net.get('h1').cmd('ip route add default via 172.16.1.1')
    net.get('h2').cmd('ip route add default via 172.16.1.65')
    net.get('h3').cmd('ip route add default via 172.16.1.129')
    net.get('h4').cmd('ip route add default via 172.16.1.1')
    net.get('h5').cmd('ip route add default via 172.16.1.65')
    net.get('h6').cmd('ip route add default via 172.16.1.129')

    # Explicitly set the trunk ports for VLANs on the trunk link between switches
    switch1 = net.get('s1')
    switch2 = net.get('s2')

    # Get the interfaces connected between s1 and s2
    intf1 = switch1.intf('s1-eth4')
    intf2 = switch2.intf('s2-eth4')

    # Set trunk mode and allow VLANs 10, 20, and 30
    switch1.cmd('ovs-vsctl set port {} vlan_mode=trunk trunk=10,20,30'.format(intf1))
    switch2.cmd('ovs-vsctl set port {} vlan_mode=trunk trunk=10,20,30'.format(intf2))

    # Start CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    run()
