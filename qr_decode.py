import cv2
from pyzbar.pyzbar import decode
import numpy as np

# 读取二维码图片
img = cv2.imread('wechat-qr.png')

# 解码二维码
result = decode(img)

# 输出解码结果
for obj in result:
    print('类型:', obj.type)
    print('数据:', obj.data.decode('utf-8'))
