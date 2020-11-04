import json
import requests


class Base:
    def __init__(self):
        self.ip = 'https://qyapi.weixin.qq.com'



    def _token(self):
        corpid = 'ww9d15d2c2087d997e'
        corpsecre = 'tTVu4kSZ47qpvuKD6ng6VE_mxATs73KbdAnm54y6GWU'
        route = f'/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecre}'
        re = requests.get(self.ip + route)
        return re.json()['access_token']





    def send_api(self, data:dict):
        s=requests.session()
        s.params={
            "access_token": self._token()
        }
        res=s.request(**data).json()
        print(json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4, ))
        return  res












