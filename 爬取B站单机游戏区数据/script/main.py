from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://www.bilibili.com/v/game/stand_alone/?spm_id_from=333.334.b_7072696d6172795f6d656e75.37#/all/click/0/1/2019-05-28,2019-06-04"
html = urlopen(base_url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
vedio_block = soup.find_all('div', {'class': 'vd-list-cnt'})    
print(vedio_block)

