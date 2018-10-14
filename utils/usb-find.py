#!/usr/bin/python

#==================
# Find USB devices
#==================

import subprocess, re

def main():
    ports_found = probe()
    print(ports_found)

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
                    ports[installed_devices[serial_num]] = port
            except:
                pass

    return ports

if __name__ == "__main__":
    main()
