#%%
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import json

#%%
data = pd.read_excel('./P3PRIB01.xls', sheetname='celková výška sněhu', skiprows=3)

d = data[(data['měsíc'] == 11) | (data['měsíc'] == 12)]
d = d.to_dict(orient='index')

#%%
out = {}
for v in d.values():
    if v['rok'] not in out:
        out[v['rok']] = []
    out[v['rok']].extend(list(v.values())[2:])

for rok in out.values():
    del rok[30]

#%%
for rok in out.values():
    plt.plot(list(range(0, 61)), rok, color='skyblue', linewidth=0.3)

#%%
with open('snih.js', 'w', encoding='utf-8') as f:
    f.write('var snih = ' + json.dumps(out) + ';')

#%%
j = 0
for o in out.values():
    x = 0
    for v in o[20:31]:
        if v > 15:
            x = 1
    j += x

#%%
j
#%%
(j / len(out)) * 100

#%%
days = []
for i in range(1, 31):
    days.append(str(i) + '. 11.')

for i in range(1, 32):
    days.append(str(i) + '. 12.')
days

