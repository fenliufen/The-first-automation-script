import  pytest
import  allure
from faker import Faker
from test_api_pige.operation import Operation



@allure.feature('api测试')
class TestCase():
    def setup(self):
        self.add=Operation()
        self.faker = Faker(locale='zh_CN')
        self.ip = 'https://qyapi.weixin.qq.com'

    def teardown(self):
        pass


    @allure.story('添加部门')
    def testcase1(self):
        data = {
            "method": "post",
            "url": f"{self.ip}/cgi-bin/department/create?",
            "json": {
                "name":f"{self.faker .company()}",
                "name_en": f"{self.faker.user_name()}",
                "parentid": 1,
            }
        }

        res=self.add.add_section(data)
        assert res['errcode']==0



    @allure.story('测试函数')
    def test_testcase2(self):
        print(self.faker.user_name())






#pytest test_apics.py  -v  --alluredir ./result/  执行用例生成测试套件
# allure generate ./result/ -o ./report/ --clean    生成html文件测试报告
