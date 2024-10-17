#!/usr/bin/env python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Host, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
import os

class VLANHost(Host):
    def config(self, vlan=100, **params):

        super(VLANHost, self).config(**params)

        intf = self.defaultIntf()

        # remove IP address from the default interface
        self.cmd('ifconfig %s inet 0' % intf)

        # add a VLAN interface to the host's interface with the specified VLAN id
        self.cmd('vconfig add %s %d' % (intf, vlan))

        # assign the specified IP address to the new VLAN interface.
        self.cmd('ifconfig %s.%d inet %s' % (intf, vlan, params['ip']))

        # Update the interface name to the VLAN version and map it in the host's interface list
        newName = '%s.%d' % (intf, vlan)
        intf.name = newName
        self.nameToIntf[newName] = intf

class SingleSwitchVlanTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')

        # Create hosts and connect them to the switch with VLANs
        host1 = self.addHost('h1', cls=VLANHost, vlan=10, ip='10.0.0.1/24')
        host2 = self.addHost('h2', cls=VLANHost, vlan=20, ip='10.0.1.1/24')
        host3 = self.addHost('h3', cls=VLANHost, vlan=30, ip='10.0.2.1/24')

        # Add host4 in the same VLAN as host1
        host4 = self.addHost('h4', cls=VLANHost, vlan=10, ip='10.0.0.2/24')

        self.addLink(host1, switch)
        self.addLink(host2, switch)
        self.addLink(host3, switch)
        self.addLink(host4, switch)

def run():
    setLogLevel('info')

    # Create and start the network
    topo = SingleSwitchVlanTopo()
    net = Mininet(topo=topo, switch=OVSSwitch)
    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
