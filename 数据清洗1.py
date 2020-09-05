import pandas as pd  # 导入pandas库
data = pd.read_csv("F:\\数据采集\\数据采集课设\\淘宝空调数据.csv",encoding='utf-8-sig')
print(data.describe())
# 将工资低于1000或者高于10万的异常值清空
data[u'views_price'][(data[u'views_price'] < 900) | (data[u'views_price']> 30000)] = None
data.dropna()#删除空缺值
print(data.describe())
print(data.shape)
data.to_csv('F:\\数据采集\\数据采集课设\\淘宝空调数据.csv',index = False,encoding='utf-8-sig')