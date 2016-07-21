## Introduction
Controlling Mininet using OpenDaylight.

## Steps

1. It is assumed that OpenDaylight and Mininet have already installed on the same machine.

2. Run OpenDaylight:
```
cd distribution/opendaylight-karaf/target/assembly/
./bin/karaf
```

3. Access DLUX UI in the following address, login using `admin` with password `admin`:
 http://localhost:8181/index.html

4. Run Mininet:
`sudo mn --controller=remote,ip=127.0.0.1 --topo single,3`

http://www.brianlinkletter.com/using-the-opendaylight-sdn-controller-with-the-mininet-network-emulator/