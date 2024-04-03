import pandas as pd

# 读取 Excel 文件
excel_data = pd.read_excel('Data.xlsx', engine='openpyxl')

# 将数据写入到文本文件
with open('output.txt', 'w') as f:
    for index, row in excel_data.iterrows():
        line = '\t'.join(map(str, row))  # 将一行数据转换为字符串，使用制表符分隔
        f.write(line + '\n')  # 将数据写入到文本文件，并添加换行符
