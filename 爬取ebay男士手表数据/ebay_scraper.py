# TODO
# 1. 向ebay.com发起请求并get到一个页面
# 2. 在每一个详情页面收集信息
# 3. 收集每一张商品页面的链接
# 4. 把爬取到的信息写进cav文件里
import requests
from bs4 import BeautifulSoup  # 把DOM树转换为Python对象树
import csv # 有关于excel或者sqlserver的包吗？

# 获取页面信息
def get_page(url):
    response = requests.get(url) # 返回一个response实例
    #如果网站响应不了，则显示状态码
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')  # lxml是什么?
    return soup

# 获取商品目录链接
def get_index_data(soup):
    try:
        links = soup.find_all('a', {'class': 's-item__link'})
    except:
        links = []
    
    urls = [item.get('href') for item in links]   
    return urls

# 获取商品详细信息
def get_detail_data(soup):
    # title
    # price
    # items sold
    try:
        title = soup.find_all('h1', id='itemTitle')[0].get_text("|").split("|")[1]
    except:
        title = ""
    try:
        price = soup.find_all('span', id='prcIsum')[0].get_text()
    except:
        price = ""
    try:
        itemsSold = soup.find_all('a', {'class': 'vi-txt-underline'})[0].get_text() # 不能写成class=""的形式对吗？
    except:
        itemsSold = ""

    data = {
        'title': title,
        'price': price,
        'itemsSold': itemsSold,
    }
    return data

# 把数据输出为csv文件
def write_csv(data):
    with open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        for i in data:
            row = [i['title'], i['price'], i['itemsSold']]  # 这里应该还有一个链接到指定商品的url字段的
            writer.writerow(row)

def main():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_pgn=1'
    BasePage = get_page(url)
    productsLink = get_index_data(BasePage)
    APageOfDetailData = [get_detail_data(get_page(i)) for i in productsLink]  # 这个命名不太优雅
    write_csv(APageOfDetailData)
    
    
    

if __name__ == '__main__':
    main()