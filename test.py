import random,time #经常要用到，一个是产生随机数，一个是时间操作的功能
import common

method=common.commondef()
browser = method.browser_open('chrome') #启动chrome浏览器
time.sleep(3) #停顿3秒
browser.maximize_window() #浏览器窗口最大化
url='http://www.baidu.com'
print("now access %s"%url)
browser.get(url)

print ("title of current page is %s" %browser.title)
print ("url of current page is %s" %browser.current_url)

