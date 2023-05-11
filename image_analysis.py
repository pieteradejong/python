from PIL import Image
import os


cwd = os.getcwd()
IMG_DIR_LOCATION = "../../resources/stock_photo_frog_on_palm_frond.jpeg"

im = Image.open(IMG_DIR_LOCATION)
# for _ in dir(im):
# 	print(_)

print()
print("getexif:")
exif = im.getexif()
print(exif)

print()
print("entropy:")
entropy = im.entropy()
print(entropy)

print()
print("colors:")
colors = im.getcolors()
print(colors)


print()
print("data:")
data = im.getdata()
print(data)

print()
print("palette:")
palette = im.getpalette()
print(palette)

print()
print("histogram:")
histogram = im.histogram()
print(histogram)


