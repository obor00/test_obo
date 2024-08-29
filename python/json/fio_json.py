#!/usr/bin/env python3

import re
import sys
import subprocess
import json
from typing import List, Dict
import yaml

json_file = "iops_read.json"

with open (json_file, "r")  as fp:
    file = json.load( fp)

s = json.dumps( file, indent = 4 )

#print(s)
res = yaml.safe_load( s )
#print( res)
print( res['fio version'] )
print( res['jobs'] [0] ['jobname'] )
print( 'read IOPS  = ' + str(res['jobs'] [0] ['read'] ['iops']))
print( 'write IOPS = ' + str(res['jobs'] [0] ['write'] ['iops']))
print( 'read bw    = ' + str(res['jobs'] [0] ['read'] ['bw']))
print( 'write bw   = ' + str(res['jobs'] [0] ['write'] ['bw']))


#
#def get_nvme_emulation_devices() -> List[Dict]:
#    devlist = json.loads(
#        subprocess.check_output(["sudo", "nvme", "list", "--output=json"]).decode("utf-8")
#    )
#    devices = [dev for dev in devlist["Devices"] if "NVMe Emulation" in dev["ModelNumber"]]
#    return devices
#
#def check_nvme_emulation_devices(devices: Dict, count: int = 4):
#    for serial_prefix in range(0, count):
#        found = False
#        for dev in devices:
#            if re.match(r"^/dev/nvme.*n1$", dev["DevicePath"]):
#                if re.match(fr"^{serial_prefix}.*$", dev["SerialNumber"]):
#                    found = True
#                    break
#        assert found, f"Virtual device {serial_prefix} not found in devices\n{devices}"
#
#
#def run_fio(device: str) -> Dict:
#    output = subprocess.check_output([
#        "sudo",
#        "fio",
#        f"--filename={device}",
#        "--direct=0",
#        "--rw=randrw",
#        "--rwmixread=50",
#        "--invalidate=1",
#        "--bs=4k",
#        "--ioengine=libaio",
#        "--iodepth=32",
#        "--runtime=20",
#        "--numjobs=4",
#        "--time_based",
#        "--group_reporting",
#        "--norandommap",
#        "--name=test_read_write",
#        "--cpumask=0xffff",
#        "--output-format=json",
#    ]).decode("utf-8")
#
#    return json.loads(output)
#
#
#def performance_is_acceptable(fio_output: Dict, device_name: str):
#    assert fio_output["read"]["iops"] >= 100, f"read iops is bad for {device_name}"
#    assert fio_output["read"]["bw"] >= 200, f"read bandwidth is bad for {device_name}"
#    assert fio_output["write"]["iops"] >= 100, f"write iops is bad for {device_name}"
#    assert fio_output["write"]["bw"] >= 200, f"write bandwidth is bad for {device_name}"

def main():
    parser = argparse.ArgumentParser()

    #parser.add_argument('command', type=str, choices=['discover', 'connect', 'disconnect'])
    parser.add_argument('-f', '--fio_json', type=str, help='fio result json file', required=True)

    # Arguments parsing
    args = parser.parse_args()

    # Arguments handling
    res = discover_nqns( args.target_ip )

    print( ' '.join(res) )

if __name__ == '__main__':
    main()

