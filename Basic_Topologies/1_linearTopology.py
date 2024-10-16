from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

class LinearTopo(Topo):
    def build(self, n=3):
        switches = []
        for i in range(n):
            switch = self.addSwitch('s{}'.format(i+1))
            host = self.addHost('h{}'.format(i+1))
            self.addLink(host, switch)
            if i > 0:
                self.addLink(switches[-1], switch)
            switches.append(switch)

def run():
    topo = LinearTopo(n=3)  
    net = Mininet(topo=topo)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
