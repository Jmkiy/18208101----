 # -*- coding: utf-8 -*-
import requests
import re
import pandas as pd
import time

# 此处写入登录之后自己的cookies
cookie = 'miid=150877443339258688; cna=PGgWFmpqng8CAd9oChejfbmx; thw=cn; tracknick=%5Cu83C1%5Cu83C1%5Cu5E02%5Cu573A; enc=vwJ6V28EKqJUVvhw8m%2BRwN22Ign8PZ6wNQSK14oWVBIV7yVwo1UyO4DyNeXqlTaAh%2BcP%2FgyXzgbXRO8CjigSdQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=0551e057e452b5e888030e5e8e01cf17_1598846479137; _m_h5_tk_enc=979e9ca48dc66f752aa362718c232dad; xlly_s=1; mt=ci%3D-1_1; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hooeq07xV8T8K7SUo4kCOJfIguTbH55iRGA%2FmfYCmBvLtzdHbjB7g5lRdZCSpILm7WAGYIpaBYTMs60k8wLmgrdCMDweCO%2BJGdi7l4y%2BQW%2FNHSxQv5ISfcReyS8wU%2FC%2B3N7eDjVAQQC3MUz5Ic9gF7qYtb1H5Z4AcF5E3HhnYzM26a15%2BpV2k609hyKfwCpzjiDg9AvSnmUyeNUDSFgqrcmeH7W%2B8JjFKoFbSZBmKhK4J0SQF3vKgEV%2FE%3D; lLtC1_=1; _samesite_flag_=true; cookie2=1fe444e53dfdcf087cfc5fcca98e4322; t=2fb70f695e8cc55d23498fa57f505674; _tb_token_=f63b77e73ef77; v=0; alitrackid=blog.csdn.net; sgcookie=E100U9rxY%2F0BmjHfYGurtlAO0UVPSCTB9nPywNnLQinD7nRHQmS7qPcoirCEz5Y557g715ToyGoMo0ScMOQXBfuVMA%3D%3D; unb=2679294552; uc3=id2=UU6m1mkaNEa0DQ%3D%3D&nk2=vsAduqyoz6Q%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCufXEBZK9hV5GHWQ%3D; csg=3b0a5a55; lgc=%5Cu83C1%5Cu83C1%5Cu5E02%5Cu573A; cookie17=UU6m1mkaNEa0DQ%3D%3D; dnk=%5Cu83C1%5Cu83C1%5Cu5E02%5Cu573A; skt=d59c96869066cbe3; existShop=MTU5ODg2MDQyMw%3D%3D; uc4=nk4=0%40vFWmNaX%2BuEzm%2B8deKQjUAaYSHw%3D%3D&id4=0%40U2xrex%2Ff5%2BvVBmyo%2F%2BiSkxWyn5M%2B; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%9C%BA29; _nk_=%5Cu83C1%5Cu83C1%5Cu5E02%5Cu573A; cookie1=BYk%2Fi9v3dWrX64g34J2uQwRl3Ccp5rCbBPUX3UcXU8w%3D; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&pas=0&existShop=false&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie15=UIHiLt3xD8xYTw%3D%3D&cookie14=UoTV5OJnvA3KJw%3D%3D; JSESSIONID=054EE7B9D73CF1FF629FC8EAD368F3AF; lastalitrackid=i.taobao.com; l=eBS-4_2qQUFIfdtDBOfwhurza77O9IRfguPzaNbMiOCPOlCd2lQ5WZPpDqY9CnGVn6o2R3Wm0ejkB8YgOyzh5mW9BJLCgsDLLdTh.; tfstk=cOaCBAD2epvIPIsy8W1ZU9nurT05Z4TssFDaOk_oPUIBWlFCifYqh2fqOdTtDf1..; isg=BAoK4D_HYQkcUeyg7eNZoFZWW_Cs-45Vbs7ebZRDi924R6sBfIj2ZPu9U7Obtwbt '
# 获取页面信息
def getHTMLText(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    user_cookies = cookie
    cookies = {}
    for a in user_cookies.split(';'):  # 因为cookies是字典形式，所以用spilt函数将之改为字典形式
        name, value = a.strip().split('=', 1)
        cookies[name] = value
    try:
        r = requests.get(url, cookies=cookies, headers=headers, timeout=60)
        print(r.status_code)
        # print(r.cookies)
        return r.text
    except:
        print('获取页面信息失败')
        return ''

    #  格式化页面，查找数据


def parsePage(html):   #采用正则表达式进行解析
     list = []
     try:
         views_title = re.findall('"raw_title":"(.*?)","pic_url"', html)
         print(len(views_title))  # 打印检索到数据信息的个数，如果此个数与后面的不一致，则数据信息不能加入列表
         print(views_title)
         views_price = re.findall('"view_price":"(.*?)","view_fee"', html)
         print(len(views_price))
         print(views_price)
         item_loc = re.findall('"item_loc":"(.*?)","view_sales"', html)
         print(len(item_loc))
         print(item_loc)
         views_sales = re.findall('"view_sales":"(.*?)","comment_count"', html)
         print(len(views_sales))
         print(views_sales)
         comment_count = re.findall('"comment_count":"(.*?)","user_id"', html)
         print(len(comment_count))
         print(comment_count)
         shop_name = re.findall('"nick":"(.*?)","shopcard"', html)
         print(len(shop_name))
         for i in range(len(views_price)):
             list.append([views_title[i], views_price[i], item_loc[i], comment_count[i], views_sales[i], shop_name[i]])
         # print(list)
         print('爬取数据成功')
         return list
     except:
         print('有数据信息不全，如某一页面中某一商品缺少地区信息')

     # 存储到csv文件中，为接下来的数据分析做准备


def save_to_file(list):
     data = pd.DataFrame(list)
     data.to_csv('F:\\数据采集\\淘宝空调数据.csv', header=False, mode='a+')  # 用追加写入的方式


def main():
     name = [['views_title', 'views_price', 'item_loc', 'comment_count', 'views_sales', 'shop_name']]
     data_name = pd.DataFrame(name)
     data_name.to_csv('F:\\数据采集\\淘宝空调数据.csv', header=False, mode='a+')  # 提前保存一行列名称
     goods = input('请输入想查询的商品名称：'.strip())  # 输入想搜索的商品名称
     depth = 50  # 爬取的页数
     start_url = 'http://s.taobao.com/search?q=' + goods  # 初始搜索地址
     for i in range(depth):
         time.sleep(3 + i)
         try:
             page = i + 1
             print('正在爬取第%s页数据' % page)
             url = start_url + 'imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200415&ie=utf8&bcoffset=3&p4ppushleft=1%2C48&sort=default&ntoffset=3&s=' + str(
                 44 * i)
             html = getHTMLText(url)
             # print(html)
             list = parsePage(html)
             save_to_file(list)
         except:
             print('数据没保存成功')

if __name__ == '__main__':
     main()