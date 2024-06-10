# pypinger.py
# This script pings a list of hosts and returns the result
# Usage: python pypinger.py <host1> <host2> <host3> ...
# Example: python pypinger.py google.com yahoo.com
# Note: This script uses ping3 library to ping the hosts
# Pre-req: 
# pip install ping3

import sys
from ping3 import ping, verbose_ping
import os

if os.path.exists('/tmp/pypinger.log'):
    os.remove('/tmp/pypinger.log')
    

def ping_hosts(hosts):
    for host in hosts:
        try:
            delay = ping(host, unit='ms', size=1, timeout=8)
            if delay is None or delay is False:  # retry mechanism to handle packet loss
                delay = ping(host, unit='ms', size=1, timeout=8)
            if delay is None or delay is False:
                # print(f'ERR: {host} is not reachable')
                print(f'❌: {host}')
                return
            else:
                with open('/tmp/pypinger.log', 'a') as f:
                    f.write(f'OK: {host} is reachable with delay {int(delay)} ms\n')
                    f.close()
                # print(f'OK: {host} is reachable with delay {int(delay)} ms')
        except Exception as e:
            # print(f'ERR: {host} caused an exception: {e}')
            print(f'❌: {host}')
            return
    # print('OK: All hosts are reachable')
    print('✅')

if __name__ == "__main__":
    ping_hosts(sys.argv[1:])