import pandas as pd
df = pd.read_csv("../../input/question-2/main.csv")
occup = []
for i in df['occupation']:
    if i not in occup:
        occup.append(i)
occup.sort()
d = {}
for i in occup:
    d[i] = []
for i in range(1, len(df['occupation'])):
    a = df['occupation'][i]
    if len(d[a]) == 0:
        d[a].append(df['age'][i])
        d[a].append(df['age'][i])
    else:
        if d[a][0] > df['age'][i]:
            d[a][0] = df['age'][i]
        if d[a][1] < df['age'][i]:
            d[a][1] = df['age'][i]

import csv
f = open('main.csv', 'w')
writer = csv.writer(f)
writer.writerow(['occuption', 'min', 'max'])
for i in d:
    writer.writerow([i, d[i][0], d[i][1]])