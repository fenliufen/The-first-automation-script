from selenium.common.exceptions import NoAlertPresentException
from time import sleep
from .base import Base
from .friendship import Friendship


class About(Base):

    def goto_about_msg(self,name, mailbox ,url,msg):
        self.webdriver.find_element_by_css_selector('.test_01 input[placeholder="昵称(必填)"]').send_keys(name)
        self.webdriver.find_element_by_css_selector('.test_01 input[placeholder="邮箱(必填)"]').send_keys(mailbox)
        self.webdriver.find_element_by_css_selector('.test_01 input[placeholder="网址(选填)"]').send_keys(url)
        self.webdriver.find_element_by_css_selector('.test_show  textarea').send_keys(msg)
        self.webdriver.find_element_by_css_selector('.test_show .but').click()

        #断言，存在alert处理alert，没有alert就往下走
        try:
            sleep(1)
            alert = self.webdriver.switch_to_alert()
            print(alert.text)
            alert.accept()
        except NoAlertPresentException:
            sleep(1)
            username = self.webdriver.find_element_by_css_selector('.username').text
            if name in username:
                print(username)
                print('添加成功了数据+1')



        return self

    def goto_friendship(self):
        self.webdriver.find_element_by_css_selector('.mylist-01 a[href="/friendship"]').click()
        return Friendship()

