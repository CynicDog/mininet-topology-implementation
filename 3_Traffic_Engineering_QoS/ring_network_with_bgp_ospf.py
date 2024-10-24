#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import Node
import os


# Custom LinuxRouter class
class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable IP forwarding
        self.cmd('sysctl -w net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class RingNetworkTopo(Topo):
    def build(self):
        # Create routers with their respective IPs
        r1 = self.addNode('r1', cls=LinuxRouter, ip="172.16.10.1/24")
        r2 = self.addNode('r2', cls=LinuxRouter, ip="172.16.10.2/24")
        r3 = self.addNode('r3', cls=LinuxRouter, ip="172.16.70.2/24")
        r4 = self.addNode('r4', cls=LinuxRouter, ip="172.16.90.2/24")

        # Link between r1 and r2 in the same network (172.16.10.0/24)
        self.addLink(r1, r2,
                     intfName1='r1-eth1', params1={'ip': '172.16.10.1/24'},
                     intfName2='r2-eth1', params2={'ip': '172.16.10.2/24'})

        # Link between r2 and r3 (172.16.10.0/24 to 172.16.70.0/24)
        self.addLink(r2, r3,
                     intfName1='r2-eth2', params1={'ip': '172.16.10.3/24'},
                     intfName2='r3-eth1', params2={'ip': '172.16.70.2/24'})

        # Link between r3 and r4 (172.16.70.0/24 to 172.16.90.0/24)
        self.addLink(r3, r4,
                     intfName1='r3-eth2', params1={'ip': '172.16.70.3/24'},
                     intfName2='r4-eth1', params2={'ip': '172.16.90.2/24'})

        # Link between r4 and r1 to complete the ring (172.16.90.0/24 to 172.16.10.0/24)
        self.addLink(r4, r1,
                     intfName1='r4-eth2', params1={'ip': '172.16.90.3/24'},
                     intfName2='r1-eth2', params2={'ip': '172.16.10.4/24'})

def run():
    setLogLevel('info')

    # Create and start the network
    topo = RingNetworkTopo()
    net = Mininet(topo=topo)
    net.start()

    # Clear PID files
    os.system("killall -9 zebra bgpd ospfd > /dev/null 2>&1")


    for router in ['r1', 'r2', 'r3', 'r4']:
        info(net.get(router).cmd("/usr/lib/quagga/zebra -f /etc/quagga/%s-zebra.conf -d -i /tmp/zebra-%s.pid > /home/mininet/logs/%s-zebra-stdout 2>&1" % (router, router, router)))
        info(net.get(router).cmd("/usr/lib/quagga/bgpd -f /etc/quagga/%s-bgpd.conf -d -i /tmp/bgpd-%s.pid > /home/mininet/logs/%s-bgpd-stdout 2>&1" % (router, router, router)))

    for router in ['r1', 'r2']:
        info(net.get(router).cmd("/usr/lib/quagga/ospfd -f /etc/quagga/%s-ospfd.conf -d -i /tmp/ospfd-%s.pid > /home/mininet/logs/%s-ospfd-stdout 2>&1" % (router, router, router)))

    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
