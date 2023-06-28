'''爬取政策基本信息'''
# -*- coding:utf-8 -*-
import requests
import json
import time
import datetime
from datetime import datetime
import  pandas as pd

# 找到网页的动态部分
def polices_list(page):
    get_url = "https://www.gd.gov.cn/gkmlpt/api/all/5?page="+str(page)+"&sid=2"
    formdata = {"page": page,"sid":2}  # 可以传入的数据（翻页数据)

    # 通过get获取动态的json文件
    resp = requests.get(get_url, data=formdata, headers={'User-Agent': 'Mozilla/5.0'})
    resp.raise_for_status()  # 返回爬取状态
    resp.encoding = resp.apparent_encoding  # 编码
    polices = json.loads(resp.text)  # json格式用json打开后是字典
    return polices
#写入csv文件
def polices_csv(polices):
    suyins = []
    publishers = []
    dates = []
    titles = []
    links = []
    # #时间限制
    s_date = datetime.strptime('20220101', '%Y%m%d').date()
    e_date = datetime.strptime('20230601', '%Y%m%d').date()
    for police in polices["articles"]:
        print(police)
        suyin = police.get("identifier")
        publisher = police.get("publisher")
        date1 = police.get("created_at")
        date = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        title = police.get("title")
        link = police.get("url")
        suyins.append(suyin)
        publishers.append(publisher)
        dates.append(date)
        titles.append(title)
        links.append(link)
    data = {'索引号': suyins, '发布机构': publishers, '发布日期': dates, '政策标题': titles, '政策正文链接': links}
    df = pd.DataFrame(data)
    df.to_csv('polices.csv', index=False, encoding='utf-8', mode='a')
if __name__ == '__main__':
    total_colleges = []
    for page in range(49):  # 设置一下总页数
        time.sleep(1)
        print("正在下载第%d页" % (page + 1))  # 慢点下，给服务器点温暖
        polices = polices_list(page)
        print(polices)
        polices_csv(polices)
        data = pd.read_csv('polices.csv')
