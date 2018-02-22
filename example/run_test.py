from example.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import unittest,time,os
import smtplib

def send_mail(file_new):
    '''发送邮件'''
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    useremail="xqq0603@sina.com"
    msg=MIMEText(mail_body,'html','utf-8')
    #msg['Subject']=Header("自动化测试报告",'utf-8')
    msg['From'] = Header(useremail)

    smtp=smtplib.SMTP()
    smtp.set_debuglevel(1)
    smtp.connect("smtp.sina.com")
    smtp.login(useremail,"10152942xqq")
    smtp.sendmail(useremail,"597129273@qq.com",msg.as_string())
    smtp.quit()
    print("email has send out")

def new_report(testreport):
    '''查找测试报告目录，找到最新文件'''
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__=='__main__':
    #写新的报告内容
    now=time.strftime("%Y%m%d_%H%M%S")
    filename='./sub_part/report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='沪江自动化测试报告',
                          description='环境：win10 chrome')
    discover=unittest.defaultTestLoader.discover('./sub_part/testcase',
                                        pattern='*_sta.py')
    runner.run(discover)
    fp.close()

    file_path=new_report('./sub_part/report/') #查找新生成的报告
    send_mail(file_path) #调用发邮件模块