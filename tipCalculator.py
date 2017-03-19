# A simple program to calculate tip.

# Total meal amount
amt = 35	# $35 total meal amount

# Tip percentage
tip = 5		# 5% of total.

# Tax 
tax = 14.5 	# 14.5 percent service charge.

#Find grand total.
total = amt * (1 + (tax/100.0))		# This is tax calculation formula.

# Calculate tip on Grand total.
tipOfferd = total * (tip/100.0)		# make tip calculation floating point
									# to retain precision.

# Print grand total on screen
print "Grand Total: $", total

# Print offered tip amount on screen.
print "Tip offered: $", tipOfferd

