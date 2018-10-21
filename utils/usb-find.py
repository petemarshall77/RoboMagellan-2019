#!/usr/bin/python
from __future__ import print_function

#==================
# Find USB devices
#==================

import subprocess, re

def main():
    ports_found = probe()
    if len(ports_found) > 0:
        for port in ports_found:
            print(port, ports_found[port])
    else:
        print("No devices found")


def probe():
    ports = {}
    port_families = ['/dev/ttyACM', '/dev/ttyUSB']
    for port_family in port_families:
        for index in range(10):
            port = '%s%s' % (port_family, index)
            command = 'udevadm info -a -n %s' % port
            try:
                out = subprocess.check_output(command.split(),
                                            stderr=subprocess.STDOUT)

                regex = re.compile("{serial}==\"([\w\.:]+)\"")
                match = regex.search(out)
                if match:
                    serial_num = match.group(1)
                    ports[port] = serial_num
            except Exception as e:
                pass

    return ports

if __name__ == "__main__":
    main()
