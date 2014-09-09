#!/usr/bin/env python

import os
import sys
import re
import math
import operator
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

    ip_counts_sorted = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    
    total_req = sum(ip_counts.values())

    print '%s total requests over the last year' % (total_req)
    print 'ip' + '\t' + 'requests' + '\t' + 'percentage'
    for k, v in ip_counts_sorted:
        raw_perc = float(v)/total_req*100
        perc = round(raw_perc, 2)

        print k + '\t' + str(v) + '\t' + str(perc)+'%'



if __name__ == "__main__":
    count_ips(get_ips())
