def computepay(h, r):
    if (h <= 40):
        Pay = h * r
    else:
        flat_pay = 40 * r
        more_pay = (h - 40) * (1.5 * r)
        Pay = more_pay + flat_pay
    return Pay


hrs = float(input("Enter Hours:"))
rate_h = float(input("Enter Rate per Hour:"))
p = computepay(hrs, rate_h)
print("Pay", p)

# Git pull and git push again