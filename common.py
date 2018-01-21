from selenium import webdriver #引入selenium模块。
from selenium.webdriver.common.keys import Keys #模拟键盘输入。
import random,time #经常要用到，一个是产生随机数，一个是时间操作的功能

class commondef(object):
    def __init__(self):
        print("init")
    def browser_open(self,br):  #启动浏览器
        try:
            if br=='chrome':
                browser = webdriver.Chrome()
                return browser
            elif br=='ie':
                browser = webdriver.firefox()
                return browser
        except Exception as msg:
            print("open error:%s"%msg)

