from mininet.util import ensureRoot, waitListening
from mininet.node import Host

import sys

ensureRoot()
timeout = 5

print("*** creating nodes ***")
h1 = Host('h1')

root = Host('root', inNamespace=False)

print("*** creating links ***")
h1.linkTo(root)

print(h1)

print("*** configuring nodes ***")
h1.setIP('10.0.0.1', 8)
root.setIP('10.0.0.2', 8)

print("*** creating banner file ***")
f = open('/tmp/{}.banner'.format(h1.name), 'w')
f.write('welcome to {} at {} \n'.format(h1.name, h1.IP()))
f.close()

print("*** running sshd ***")
cmd = '/usr/sbin/sshd -o UseDNS=no -u0 -o "Banner /tmp/{}.banner"'.format(h1.name)

# add arguments from the command line
if len(sys.argv) > 1:
    cmd += ' ' + ' '.join(sys.argv[1:])

h1.cmd(cmd)
listening = waitListening(server=h1, port=22, timeout=timeout)

if listening:
    # it uses the same user + password of the host
    print("*** you may now ssh into {} at {}".format(h1.name, h1.IP()))
else:
    print("*** Warning: after {} seconds, {} is not listening on port 22".format(timeout, h1.name))