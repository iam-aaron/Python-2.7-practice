#!/usr/bin/python

from fileinput import filename
import glob
import os
import shutil
import json


try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts

receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for file_path in receipts:
    with open(file_path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
        file_name = file_path.split('/')[-1] #-1 to get the last element
        destination = "./processed/%s" % file_name
        shutil.move(file_path, destination)
        print("Moved '%s' to '%s'" % (file_name, destination))

print("Receipt subtotal is %.2f" % subtotal)
#Iterate over receipts
    #read content and tally a subtotal
    #mv the file to the processed directory
    #print that we processed the file

#Print the subtotal of all processed receipts