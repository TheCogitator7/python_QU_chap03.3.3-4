import pandas as pd

#csv 파일을 읽어들일 때
data_csv=pd.read_csv('https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv')

print(data_csv)

#파일썬의 데이터 프레임을 csv 파일로 저장할 대 to_csv()
data_csv.to_csv('data.csv')

print()
print()

#excel 파일을 읽어들일 때
data_excel=pd.read_excel('https://github.com/hyunyulhenry/quant_py/raw/main/kospi.xlsx', sheet_name='kospi')

print(data_excel)

#데이터 프레임을 엑셀 파일로 저장할 때 to_excel()
data_excel.to_excel('data.xlsx')


