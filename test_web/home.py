from .base import Base
from selenium.webdriver.common.by import By
from time import sleep
from .journal import Journal


class Home(Base):
    base_url = 'http://112.74.38.68:81/home'


    #输入框输入条件
    def goto_home(self,value):
        self.webdriver.find_element(By.CSS_SELECTOR, ".doahang-tlter label input[type='text']").send_keys(value)
        return  self


    #点击搜索
    def goto_seek(self,val):
        self.webdriver.find_element(By.CSS_SELECTOR,".doahang-tlter label span").click()
        sleep(1)
        self.webdriver.find_element(By.CSS_SELECTOR, ".doahang-tlter label input[type='text']").clear()
        list = self.webdriver.find_elements_by_css_selector('.iconfont1')
        sleep(2)
        self.webdriver.save_screenshot(f'./result/{val}.png')
        if len(list)==0:
            print('数据为空')
        else:
            print(f'总共有{len(list)}数据')
            for i in list:
                text = i.text
                if val in text:
                    print('数据一致')
        return self



    #点击全部文章
    def goto_complete(self,val):
        li = self.webdriver.find_elements_by_css_selector('.daohang-list li')
        li[0].click()
        sleep(1)
        list=self.webdriver.find_elements_by_css_selector('.list li')
        lens=len(list)
        assert lens==val
        return self



    #点击标签除全部文章
    def goto_webtest(self,index,val):
        li = self.webdriver.find_elements_by_css_selector('.daohang-list li')
        li[index].click()
        list = self.webdriver.find_elements_by_css_selector('.iconfont1')
        sleep(1)
        self.webdriver.save_screenshot(f'./result/{index}.png')
        if len(list)==0:
            print('数据为空')
        else:
            print(f'总共有{len(list)}数据')
            for i in list:
                text = i.text
                if val in text:
                    print('数据一致')

        return self


   #验证滚动条是都可以用 因为其他页面的滚动条都是一个方法，所有验证一次就行
    def  goto_slide(self,x,y):
        self.webdriver.refresh()
        sleep(2)
        js = f"window.scrollTo({x},{y});"
        self.webdriver.execute_script(js)
        sleep(2)
        self.webdriver.find_element_by_css_selector('#gotop').click()
        print('滑动滚动条，并且一键返回顶部')
        return self



    #去日志文章页面
    def goto_journal(self):
        self.webdriver.find_element_by_css_selector('.mylist-01 a[href="/journal"]').click()
        return  Journal()








