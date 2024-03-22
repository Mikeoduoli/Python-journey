file_read = open(
    'C:/Users/Obed/Documents/Michael_Obed_Oduoli-AccessBank_CoverLetter.docx')
count = 0
for line in file_read:
    count += 1
print("Line count:", count)

# remove the newline character using rstrip()
f_hand = open('mbox-short.txt')
for line in f_hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')

for words in fh:
    caps = words.upper().rstrip()
    print(caps)

    # 7.2 Assignment
    # Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        # new_l = line.strip(line[X-DSPAM-Confidence +1:])
        col_split = line.find(":")
        cln_float = line[col_split + 1:].strip()

        find_avg = float(cln_float)

        count += 1
        total += find_avg
if count != 0:
    avg = total/count
else:
    avg = 0.0
    print()
print("Average spam confidence:", avg)
