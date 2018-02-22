from selenium import webdriver
import unittest
from example import driver

class mytest(unittest.TestCase):
    '''testcase开始与结束的保存'''
    def setUp(self):
        self.driver=driver.browserstart()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()