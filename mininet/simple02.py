from mininet.net import Mininet
from mininet.net import CLI
from time import sleep

"""
based on presentation http://conferences.sigcomm.org/sigcomm/2014/doc/slides/mininet-intro.pdf
"""


def main():
    net = Mininet()
    # create hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # create switch
    s1 = net.addSwitch('S1')

    # create controller
    c1 = net.addController('c1')

    # create links
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.start()

    # start web server on h2
    print('starting web server...')
    h2.cmd('python -m SimpleHTTPServer 80 &')
    sleep(2)

    # use h1 as a web client
    print('accessing web server..')
    h1.cmd('curl', h2.IP())

    # CLI(net)
    print('kill web server..')
    h2.cmd('kill %python')

    print('finish.')
    net.stop()

if __name__ == '__main__':
    main()
