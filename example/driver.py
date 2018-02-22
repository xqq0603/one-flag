from selenium import webdriver
def browserstart():
    '''浏览器启动'''
    try:
        browser=webdriver.Chrome()
        return browser
    except Exception as msg:
        print("浏览器打开异常")

if __name__=="__main__":
    dr=browserstart()
    dr.get("http://www.baidu.com")
    dr.quit()
