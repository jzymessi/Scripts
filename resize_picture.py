# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image
import os.path

'''修改图片文件大小jpgfile：图片文件；savedir：修改后要保存的路径'''

def convertjpg(jpgfile, savedir, width=224, height=224):
    img = Image.open(jpgfile)
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(savedir, os.path.basename(jpgfile)))

'''查找给定路径下图片文件，并修改其大小'''
def modifyjpgSize(file, saveDir):
    for jpgfile in glob.glob(file):
        convertjpg(jpgfile, saveDir)

# 测试代码
file = r'D:\test2\restImage\*.jpg'
saveDir = r'D:\test2\outImage'
modifyjpgSize(file, saveDir)

