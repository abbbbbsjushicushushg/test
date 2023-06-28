# import requests
# import json
# import pandas as pd
# # 找到网页的动态部分
# get_url = "https://www.gd.gov.cn/gkmlpt/api/all/5?page=1&sid=2"  # 如图二所示
# formdata={"page":1,"sid":2}  #
# # 通过post获取动态的json文件
# resp = requests.get(get_url,data=formdata,headers={'User-Agent':'Mozilla/5.0'})
# resp.raise_for_status()                 # 返回爬取状态
# resp.encoding = resp.apparent_encoding  # 编码
# polices = json.loads(resp.text)         # json格式用json打开后是字典
# print(polices)
# #写入csv文件
# suyins = []
# publishers = []
# dates = []
# titles = []
# links = []
# for police in polices["articles"]:
#     print(police)
#     suyin = police.get("identifier")
#     publisher = police.get("publisher")
#     date = police.get("created_at")
#     title = police.get("title")
#     link = police.get("url")
#     suyins.append(suyin)
#     publishers.append(publisher)
#     dates.append(date)
#     titles.append(title)
#     links.append(link)
# data = {'索引号':suyins,'发布机构':publishers,'发布日期':dates,'政策标题':titles,'政策正文链接':links}
# trydf = pd.DataFrame(data)
# trydf.to_csv('polices.csv', index=False, encoding='utf-8', mode='a')
#
import numpy as np
import pandas as pd
df = pd.read_csv('polices.csv')
#print(df.head())
#df['发布日期'] = pd.to_datetime(df['发布日期'],format='Y%-m%-d%',errors = 'coerce') #将数据类型转换为日期类型
#根据输入日期输出政策
print("请输入日期（格式为Y%-m%-d%）：")
date = input()
# 读取第B列中大于6的值
mask = df["发布日期"] == date
pos = np.flatnonzero(mask)
print(df.iloc[pos])

