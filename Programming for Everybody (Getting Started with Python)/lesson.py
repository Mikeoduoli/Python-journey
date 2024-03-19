hrs = float(input("Enter hours:"))
rate_h = float(input("Enter rate per hour:"))

if (hrs <= 40):
    pay = hrs * rate_h

else:
    casual_Pay = 40 * rate_h
    more_Pay = (hrs - 40) * (1.5 * rate_h)
    pay = casual_Pay + more_Pay

print(pay)