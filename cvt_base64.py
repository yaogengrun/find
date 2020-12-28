import base64
import os
import cv2
import numpy as np


def cvt_img2b64(img):
    """
    :param img: image : numpy array
    :return: base64 code
    """
    flag, img_encode = cv2.imencode('.jpg', img)
    if flag:
        b64encode = base64.b64encode(img_encode)
        return b64encode
    else:
        raise Exception("Can not encode image")


def cvt_b642img(filepath: str):
    """
    :param filepath:base64 file path
    :return: image : numpy array
    """
    assert os.path.exists(filepath), "File not exists!"
    with open(filepath, 'rb') as f:
        decode = base64.b64decode(f.read())
    nparr = np.frombuffer(decode, np.int8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

