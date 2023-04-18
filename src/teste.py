import os
import pandas as pd
from importlib.metadata import files
import numpy as np

directory = '../data/premierleague/'
extension = '.csv'
dfGeral = pd.DataFrame()

for file in os.listdir(directory):
    if file.endswith(extension):
        df = pd.read_csv(directory + file)
        cut = pd.DataFrame(
            df[['FTR', 'AvgH', 'AvgD', 'AvgA']])
        dfGeral = dfGeral.append(cut)

dfGeral['AvgH'] = dfGeral['AvgH'].round(1)
dfGeral['AvgD'] = dfGeral['AvgD'].round(1)
dfGeral['AvgA'] = dfGeral['AvgA'].round(1)

faixas = np.linspace(1.0, 100.0, 990).round(1)

dfFaixas = pd.DataFrame(0,
                        index=faixas,
                        columns=['% Odd', '% Real', 'AvgHT', 'AvgHR', 'AvgDT', 'AvgDR', 'AvgAT', 'AvgAR'])

FTRH = dfGeral['AvgH'][dfGeral['FTR'] == 'H']
FTRD = dfGeral['AvgD'][dfGeral['FTR'] == 'D']
FTRA = dfGeral['AvgA'][dfGeral['FTR'] == 'A']

for faixa in faixas:
    dfFaixas.at[faixa, 'AvgHT'] = (dfGeral['AvgH'] == faixa).sum()
    dfFaixas.at[faixa, 'AvgHR'] = (FTRH == faixa).sum()
    dfFaixas.at[faixa, 'AvgDT'] = (dfGeral['AvgD'] == faixa).sum()
    dfFaixas.at[faixa, 'AvgDR'] = (FTRD == faixa).sum()
    dfFaixas.at[faixa, 'AvgAT'] = (dfGeral['AvgA'] == faixa).sum()
    dfFaixas.at[faixa, 'AvgAR'] = (FTRA == faixa).sum()
    dfFaixas.at[faixa, '% Odd'] = (1/faixa).round(2)
    dfFaixas.at[faixa, '% Real'] = ((
        dfFaixas.at[faixa, 'AvgHR'] + dfFaixas.at[faixa, 'AvgDR'] + dfFaixas.at[faixa, 'AvgAR']) / (
            dfFaixas.at[faixa, 'AvgHT'] + dfFaixas.at[faixa, 'AvgDT'] + dfFaixas.at[faixa, 'AvgAT'])).round(2)

print(dfFaixas.head(50))
