from mininet.cli import CLI
from mininet.log import setLogLevel, info

def topoTP():
    
    net = Mininet( controller=Controller )

    info("*** Adding Controller\n")
    net.addController( 'c0' )

    info("*** Adding Hosts\n")
    emisorFTP = net.addHost('h1' """, ip='172.16.5.2'""")
    receptorFTP = net.addHost('h2' """, ip='172.16.4.2'""")
    emisorVideo = net.addHost('h3' """, ip='172.16.3.2'""")
    receptorVideo = net.addHost('h4' """, ip='172.16.2.2'""")
    routerA = net.addSwitch('s0')
    routerB = net.addSwitch('s1')

    info("*** Adding Links\n")
    net.addLink(emisorFTP, routerA)
    net.addLink(emisorVideo, routerA)
    net.addLink(routerA, routerB)
    net.addLink(routerB, receptorFTP)
    net.addLink(routerB, receptorVideo)

    info("*** Starting network\n")
    net.start()

    info("*** Starting CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topoTP()
    
