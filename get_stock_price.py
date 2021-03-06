


import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:' + lg.error_code)
print('login respond  error_msg:' + lg.error_msg)

#### 获取沪深A股历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data("sz.000725",
    "date, code, open, high, low, close, preclose, volume, amount, adjustflag, turn, tradestatus, pctChg, isST",
    start_date='2015-07-01', end_date='2018-11-30',
    frequency="d", adjustflag="3")
print('query_history_k_data respond error_code:'+rs.error_code)
print('query_history_k_data respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

final_result = result[['date','open','high','low','close','volume', 'adjustflag']]
final_result.columns=['date','open','high','low','close','volume', 'adj_close']
print("History A stock price:\n", final_result)

#### 结果集输出到csv文件 ####
final_result.to_csv('./data/jingdongfang.csv', index=False)

#### 登出系统 ####
bs.logout()