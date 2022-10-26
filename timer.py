#!/usr/bin/python
#import time ###UNCOMMENT THIS###
#if you want to import all time package
#calling time functions will look like time.strftime("%X", start_time), time.localtime(), time.mktime(stop_time)

#import specific function only from time package, simpler function call
from time import localtime, strftime, mktime

start_time = localtime()
print("Time start at %s" % strftime("%X", start_time))

#Wait for user input
raw_input("Please press Enter to continue... ")


stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print("Timer stopped at %s" % strftime("%X", stop_time))
print("Total time: %s seconds" % difference)