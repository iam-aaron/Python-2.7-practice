#!/usr/bin/python

import subprocess

#APPROACH 1
# code = subprocess.call(['ls', '-l'])
# if code == 0:
#     print("command finished successfully")
# else:
#     print("failed with code: %i" & code)


#APPROACH 2
# output = subprocess.check_output(['ls', '-l'])
# print(output)


#APPROACH 3
try:
    output = subprocess.check_output(
        ['ls fake.txt'],
        stderr=subprocess.STDOUT
    )
except OSError as err:
    print("Caught OSError")
    output = err
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessError")
    output = err

print(output)