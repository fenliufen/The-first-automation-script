import requests
import pytest
from faker import Faker
import json


ip='https://qyapi.weixin.qq.com'

@pytest.fixture(autouse=True)
def token():
     corpid='ww9d15d2c2087d997e'
     corpsecre='tTVu4kSZ47qpvuKD6ng6VE_mxATs73KbdAnm54y6GWU'
     route=f'/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecre}'
     re=requests.get(ip+route)
     return re.json()['access_token']




class TestCase():

     def setup(self):
         self.faker=Faker(locale='zh_CN')
         self.data = {
              "userid": f'{self.faker.random_number(digits=7)}',
              "name": f'{self.faker.name()}',
              "mobile": f'{self.faker.phone_number()}',
              "department": [2],
         }


     def teardown(self):
          pass


     def test_add(self,token):
          print(f'我添加了{self.data["name"]}')
          route=f'/cgi-bin/user/create?access_token={token}'
          res=requests.post(ip+route,json=self.data).json()
          print(json.dumps(res,ensure_ascii=False, sort_keys=True, indent=4,))



     def test_delete(self,token):
         route=f'/cgi-bin/user/simplelist?access_token={token}&department_id=2&fetch_child=0'
         res=requests.get(ip+route).json()
         del_route=f'/cgi-bin/user/delete?access_token={token}&userid={res["userlist"][1]["userid"]}'
         print(f'我删除了{res["userlist"][1]["name"]}')
         print(requests.get(ip + del_route).json())
