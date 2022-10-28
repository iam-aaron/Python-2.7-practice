#!/usr/bin/python

from fileinput import filename
import glob
import os
import shutil
import json
import re #for regular expression


try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts

#receipts = glob.glob('./new/receipt-[0-9]*.json')

#EVEN RECEIPTS using iglob (iterators)
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') if re.match('./new/receipt-[0-9]*[02468].json',f)]

subtotal = 0.0

for file_path in receipts:
    with open(file_path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
        destination = file_path.replace('new','processed')
        shutil.move(file_path, destination)
        print("Moved '%s' to '%s'" % (file_path, destination))

print("Receipt subtotal is %.2f" % subtotal)
#Iterate over receipts
    #read content and tally a subtotal
    #mv the file to the processed directory
    #print that we processed the file

#Print the subtotal of all processed receipts