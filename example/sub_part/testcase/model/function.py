from selenium import webdriver
import os
import time

def insert_img(driver,file_name):
    '''自动化测试截图'''
    base_dir=os.path.dirname(os.path.dirname(__file__))    #取得当前路径
    base_dir=str(base_dir)                                 #路径转字符串
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/testcase')[0]                   #修改保存路径
    file_path=base+"/report/img/"+file_name
    driver.get_screenshot_as_file(file_path)                #截图保存
    print(base)

if __name__=="__main__":
   driver=webdriver.Chrome()
   driver.get("http://www.baidu.com/")
   timestamp=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))    #时间戳取得
   insert_img(driver,'baidu'+timestamp+'.jpg')
   driver.quit()
