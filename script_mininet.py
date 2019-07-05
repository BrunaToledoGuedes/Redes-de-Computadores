#!/usr/bin/python
#Exemplo de program python gerado à partir da aplicação RedeDB#Este program gera uma rede virtual mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController

def simpleTest():

    net = Mininet()
    c1 = net.addController( 'c1', ip = '127.0.0.1', port=6653 )
    s1 = net.addSwitch( 's1' )
	
    Host1 = net.addHost('Host1', ip = '10.0.0.1', mascara = '255.255.255.0', gateway = '10.140.5.0')

    linkHost1 = net.addLink('Host1', s1, bw=10, delay='10ms', loss=0)

    Host2 = net.addHost('Host2', ip = '10.0.0.2', mascara = '255.255.255.0', gateway = '10.140.5.0')

    linkHost2 = net.addLink('Host2', s1, bw=10, delay='10ms', loss=0)

    Host3 = net.addHost('Host3', ip = '10.0.0.3', mascara = '255.255.255.0', gateway = '10.140.5.0')

    linkHost3 = net.addLink('Host3', s1, bw=10, delay='10ms', loss=0)

    Host4 = net.addHost('Host4', ip = '10.0.0.4', mascara = '255.255.255.0', gateway = '10.140.5.0')

    linkHost4 = net.addLink('Host4', s1, bw=10, delay='10ms', loss=0)

    Host5 = net.addHost('Host5', ip = '10.0.0.5', mascara = '255.255.255.0', gateway = '10.140.5.0')

    linkHost5 = net.addLink('Host5', s1, bw=10, delay='10ms', loss=0)

    link1 = net.addLink('Host1', 'Host2', bw=6, delay='15ms', loss=8)

    link2 = net.addLink('Host2', 'Host3', bw=7, delay='15ms', loss=8)

    link3 = net.addLink('Host1', 'Host3', bw=8, delay='10ms', loss=5)

    link4 = net.addLink('Host1', 'Host4', bw=5, delay='5ms', loss=10)

    link10 = net.addLink('Host1', 'Host5', bw=5, delay='5ms', loss=6)

    net.build()
	
    c1.start()  
    s1.start([c1])
    CLI(net)

if __name__ == '__main__':

    simpleTest()