import csv    #加载csv包便于读取csv文件
import pandas as pd


def xlsx_to_csv_pd():
    #data_xls = pd.read_excel('zhongxing.xlsx', index_col=0)
    #data_xls.to_csv('zhongxing.csv', encoding='utf-8',sep='\t')
    #data_xls = pd.read_excel('falv.xlsx', index_col=0)
    #data_xls.to_csv('falv.csv', encoding='utf-8', sep='\t')
    data_xls = pd.read_excel('qinggan.xlsx', index_col=0)
    data_xls.to_csv('qinggan.csv', encoding='utf-8', sep='\t')


if __name__ == '__main__':
    xlsx_to_csv_pd()

