x = 1
print(x)


# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour
# to test the program (the pay should be 96.25). You should use input to read
# a string and float() to convert the string to a number.
# Do not worry about error checking or bad user data.

# This first line is provided for you

hrs = float(input("Enter Hours:"))
rateHrs = float(input("Enter Rate per Hour:"))


Pay = int(hrs) * rateHrs

print("Pay:", Pay)


# Exercise 3.3

