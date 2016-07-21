from mininet.topo import Topo

class MyTopo(Topo):
    """
    Simple topology example
    """
    def __init__(self):
        "create custom topo"
        # initialize topology
        Topo.__init__(self)

        # add hosts and switches
        left_host = self.addHost('h1')
        right_host = self.addHost('h2')
        left_switch = self.addSwitch('s1')

        # add links
        self.addLink(left_host, left_switch)
        self.addLink(right_host, left_switch)

topos = {
    'mytopo': (lambda : MyTopo() )
}