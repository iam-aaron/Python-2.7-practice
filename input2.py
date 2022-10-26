#!/usr/bin/python

def gather_information():
    height = float(raw_input("What is your height? (inches or meters) "))
    weight = float(raw_input("What is your weight? (pounds  or kilograms) "))
    unit = raw_input("Are your measurements in imperial or metric units? ").lower().strip()
    return (height, weight, unit)

def compute_bmi(height, weight, unit='metric'): #sets default unit as "metric"
    if unit == "metric":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    print("Your BMI is %s" % bmi)

while True:
    height, weight, unit = gather_information()
    if unit.startswith('i'):
        compute_bmi(height=height, weight=weight, unit="imperial") #key word arguments
        break
    elif unit.startswith('m'):
        compute_bmi(height, weight) #positional arguments
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric")
