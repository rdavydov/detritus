#! /usr/bin/env python

import sys
from scapy.all import *

pkt=RadioTap()/Dot11()/Raw()
pkt[Raw].load='I love to send a lot of trash'
sendpfast(pkt, iface="wlan0mon", loop=2000, file_cache="true")
