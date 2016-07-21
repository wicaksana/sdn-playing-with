#!/usr/bin/env bash

cd /home/arif/Github/SDNHub_Opendaylight_Tutorial/distribution/opendaylight-karaf/target/assembly
./bin/karaf &

sudo mn --controller=remote,ip=127.0.0.1 --topo linear,3 --mac --switch ovs,protocols=OpenFlow13