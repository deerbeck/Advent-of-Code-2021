b_ele = ["22 13 17 11 0",
 "8 2 23 4 24",
"21 9 14 16 7",
 "6 10 3 18 5",
 "1 12 20 15 19"]

p = 100
w_element = []
columns = [[],[],[],[],[]]
rows = [[],[],[],[],[]]
for i in range(5):
    for l in range(5):
        columns[i].append(b_ele[l].split(" ")[i])

for i in range(5):
    rows[i] = b_ele[i].split(" ")

print(columns)
print(rows)