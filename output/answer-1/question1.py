import pandas as pd
df = pd.read_csv("../../input/question-1/main.csv")
l = []
for i in df:
    if i!='Total':
        l.append(i)
d={}
for i in l:
    d[i]=0
import csv
f = open('main.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Year', 'Population', 'Violent', 'Property', 'Murder', 'Forcible_Rape', 'Robbery', 'Aggravated_assault', 'Burglary', 'Larceny_Theft', 'Vehicle_Theft'])

cnt = 1
for i in range(0, len(df['Population'])):
    if cnt == 1:
        d['Year'] = df['Year'][i]
    for j in l[1:]:
        d[j] += df[j][i]

    if cnt==10:
        data = []
        for i in l:
            data.append(d[i])
        print(data)
        writer.writerow(data)
        for j in l:
            d[j] = 0
        cnt = 0
    cnt += 1