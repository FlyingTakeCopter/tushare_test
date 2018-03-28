import tushare as ts

df = ts.stock_pledged()

# print(df)

print(df[df.p_ratio >= 50]['code'])
