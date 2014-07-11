#!/user/bin/env python

import os
import sys
from collections import Counter
from pprint import pprint

'''List IPs and how many times they occur in a set of EZProxy logs'''

dirname = sys.argv[1]

logs = os.listdir(dirname)

def get_ips():
    ip_list = []

    for f in logs:
        curr_log = os.path.join(dirname, f)
        lines = [line.strip() for line in open(curr_log)]

        for line in lines:
            ip_list.append(line.split('-')[0])

        return ip_list
    

def count_ips(ip_list):

    ip_counts = Counter(ip_list)
    pprint(ip_counts)




count_ips(get_ips())