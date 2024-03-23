f_names = open("mbox-short.txt", "r")

count = 0

for fname in f_names:
    fname = fname.rstrip()
    if not fname.startswith("From "):
        continue
    emails = fname.split()
    print(emails[1])

    count += 1


print("There were", count, "lines in the file with From as the first word")
