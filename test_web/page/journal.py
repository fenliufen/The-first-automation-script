from time import sleep
from .base import Base
from .dynamic import Dynamic


class Journal(Base):

    #验证日志文章数据是否一致 因为其他的都是home页面一样所以只需要核对数据就行
  def goto_complete(self,val):

      sleep(1)
      list = self.webdriver.find_elements_by_css_selector('.list li')
      lens = len(list)
      assert lens==val
      if lens==val:
          print(f'现在日志文章总共有{lens}条数据,数据一致')
      else:
          print(f'现在日志文章总共有{lens}条数据,与实际结果不一致')

      return self



  #去动态页面
  def goto_dynamic(self):
      self.webdriver.find_element_by_css_selector('.mylist-01 a[href="/dynamic"]').click()
      return Dynamic()