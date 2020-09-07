from .about import About
from .base import Base
from time import sleep


class Dynamic(Base):
    #验证动态页面数据是否一致
    def goto_V_date(self,val):
        self.webdriver.execute_script("window.scrollTo('100','1000')")
        sleep(1)
        self.webdriver.execute_script("window.scrollTo('1000','100')")
        sleep(1)
        list=self.webdriver.find_elements_by_css_selector('.logo a')
        lens= len(list)

        if lens==val:
            print(f'现在动态里边有{lens}条数据,数据一致')
        else:
            print(f'断言失败，现在动态数据是{lens}条')


    def goto_v_about(self):
        self.webdriver.find_element_by_css_selector('.mylist-01 a[href="/about"]').click()
        return About()