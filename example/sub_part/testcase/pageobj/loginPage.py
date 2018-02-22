from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from example.sub_part.testcase.pageobj import base
import time

class login(base.Page):
    '''用户登录页面'''

    url='/'
    user_img_loc=(By.XPATH,"//a[@class='fastLogin']/span")
    #user_login_loc=(By.ID,"mzLogin")

    def bbs_login(self):
        self.find_element(*self.user_img_loc).click()
        time.sleep(1)
        #self.find_element(*self.user_login_loc).click()

    login_name_loc=(By.NAME,"username")
    login_password_loc=(By.NAME,"password")
    login_button_loc=(By.XPATH,"//button[@class='hp-btn hp-btn-green']")

    #用户名密码和按钮
    def login_action(self,username,password):
        self.find_element(*self.login_name_loc).send_keys(username)
        self.find_element(*self.login_password_loc).send_keys(password)
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username="airetest010",password="hujiang1234"):
        '''登录行为'''
        self.open()
        self.bbs_login()
        self.login_action(username,password)
        time.sleep(1)

    user_err_loc=(By.XPATH,"//div[@class='hp-input hp-input-username hp-input-err']/span[@class='hp-err-tips']")
    password_err_loc = (By.XPATH, "//div[@class='hp-input hp-input-err']/span[@class='hp-err-tips']")
    login_success_loc = (By.XPATH, "//a[@class='user-pic']/img")
    #错误提示
    def user_err_tips(self):
        return self.find_element(*self.user_err_loc).text
    def password_err_tips(self):
        return self.find_element(*self.password_err_loc).text
    #成功用户名
    def login_success_tips(self):
        time.sleep(10)
        return  self.find_element(*self.login_success_loc).get_attribute('alt')