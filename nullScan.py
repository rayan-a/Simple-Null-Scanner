#!/usr/bin/env python

import signal
import sys
from scapy.all import *

ipAddress=raw_input("Target IP address: ")
try:
	while True:
		poAddress=input("Target port (Press CTL+C to exit): ")
		print"scanning port",poAddress , "on", ipAddress, "\n"


		ans, unas = sr(IP(dst=ipAddress)/TCP(dport=poAddress,flags=""), inter=0.5, retry=3, timeout=1, verbose=0)
		if (ans):
			print "port", poAddress, "closed\n"
		else:
			print "port", poAddress, "open\n"

except KeyboardInterrupt:
	print "\n Interrupted"