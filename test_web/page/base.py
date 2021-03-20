from selenium import  webdriver
from  selenium.webdriver.remote.webdriver import WebDriver
import sys
from page.tools import get_root_dir

sys.path.append(get_root_dir())


class Base:

    base_url=''

    def __init__(self,webdrive: WebDriver=None):
        #如果webdrive为空就创建个webdrive  不为空则复用一个webwebdrive
        #复用通同一个游览器
        if  webdrive is None:
            home = webdriver.ChromeOptions()
            home.debugger_address = '127.0.0.1:9222'
            self.webdriver = webdriver.Chrome(options=home)
            self.webdriver.maximize_window()
            self.webdriver.implicitly_wait(10)

        else:

            self.webdriver=webdrive

        if self.base_url!='':
            self.webdriver.get(self.base_url)