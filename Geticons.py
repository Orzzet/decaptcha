__author__ = 'Dell'

from PIL import Image, ImageTk
import hashlib
import time

def geticons(filename, lowerpix = 1, higherpix = 200, test = 1):

    im = Image.open(filename)
    im2 = Image.new("P",im.size,255)
    im = im.convert("P")
    temp = {}

    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            temp[pix] = pix
            if pix >= lowerpix and pix <= higherpix: # these are the numbers to get
                im2.putpixel((y,x),0)

    #count = 0
    #for i in im.histogram():
    #  print(count,i)
    #  count += 1
    imout = im2
    if test==1:
        return(ImageTk.PhotoImage(imout))
    im2.save("output.png")

    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []


    for y in range(im2.size[0]): # slice across
        for x in range(im2.size[1]): # slice down
            pix = im2.getpixel((y,x))
            if pix != 255:
                inletter = True

        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start, end))

        inletter=False

    count = 0
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))

        update = str(time.time()) + str(count)
        m.update(update.encode('utf-8'))

        im3.save("./%s.gif" % (m.hexdigest()))
        count += 1

    return(ImageTk.PhotoImage(imout))