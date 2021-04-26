import urllib.request
import  requests
import os
import re
import ssl
import random
import datetime

# 全局忽视证书
ssl._create_default_https_context = ssl._create_unverified_context


class Test_Case():

    def setup(self):

        self.s=requests.session()
        self.s.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        }

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)




    def teardown(self):
        pass



    def test_case1(self):
        #爬取图片url
        #<img src="https://.*?\.jpg"  匹配图片正则
        list= []
        for i in range(1,10):
            url1=f"https://8xhjdj.xyz/html/category/photo/list_7_{i}.html"
            url2=f"http://article.photofans.cn/vision/gallery/beauty/?page={i}"
            url3=f"http://article.photofans.cn/vision/?page={i}"
            res=self.s.get(url3).text
            pic_url = re.findall('<img src="http://.*?\.jpg"', res, re.S)
            '''
               如果没有匹配到数据则什么也不做，直接pass，如果查匹配
               数据成功了，则进一步判断是否有data文件夹，没有则创建，
               写入匹配的的数据，其他匹配也是同理。
            '''
            if pic_url==[]:
                pass

            else:
                #判断文件夹是否为空，为空则创建文件夹
                data = os.getcwd() + r"\data/"
                if not os.path.exists(data):
                    os.mkdir(data)

                #写入匹配到的数据
                with open(f'{data}img1.txt', 'a+') as f:
                    for p in pic_url:
                        # lstrip():去掉字符串左边的头部rstrip()去掉右半的头部
                        url =p.lstrip('<img src="').rstrip('"')
                        list.append(url)
                        f.write(url + '\n')



    def test_case2(self):
        #下载图片
        with open('data/img1.txt', 'r') as f:
            list = []
            list1=[]
            for i in f:
                if i==" \n":
                    pass
                else:
                    list.append(i.rstrip("\n"))


            #去重复
            for e in list:
                if e!="" and e !="#":
                    if e not in list1:
                       list1.append(e)


            #将网页中的图片下载至文件夹
            for i in range(len(list1)):

                #返回当前路径
                img=os.getcwd() + r"\img/"
                if not os.path.exists(img):
                    os.mkdir(img)

                filename = f"{img}{i}.jpg"
                pic = list1[i]
                # 下载图片至本地文件夹
                urllib.request.urlretrieve(pic,filename)



    def test_case3(self):
        #爬取网页视频链接
        list= []
        for i in range(1,3):
            url1 = f"https://8x01x5.xyz/html/other/index_21_{i}.html"
            res = self.s.get(url1).text
            pic_url1=re.findall('<a href="/html/4.*?\/"', res, re.S)
            if pic_url1==[]:
                pass
            else:
                data = os.getcwd() + r"\data/"
                if not os.path.exists(data):
                    os.mkdir(data)

                with open(f'{data}pictures.txt', 'a+') as f:
                    for p in pic_url1:
                         # lstrip():去掉字符串左边的(头部)
                        url = p.lstrip('<a href="').rstrip('"')
                        list.append(url)
                        f.write("https://8xhjdj.xyz"+url + '\n')





    def test_case4(self):

        #读取网页视频页面的url
        with open('data/pictures.txt', 'r') as f:
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
            res=self.s.get(url).text
            pic_url1 = re.findall('<a href="https://ppp.downloadxx.com/assets/.*?\.mp4"', res, re.S)
            if pic_url1==[]:
                pass

            else:
                url=pic_url1[0].lstrip('<a href="').rstrip('"')
                data = os.getcwd() + r"\data/"
                if not os.path.exists(data):
                    os.mkdir(data)

                #把匹配到的视频下载链接写进文件
                with open(f'{data}mp4.txt', 'a+') as f:
                    f.write("h"+url + '\n')




    def test_case5(self):
        #视频下载
        list= []
        list1 = []
        with open('data/mp4.txt', 'r') as f:
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

            #下载视频文件
            filename = f"{mp4}{i}.mp4"
            pic = list1[i]
            urllib.request.urlretrieve(pic, filename)






    #匹配没有协议开头的图片地址
    def test_case6(self):
        #图片url筛选
        list = []
        for i in range(1,10):
            url1=f"https://www.ivsky.com/tupian/katongtupian/index_{i}.html"
            url2 = f"https://www.ivsky.com/bizhi/yingshi/index_{i}.html"
            res = self.s.get(url2).text
            pic_url = re.findall('<img src="(.*?)"', res, re.S)
            if pic_url==[]:
                pass
            else:
                data = os.getcwd() + r"\data/"
                if not os.path.exists(data):
                    os.mkdir(data)

                with open('../reptile/data/img2.txt', 'a+') as f:
                    for p in pic_url:
                        # lstrip():去掉字符串左边的(头部) rstrip去掉右边的头部
                        url = p.lstrip('<img src="').rstrip('"')
                        f.write("https:"+url + '\n')





    #所有的a标签筛选，写入文件
    def test_case7(self):
        # 链接筛选
        list = []
        for i in range(1,11):
            url1=f"https://www.ivsky.com/tupian/katongtupian/index_{i}.html"
            url2 = f"https://www.ivsky.com/tupian/wupin/index_{i}.html"
            res = self.s.get(url2).text
            pic_url = re.findall('<a href="(/tupian.*?)"', res, re.S)
            if pic_url==[]:
                pass
            else:
                data = os.getcwd() + r"\data/"
                if not os.path.exists(data):
                    os.mkdir(data)

                with open('data/img3.txt', 'a+') as f:
                    for p in pic_url:
                        # lstrip():去掉字符串左边的(头部) rstrip去掉右边的头部
                        url = p.lstrip('<a href="').rstrip('"')
                        print(url)
                        f.write("https://www.ivsky.com"+url + '\n')




    #每次进点击a标签筛选图片地址
    def test_case8(self):
        # 读取网页img的url
        with open('data/img3.txt', 'r') as f:
            list = []
            list1 = []
            for i in f:
                if i == "":
                    pass
                else:
                    list.append(i)

            # 去重复
            for e in list:
                for e in list:
                    if e not in list1:
                        list1.append(e)

        for j in list1:
            url = j.rstrip("\n")
            res = self.s.get(url).text
            pic_url1 = re.findall('<img src="(.*?)"', res, re.S)
            if pic_url1==[]:
                pass
            else:
                url = pic_url1[0].lstrip('<img src="').rstrip('"')
                data = os.getcwd() + r"\data/"
                if not os.path.exists(data):
                    os.mkdir(data)

                # 把匹配到的图片url下载链接写进文件
                with open(f'{data}img4.txt', 'a+') as f:
                    f.write("https:" + url + '\n')



    #把匹配到的图片下载到本地
    def test_case9(self):
        # 下载图片
        with open('data/img4.txt', 'r') as f:
            list = []
            list1 = []
            for i in f:
                if i == " \n":
                    pass
                else:
                    list.append(i.rstrip("\n"))

            # 去重复
            for e in list:
                if e != "" and e != "#":
                    if e not in list1:
                        list1.append(e)


            # 将网页中的图片下载至文件夹
            for i in range(len(list1)):
                # 返回当前路径
                img = os.getcwd() + r"\img/"
                if not os.path.exists(img):
                    os.mkdir(img)
                filename = f"{img}{i}.png"
                pic = list1[i]
                # 下载图片至本地文件夹
                urllib.request.urlretrieve(pic, filename)
