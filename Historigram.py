__author__ = 'Dell'

from PIL import Image
from operator import itemgetter

im = Image.open("captcha.jpg")
im = im.convert("P")
his = im.histogram()

values = {}

mostpixels = []

def historigram():

    for i in range(256):
        values[i] = his[i]

    print('Id ' + 'Number of pixels')

    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        print(j,k)
        mostpixels.append([j,k])

    return mostpixels