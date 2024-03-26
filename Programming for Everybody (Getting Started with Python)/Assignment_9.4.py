name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sender = {}
for line in handle:
    if line.startswith("From "):
        line = line.rstrip().split()
        word = line[1]
        sender[word] = sender.get(word, 0) +1


bigword = None
bigcount = None

for word, count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)