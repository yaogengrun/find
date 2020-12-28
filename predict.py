# -------------------------------------------------
# @Time    : 2020/11/22 17:24
# @Author  : RunRun
# @Software: PyCharm
# -------------------------------------------------
# 功能
#
#  模型进行图片的测试
#
from nets.yolo3 import yolo_body
from keras.layers import Input
from yolo import YOLO
from PIL import Image

yolo = YOLO()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)
        r_image.show()
yolo.close_session()
