import tushare as ts


'''
输入参数
名称	类型	必选	描述
is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
list_status	str	N	上市状态： L上市 D退市 P暂停上市
exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)

输出参数
名称	类型	描述
ts_code	str	TS代码
symbol	str	股票代码
name	str	股票名称
area	str	所在地域
industry	str	所属行业
fullname	str	股票全称
enname	str	英文全称
market	str	市场类型 （主板/中小板/创业板）
exchange	str	交易所代码
curr_type	str	交易货币
list_status	str	上市状态： L上市 D退市 P暂停上市
list_date	str	上市日期
delist_date	str	退市日期
is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
'''

pro = ts.pro_api('0032c5c89307c3f05daee628ea576ceb2afc87ed5ccdcd033dbe6748')
#查询当前所有正常上市交易的股票列表
# df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,list_date,is_hs')
# print (df)

#查询曾用名
# df2 = pro.namechange(ts_code='002456.SZ', fields='ts_code,name,start_date,end_date,change_reason')
# print (df2)

#查询沪股通、深股通信息
# df3 = pro.hs_const(hs_type='SH')
# print (df3)

#查询上市公司基础信息
# df4 = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
# print (df4)

#IPO新股列表
# df5 = pro.new_share(start_date='20190901', end_date='20190429')
# print (df5)

df6 = pro.daily(ts_code='000001.SZ', start_date='20190428', end_date='20190429')
print (df6)