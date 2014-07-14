#!/user/bin/env python

import os
import sys
import re
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

            garbage = re.search(r'\/img\/|\/images\/|\/style\/|\/script\/|\/foresee\/\g', line) #not 100% exhaustive but this should remove lines that GET server resources like scripts, images and stylesheets

            if garbage:
                #print "I'm a garbage line."
                pass
            else:
                ip_list.append(line.split('-')[0])

    return ip_list
    

def count_ips(ip_list):

    ip_counts = Counter(ip_list)
    
    for k in ip_counts:
        print k, ip_counts[k]



if __name__ == "__main__":
    count_ips(get_ips())