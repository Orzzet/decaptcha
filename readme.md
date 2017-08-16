# Decaptcha

## Description

Get the characters of a simple captcha. You need to train the cracker before.

## Dependencias

* [pillow](https://pypi.python.org/pypi/Pillow/) Fork de PIL para el manejo de imágenes.

## Usage

### Training

Open trainer.py to see an interface that guides you through the training.

Click "Historigram" to select a captcha image.

Select which parts of the historigram you want to see (from the historigram or the cells) select "test" and click 
"Get icons". Check if you can clearly see the desired characters. Repeat this process until the characters can be seen
clearly.

Deselect "test" and click "Get icons". New files containing the letters should have been created. Move the characters
to the right folder of "iconset" (p.e: move an image containing "a" to the folder /iconset/a).

Click "Crack test" and check if the training to solve that captcha was successful. If it was, you are gonna need the lower and upper bound of the histogram in order to crack similar captchas.

### Cracking

The file Crack.py contains the function solve_image(filename, lowerpix, higherpix) that returns a string with the
characters of the captcha.

~~~
from Crack import *

filename = "captcha.jpg"
lowerpix = 100
higherpix = 200

solution = solve_image(filename, lowerpix, higherpix)
print(solution)

~~~
