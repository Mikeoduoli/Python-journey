text = "X-DSPAM-Confidence:    0.8475"

# num = text.find("0.8475")

# pos = float(num(num[23:29]))

# print(pos)


find_col = text.find(":")

num = text[find_col +1:].strip()


pos = float(num)

print(pos)