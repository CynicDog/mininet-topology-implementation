from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI

class SpanningTreeTopo(Topo):
    def build(self):
        # Create four switches
        s1 = self.addSwitch('s1', cls=OVSSwitch)
        s2 = self.addSwitch('s2', cls=OVSSwitch)
        s3 = self.addSwitch('s3', cls=OVSSwitch)
        s4 = self.addSwitch('s4', cls=OVSSwitch)

        # Connect switches according to the specified scenario
        self.addLink(s3, s1)
        self.addLink(s3, s4)
        self.addLink(s1, s4)
        self.addLink(s1, s2)
        self.addLink(s2, s4)

def run():
    topo = SpanningTreeTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, waitConnected=True)

    # Start the network
    net.start()

    # Set MAC addresses for each switch
    mac_addresses = {
        's1': '52:54:00:0f:ad:ab',
        's2': '52:54:00:13:cf:9a',
        's3': '52:54:00:16:5d:53',
        's4': '52:54:00:1d:d2:3a'
    }

    # Set MAC addresses and enable STP on each switch
    for switch in net.switches:
        mac_addr = mac_addresses[switch.name]
        switch.cmd('ovs-vsctl set Bridge {} other-config:hwaddr={} stp_enable=true'.format(switch, mac_addr))

    # Configure switch s3 as the root bridge
    net.get('s3').cmd('ovs-vsctl set Bridge s3 other-config:stp-priority=4096')

    # Ensure other switches have higher priority
    for switch in ['s1', 's2', 's4']:
        net.get(switch).cmd('ovs-vsctl set Bridge {} other-config:stp-priority=32768'.format(switch))

    # Run CLI for testing
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    run()
