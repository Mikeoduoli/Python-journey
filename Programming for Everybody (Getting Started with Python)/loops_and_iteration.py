large_num = None
small_num = None
while True:
    l_num = input("Enter a number:")
    if l_num == 'done':
        break
    try:
        num = int(l_num)
    except ValueError:
        print("Not valid input")
        continue

    if large_num is None or num > large_num:
        large_num = num
    if small_num is None or num < small_num:
        small_num = num

print("Maximum is", large_num)
print("Minimum is", small_num)
