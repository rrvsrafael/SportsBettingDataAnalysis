import os
import pandas as pd

directory = 'data'
filename = 'E02021.csv'
filepath = os.path.join(directory, filename)
df = pd.read_csv(filepath)
cut = pd.DataFrame(df[['FTR', 'B365H', 'B365D', 'B365A']])

home = cut[cut['FTR'] == 'H']
draw = cut[cut['FTR'] == 'D']
away = cut[cut['FTR'] == 'A']
home = home['B365H']
draw = draw['B365D']
away = away['B365A']

print(home.mean(), draw.mean(), away.mean())

home.plot.hist(alpha=0.5)
draw.plot.hist(alpha=0.5)
away.plot.hist(alpha=0.5).get_figure().savefig('plot.jpg')
