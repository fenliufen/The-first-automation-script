#coding=utf-8

import  os


def directory():

    data=os.getcwd() + r"\data/"
    img =os.getcwd() + r"\img/"
    mp4=os.getcwd() + r"\mp4/"

    if not os.path.exists(img):
        os.mkdir(img)

    if not os.path.exists(data):
        os.mkdir(data)

    if not  os.path.exists(mp4):
        os.mkdir(mp4)

    else:

        return