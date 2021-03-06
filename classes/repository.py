import pandas as pd
import os
import xlrd
import numpy as np

from classes.views import Posicao, Extrato


class PosicaoRepository:

    files = os.listdir('./datasets/posicao/')
    posicao = Posicao()
    extrato = Extrato()

    stocks = pd.DataFrame()
    pickings = pd.DataFrame()
    fis = pd.DataFrame()
    fiis = pd.DataFrame()
    picking_fii = pd.DataFrame()

    def load_data(self):
        print('chamando load_data ...')
        for file_name in self.files:
            print(file_name)
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

            df_stocks = self.posicao.get_acoes(df)
            df_stocks['period'] = period
            self.stocks = self.stocks.append(df_stocks, ignore_index=True)

            df_pickings = self.posicao.get_acoes_provento(df)
            df_pickings['period'] = period
            self.pickings = self.pickings.append(df_pickings, ignore_index=True)

            df_fi = self.posicao.get_fi(df)
            df_fi['period'] = period
            self.fis = self.fis.append(df_fi, ignore_index=True)

            df_fii = self.posicao.get_fii(df)
            df_fii['period'] = period
            self.fiis = self.fiis.append(df_fii, ignore_index=True)

            df_picking_fii = self.posicao.get_fii_proventos(df)
            df_picking_fii['period'] = period
            self.picking_fii = self.picking_fii.append(df_picking_fii, ignore_index=True)