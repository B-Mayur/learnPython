# -*- coding: utf-8 -*-

from sys import argv

total, tip = argv[1], argv[2]

print "Total bill amount: $", total
t = int(total) * (int(tip)/100.0)

print "Tip offered: $", t