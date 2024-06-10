# pypinger.py
# This script pings a list of hosts and returns the result
# Usage: python pypinger.py <host1> <host2> <host3> ...
# Example: python pypinger.py google.com yahoo.com
# Note: This script uses ping3 library to ping the hosts
# Pre-req: 
# pip install ping3

import sys
from ping3 import ping, verbose_ping

def ping_hosts(hosts):
    for host in hosts:
        try:
            delay = ping(host, unit='ms')
            if delay is None or delay is False:
                print(f'ERR: {host} is not reachable')
                return
            else:
                print(f'OK: {host} is reachable with delay {int(delay)} ms')
        except Exception as e:
            print(f'ERR: {host} caused an exception: {e}')
            return
    print('OK: All hosts are reachable')

if __name__ == "__main__":
    ping_hosts(sys.argv[1:])