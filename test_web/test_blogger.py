from .base import Base
from .home import Home
import allure
import pytest

@allure.feature('个人博客测试用例执行情况')
class TestCase():

    def setup_class(self):
        self.home=Home()
        self.base=Base()

    def teardown_class(self):
        self.base.close()

    @pytest.mark.parametrize('a,b',[('测试','网站测试'),('网站开发','网站开发'),('系统','操作系统'),('程序算法','程序算法')])
    @allure.story('模糊查询相关的数据并且断言')
    def testcase1(self,a,b):
        self.home.goto_home(a).goto_seek(b)
        allure.attach.file(f'./result/{b}.png', f'{b}.png', attachment_type=allure.attachment_type.PNG)


    @allure.story('点击全部文章，并筛选出数据')
    def testcase2(self):
        self.home.goto_complete(8)

    @pytest.mark.parametrize('c,d',[(1,'网站测试'),(2,'网站开发'),(3,'操作系统'),(4,'深度学习'),(5,'程序算法'),(6,'其他')])
    @allure.story('导航栏页签测试，并筛选出数据')
    def testcase3(self,c,d):
        self.home.goto_webtest(c,d)
        allure.attach.file(f'./result/{c}.png', f'{c}.png', attachment_type=allure.attachment_type.PNG)



    @allure.story('一键返回顶部事件')
    def testcase4(self):
        self.home.goto_slide(200,2000)


    @allure.story('日志文章数据测试')
    def testcase5(self):
        self.home.goto_journal().goto_complete(13)

    @allure.story('动态数据测试核对')
    def testcase6(self):
       self.home.goto_journal().goto_dynamic().goto_V_date(25)

    @allure.story('关于我留言模块功能测试')
    @pytest.mark.parametrize('name,mailbox,url,msg',[('小小','1607187254@qq.com','www.baidu','最近没看到你更新博客'),('','1607187254@qq.com','www.baidu','博主很帅'),
     ('小小','','www.baidu','最近没看到你更新博客'),('小小','1607187254@qq.com','www.baidu',''),('小宏','1607187254@qq.com','','最近没看到你更新博客'),
     ('小小','1607187254.com','www.baidu','最近没看到你更新博客')])
    def testcase7(self,name,mailbox,url,msg):
      self.home.goto_journal().goto_dynamic().goto_v_about().goto_about_msg(name,mailbox,url,msg)



    @allure.story('友情链接功能测试')
    @pytest.mark.parametrize("urlname,mailbox,url,msgtext",[('','1607187254@qq.com','https://www.baidu.com/','1'),
    ('博客园官网','','https://www.baidu.com/','1'),('','1607187254@qq.com','','1'),
    ('博客园官网','1607187254@qq.com','https://www.baidu.com/',''),('博客园官网','1607187254@.com','https://www.baidu.com/','1'),('博客园官网','1607187254@qq.com','https://www.baidu.com/','1'),])
    def testcase8(self,urlname,mailbox,url,msgtext):
        self.home.goto_journal().goto_dynamic().goto_v_about().goto_friendship().goto_friendship_msg(urlname,mailbox,url,msgtext)

if __name__=='__main__':
    pytest.main()




#先在谷歌目录执行下面命令，开启一个本地端口好复用游览器
#chrome --remote-debugging-port=9222
#pytest test_blogger.py  -v  --alluredir ./result/  执行用例生成测试套件
# allure generate ./result/ -o ./report/ --clean    生成html文件测试报告

