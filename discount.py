# -*- coding:utf-8 -*-

from sys import argv

script, total = argv

print "Total order amount is: $",total
dis = raw_input("How much \% discount to offer?:")
total = int(total) * (1 - (float(dis)/100.0))
print "total after discount: ", total