# Simple-Null-Scanner
This is a smiple TCP Null scanner.

# Usage
python nullscan.py

# Description
A null scan is a type of port scan where a crafted TCP packet is sent to a target. If the target responds with a packet that has a RST flag the port is closed, we can tell if the port is open if the target does not respond. 
The crafted packet must have a TCP sequence number of 0 and all TCP header flags set to 0 as well.
