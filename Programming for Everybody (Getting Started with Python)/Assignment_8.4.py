with open("romeo.txt", "r") as fname:
    w_list = []

    for line in fname:
        new_l = line.split()
        for nw_line in new_l:
            if nw_line not in w_list:
                w_list.append(nw_line)
w_list.sort()

for l in w_list:
    print(l)
# Displays result in Python's list
print(w_list)
