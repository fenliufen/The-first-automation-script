# coding=utf-8
from reptile.page.base_page import Base



download=Base()



img_url="http://article.photofans.cn/vision/gallery/beauty/?page=1"
img_reg='<img src="http://.*?\.jpg"'  #匹配图片url正则
img_url_a="https://www.ivsky.com/tupian/katongtupian/index_1.html"
img_reg_a='<a href="(/tupian.*?)"'   #匹配链接正则
img_path="./data/img_1.txt"   #需要下载图片的文件



#图片下载
#download.img_url(img_url,img_reg).img_url_a(img_url_a,img_reg_a).img_download(img_path)
#download.img_download(img_path)



mp4_url_a="https://8x01x5.xyz/html/other/index_21_3.html"    #链接地址
mp4_url_reg='<a href="/html/4.*?\/"'     #a标签正则表达式-匹配链接下载视频
mp4_url_path="./data/mp4_1.txt"          #获取到的a标签，访问静态网页获取pm4链接
mp4_reg='<a href="https://ppp.downloadxx.com/assets/.*?\.mp4"'         #获取mp4链接




#MP4下载
# download.mp4_url_a(mp4_url_a,mp4_url_reg).mp4_url(mp4_url_path,mp4_reg)



al=["1","2","3","1","3","1","9","1","3","5","3","10","10"]
al2=[]
al3={}

for i in al:
    if i not in al2:
        al2.append(i)
        al3[i]=al.count(i)





print(al3)