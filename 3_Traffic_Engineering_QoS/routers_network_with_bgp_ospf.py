from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import Node


# Custom LinuxRouter class
class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable IP forwarding
        self.cmd('sysctl -w net.ipv4.ip_forward=1')

    def initiateBGP(self):
        self.cmd('')  # Placeholder for BGP initiation

    def initiateOSPF(self):
        # Start OSPF
        self.cmd('')
        self.cmd('')

    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class OSPFNetworkTopo(Topo):
    def build(self):
        # Create routers with their respective IPs
        r1 = self.addNode('r1', cls=LinuxRouter, ip="172.16.10.1/24")
        r2 = self.addNode('r2', cls=LinuxRouter, ip="172.16.10.2/24")
        r3 = self.addNode('r3', cls=LinuxRouter, ip="172.16.20.2/24")
        r4 = self.addNode('r4', cls=LinuxRouter, ip="172.16.20.4/24")

        # Link between r1 and r2 in the same network
        self.addLink(r1, r2,
                     intfName1='r1-eth1', params1={'ip': '172.16.10.1/24'},
                     intfName2='r2-eth1', params2={'ip': '172.16.10.2/24'})

        # Link between r1 and r3 over different networks
        self.addLink(r1, r3,
                     intfName1='r1-eth2', params1={'ip': '172.16.20.1/24'},
                     intfName2='r3-eth1', params2={'ip': '172.16.20.2/24'})

        # Link between r3 and r4 in the same network
        self.addLink(r3, r4,
                     intfName1='r3-eth2', params1={'ip': '172.16.20.3/24'},
                     intfName2='r4-eth1', params2={'ip': '172.16.20.4/24'})


def run():
    setLogLevel('info')

    # Create and start the network
    topo = OSPFNetworkTopo()
    net = Mininet(topo=topo)
    net.start()

    # Retrieve routers from the Mininet network
    routers = ['r1', 'r2', 'r3', 'r4']

    # Initiate OSPF on all routers
    for router in routers:
        router.initiateOSPF()

    CLI(net)
    net.stop()


if __name__ == '__main__':
    run()
