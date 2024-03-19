# We use range function to generate a
# sequence of numbers

numbers = range(5, 10, 2)

# we apply the 3rd value as a step

# that's our range object - generates range
# of numbers. the fifth number is excluded.

range(0, 5)

for num in numbers:
    print(num)

# also we can call range() directly without
# storing it in a variable

for num in range(5):
    print(num)
