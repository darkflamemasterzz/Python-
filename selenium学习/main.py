from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建Chrome 
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(r"C:\Users\Lenovo\.wdm\chromedriver\74.0.3729.6\win32\chromedriver.exe")
# 打开一个页面
driver.get("https://www.bilibili.com/v/game/stand_alone/?spm_id_from=333.334.b_7072696d6172795f6d656e75.37#/all/click/0/1/2019-05-30,2019-06-06")
# 找到你想要的元素
elements = driver.find_elements_by_class_name("l-item")  # 如何等待页面加载完成?
# 获取视频链接
a = [i.find_element_by_tag_name("a").get_attribute("href") for i in elements]
print(a)
driver.close()

# 标题是否包含Python一词
# assert "Python" in driver.title
# 查找name属性为q的元素
# elem = driver.find_element_by_name("q")
# 发送关键字
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# driver.close()