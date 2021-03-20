from selenium.common.exceptions import NoAlertPresentException
from page.base import Base
from time import sleep

class Friendship(Base):
    def goto_friendship_msg(self,urlname,mailbox,url,msgtext):
        sleep(2)
        self.webdriver.execute_script('window.scrollTo("100","2000");')
        self.webdriver.find_element_by_css_selector('.apply-tip input[placeholder="站点名称(必填)"]').send_keys(urlname)
        self.webdriver.find_element_by_css_selector('.apply-tip input[placeholder="个人邮箱(必填)"]').send_keys(mailbox)
        self.webdriver.find_element_by_css_selector('.apply-tip input[placeholder="网站地址(必填)"]').send_keys(url)
        self.webdriver.find_element_by_css_selector('.list_show textarea').send_keys(msgtext)
        self.webdriver.find_element_by_css_selector('.but').click()

        # 异常捕获，存在alert处理alert，没有alert就往下走
        try:
            sleep(1)
            alert = self.webdriver.switch_to_alert()
            text=alert.text
            sleep(1)
            alert.accept()
            if text=='提交成功':
                sleep(1)
                self.webdriver.execute_script('window.scrollTo("2000","0");')
                urlname_list = self.webdriver.find_elements_by_css_selector('.list-demo ul li a')
                print(f'现在有{len(urlname_list)}条数据')
                for i in urlname_list:
                    text = i.text
                    if text == urlname:
                        print(text)

            else:
                print(text)


        except NoAlertPresentException:
            print('用例执行失败')



        return
