#!/home/mayur/anaconda2/bin
# -*- coding: utf-8 -*-

# file: ex6.py

x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who knwos %s and those who %s" % (binary, doNot)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"

print jokeEvaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e