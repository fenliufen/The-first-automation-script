# coding=utf-8
from reptile.page.create_dir import directory
import urllib.request
import requests
import os
import re
import ssl
import random


class Base:


    # 忽略证书
    ssl._create_default_https_context = ssl._create_unverified_context


    def __init__(self):
        self.s = requests.session()
        self.s.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        }

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        directory()







    def Schedule(self, a, b, c):
        percent = 100.0 * a * b / c
        if percent > 100:
            percent = 100
        print("%4.2f%%" %(percent))





    def img_url(self, url, reg):

        if url == "":
            print("url 参数必填")
            return

        if reg == "":
            print("reg 参数必填")
            return

        list = []
        res = self.s.get(url).text
        pic_url = re.findall(reg, res, re.S)

        if pic_url == []:
            print("没有爬取到数据，请检查正则表达式是否正确")
            return

        else:

            # 当前的工作目录
            data = os.getcwd() + r"\data/"

            with open(f'{data}img_1.txt', 'w') as f:
                for i in range(len(pic_url)):
                    # lstrip():去掉字符串左边的头部rstrip()去掉右半的头部
                    url = pic_url[i].lstrip('<img src="').rstrip('"')
                    list.append(url)
                    f.write(url + '\n')

                print(f"爬取到了{len(pic_url)}条图片下载链接数据，爬取数据成功！")

        return self







    def img_url_a(self, url, reg):

        if url == "":
            print("url 参数必填")
            return

        if reg == "":
            print("reg 参数必填")
            return


        res = self.s.get(url).text
        pic_url = re.findall(reg, res, re.S)

        if pic_url == []:

            print("没有爬取到数据，请检查正则表达式是否正确")
            return

        else:
            # 当前的工作目录
            data = os.getcwd() + r"\data/"
            with open(f'{data}img_2.txt', 'w') as f:
                for p in pic_url:
                    # lstrip():去掉字符串左边的(头部) rstrip去掉右边的头部
                    url = p.lstrip('<a href="').rstrip('"')
                    f.write(url + '\n')

                print(f"爬取到了{len(pic_url)}条img跳转链接数据，爬取数据成功！")

        return self








    def img_download(self, path):

        list = []
        list1 = []

        if path == "" or path is None:
            print("path 参数不能为空")
            return

        with open(path, 'r') as f:

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
                filename = f"{img}{str(random.randint(111111,999999))}.png"
                pic = list1[i]
                # 下载图片至本地文件夹
                urllib.request.urlretrieve(pic, filename, self.Schedule)

            print("所有图片下载完成！")

        return







    def mp4_url_a(self, url, reg):
        if url == "":
            print("url 参数必填")
            return

        if reg == "":
            print("reg 参数必填")
            return

        # 爬取网页视频链接
        list = []
        res = self.s.get(url).text
        pic_url1 = re.findall(reg, res, re.S)
        if pic_url1 == []:

            print("没有爬取到数据，请检查正则表达式是否正确")
            return

        else:
            data = os.getcwd() + r"\data/"
            with open(f'{data}mp4_1.txt', 'w') as f:
                for p in pic_url1:
                    # lstrip():去掉字符串左边的(头部)
                    url = p.lstrip('<a href="').rstrip('"')
                    list.append(url)
                    f.write("https://8xhjdj.xyz" + url + '\n')
            print(f"爬取到了{len(pic_url1)}条mp4跳转链接，爬取数据成功！")

        return self






    def mp4_url(self, path, reg):
        # 读取网页视频页面的url
        with open(path, 'r') as f:
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
            pic_url1 = re.findall(reg, res, re.S)
            if pic_url1 == []:

                print("没有爬取到数据，请检查正则表达式是否正确")
                return

            else:
                url = pic_url1[0].lstrip('<a href="').rstrip('"')
                data = os.getcwd() + r"\data/"
                with open(f'{data}mp4_2.txt', 'a+') as f:
                    f.write("h"+url + '\n')

        print(f"一共匹配了{len(list1)}条mp4的下载链接！")

        return self
