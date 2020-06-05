import pandas as pd
import os
import xlrd
import numpy as np

from views import Posicao, Extrato

files = os.listdir('./datasets/posicao/')

stocks = pd.DataFrame()
pickings = pd.DataFrame()
fis = pd.DataFrame()
fiis = pd.DataFrame()
picking_fii = pd.DataFrame()

posicao = Posicao()
extrato = Extrato()

for file_name in files:
    if file_name == '.DS_Store':
        continue
    
    wb = xlrd.open_workbook('./datasets/posicao/' + file_name, logfile=open(os.devnull, 'w'))
    df = pd.read_excel(wb)
    
    #df = pd.read_excel('../datasets/' + file_name)
    date_position = df[df['Unnamed: 56'].str.contains('Data de referência', na=False)]['Unnamed: 56']
    
    # position date
    date_position = pd.to_datetime(date_position.str.replace('Data de referência: ', ''), format='%d/%m/%Y')
    
    #month = int(date_position.dt.month.values)
    #year = int(date_position.dt.year.values)
    #period = str(year) + '/' + str(month)
    period = date_position.values[0]

    
    # get stocks
    df_stocks = posicao.get_acoes(df)
    #display(df_stocks.head())
    df_stocks['period'] = period
    stocks = stocks.append(df_stocks, ignore_index=True)

    df_pickings = posicao.get_acoes_provento(df)
    df_pickings['period'] = period
    pickings = pickings.append(df_pickings, ignore_index=True)

    df_fi = posicao.get_fi(df)
    df_fi['period'] = period
    fis = fis.append(df_fi, ignore_index=True)

    df_fii = posicao.get_fii(df)
    df_fii['period'] = period
    fiis = fiis.append(df_fii, ignore_index=True)

    df_picking_fii = posicao.get_fii_proventos(df)
    df_picking_fii['period'] = period

    picking_fii = picking_fii.append(df_picking_fii, ignore_index=True)

print(picking_fii.sort_values(by='period').head())