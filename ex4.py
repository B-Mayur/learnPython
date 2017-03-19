# -*- coding: utf-8 -*-

# Declare a variable containing total number of cars.
cars = 100
# A variable holding total numbers of seats available per car.
spaceInCar = 4.0
# Variable contining total number of drivers available.
drivers = 30
# Variable containing total number of passengers.
passengers = 90
# Number of non-Driven cars
carsNotDriven = cars - drivers
# Available cars w/ drivers.
carsDriven = drivers
# Carpool Capacity.
carpoolCapacity = carsDriven * spaceInCar
# Average passengers per car.
averagePassengersPerCar = passengers / carsDriven

# Print on console, number of cars available.
print "There are", cars, "cars available."
# Print on console, number of drivers available.
print "There are only", drivers, "drivers available."
# Print on console, empty cars OR Cars not driven.
print "There will be", carsNotDriven, "empty cars today."
# PRint on console, number of passengers we can transport.
print "We can transpor", carpoolCapacity, "people today."
# Print on console, the number of passengers available today.
print "We have", passengers, "to capool today."
# Print on console, how many passenger we need to put in a car.
print "We need to put about", averagePassengersPerCar, "passengers in each car."