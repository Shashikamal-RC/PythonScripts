# works only python 2 (don't use python3 to execute)
from PIL import Image, ImageFilter

# opening image
img = Image.open('./Images/pikachu.jpg')

print(img) #image info
print(img.mode) #image mode info

# applying blur filters
filterd_image = img.filter(ImageFilter.BLUR)
filterd_image.save("./Images/blur_pikachu.png", 'png')

# applying smooth filter
filterd_image = img.filter(ImageFilter.SMOOTH)
filterd_image.save("./Images/smooth_pikachu.png", 'png')

# applying sharp filter
filterd_image = img.filter(ImageFilter.SHARPEN)
filterd_image.save("./Images/sharp_pikachu.png", 'png')

# converting an image to gray scale
filterd_image = img.convert("L")
filterd_image.save("./Images/gray_pikachu.png", 'png')

# show the image
# filterd_image.show()

# rotating the images
filterd_image = img.convert("L")
crooked = filterd_image.rotate(90)
crooked.save("./Images/rotated_pikachu90.png", 'png')

filterd_image = img.convert("L")
crooked = filterd_image.rotate(180)
crooked.save("./Images/rotated_pikachu180.png", 'png')

# resizing images
filterd_image = img.convert("L")
resize = filterd_image.resize((300,300)) #parameter should be tuple
resize.save("./Images/resize_pikachu.png", 'png') 

# croping image
filterd_image = img.convert("L")
box = (100, 100, 400, 400) #pixel location of 4 corners
region = filterd_image.crop(box)
region.save("./Images/croped_pikachu.png", 'png') 

image = Image.open('./Images/astro.jpg')
print(image.size) #size of the image

# resizing 
new_img = image.resize((400, 1400))
new_img.save("./Images/cropped_astro.png", 'png') # this will make image squished

#solution for that - thumbnail
image.thumbnail((400, 400))
image.save("./Images/thumbnail_astro.png", 'png') # this will not make image squished