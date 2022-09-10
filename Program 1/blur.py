from PIL import Image, ImageFilter

before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(10)) #<-- Change this number for more (+) or less (-) blur.
after.save("out.bmp") #This will provide a new file, with the image that is blurred. 

"""
Change the "boxblur()" number to get different levels of blur.
"""


"""
HOW TO RUN

1. CD into blur file
2. Run in terminal "python blur.py"

"""