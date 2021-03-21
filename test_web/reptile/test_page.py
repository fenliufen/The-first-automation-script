from urllib.request import urlretrieve
import  requests
import os
import re
import time
import ssl
import random






class Test_Case():

    #全局忽视证书
    ssl._create_default_https_context = ssl._create_unverified_context


    def setup(self):
        self.s=requests.session()
        self.s.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "sec-ch-ua":'Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99',
        }


    def teardown(self):
        pass



    def test_case1(self):
        #爬取图片url
        list= []
        for i in range(1,20):
            url1=f"https://8xhjdj.xyz/html/category/photo/list_7_{i}.html"
            url2=f"http://article.photofans.cn/vision/gallery/beauty/?page={i}"
            url3=f"https://sc.chinaz.com/tupian/meihuatupian_{i}.html"
            res=self.s.get(url1).text
            pic_url = re.findall('<img src="https://.*?\.jpg"', res, re.S)
            with open('picture.txt', 'a+') as f:
                for p in pic_url:
                    # lstrip():去掉字符串左边的(头部)
                    url =p.lstrip('<img src="').rstrip('"')
                    list.append(url)
                    print(url)
                    f.write(url + '\n')


    def test_case2(self):
        #下载图片
        with open('picture.txt', 'r') as f:
            list = []
            list1=[]
            for i in f:
                if i=="":
                    pass
                else:
                    list.append(i.rstrip("\n"))


            #去重复
            for e in list:
                if e!="":
                    if e not in list1:
                       list1.append(e)

            print(list1)
            # 将网页中的图片下载至文件夹
            for i in range(len(list1)):

                #返回当前路径
                img=os.getcwd() + r"\img/"
                if not os.path.exists(img):
                    os.mkdir(img)
                else:
                    filename = f"{img}{str(random.randint(111111,999999))}.png"
                    pic = list1[i]
                    # 下载图片至本地文件夹
                    urlretrieve(pic, filename)



    def test_case3(self):
        #爬取网页视频链接
        list= []
        for i in range(12,15):
            url1 = f"https://8xhjdj.xyz/html/category/video/video1/page_{i}.html"
            res = self.s.get(url1).text
            pic_url1=re.findall('<a href="/html/4.*?\/"', res, re.S)


            with open('pictures.txt', 'a+') as f:
                for p in pic_url1:
                    # lstrip():去掉字符串左边的(头部)
                    url = p.lstrip('<a href="').rstrip('"')
                    list.append(url)
                    f.write("https://8xhjdj.xyz"+url + '\n')





    def test_case4(self):
        #读取网页视频页面的url
        with open('pictures.txt', 'r') as f:
            list = []
            list1=[]
            for i in f:
                if i=="":
                    pass
                else:
                    list.append(i)

            # 去重复
            for e in list:
                for e in list:
                    if e not in list1:
                        list1.append(e)

        for j in list1:
            url=j.rstrip("\n")
            time.sleep(1)
            res=self.s.get(url).text
            time.sleep(1)
            pic_url1 = re.findall('<a href="https://ppp.downloadxx.com/assets/.*?\.mp4"', res, re.S)
            url=pic_url1[0].lstrip('<a href="').rstrip('"')

            #把匹配到的视频下载链接写进文件
            with open('mp4.txt', 'a+') as f:
                f.write("h"+url + '\n')




    def test_case5(self):

        #视频下载
        list= []
        list1 = []
        with open('mp4.txt', 'r') as f:
            for i in f:
                if i=="":
                    pass
                else:
                    list.append(i.rstrip("\n"))


        # 去重复
        for e in list:
            if e !="":
                if e not in list1:
                    list1.append(e)


        # 将网页中的视频下载至文件夹
        for i in range(len(list1)):
            mp4 = os.getcwd() + r"\mp4/"
            if not os.path.exists(mp4):
                os.mkdir(mp4)
            else:
                filename = f"{mp4}{str(random.randint(111111,999999))}.mp4"
                pic = list1[i]
                urlretrieve(pic, filename)