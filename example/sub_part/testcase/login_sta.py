import time
import unittest,random,sys
from example.sub_part.testcase.model import myunit,function
from example.sub_part.testcase.pageobj import loginPage

class loginTest(myunit.mytest):
    '''登陆测试'''

    #测试用户登陆
    def user_login_verify(self,username="",password=""):
        loginPage.login(self.driver).user_login(username,password)


    def test_login1(self):
        '''用户名密码为空'''
        self.user_login_verify("","")
        po=loginPage.login(self.driver)
        self.assertEqual(po.user_err_tips(),"不能为空")
        self.assertEqual(po.password_err_tips(),"不能为空")
        function.insert_img(self.driver,"up_empty.jpg")

    def test_login2(self):
        '''用户名正确密码空'''
        self.user_login_verify(username="airetest010")
        po=loginPage.login(self.driver)
        self.assertEqual(po.password_err_tips(), "不能为空")
        function.insert_img(self.driver, "password_empty.jpg")

    def test_login3(self):
        '''用户名空密码正确'''
        self.user_login_verify(password="hujiang1234")
        po = loginPage.login(self.driver)
        self.assertEqual(po.user_err_tips(), "不能为空")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        '''账密不匹配'''
        pass

    def test_login5(self):
        '''均正确'''
        self.user_login_verify(username="airetest010",password="hujiang1234")
        time.sleep(2)
        po = loginPage.login(self.driver)
        self.assertEqual(po.login_success_tips(),"airetest010")
        function.insert_img(self.driver, "success.jpg")
        

if __name__=="__main__":
    unittest.main()