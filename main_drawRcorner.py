from PIL import Image, ImageDraw, ImageFilter
import cv2
import numpy as np

# Step1: input parameters
width = 1080
height = 2504
radius = 100

# Step2: create a roundCorner resource
# Create a new image with black background
img = Image.new('RGB', (width, height), color = 'black') # 底板为纯黑图

# Create a mask with rounded corners
mask = Image.new('L', (width, height), 0)
draw = ImageDraw.Draw(mask)
# 左上
draw.rectangle((0, 0, radius, radius), fill ='white') # 矩形透明度最高
draw.pieslice([(0, 0), (2*radius, 2*radius)], 180, 270, fill=0) # 去除边缘
# 右上
draw.rectangle((width - radius, 0, width, radius), fill ='white') # 矩形透明度最高
draw.pieslice([(width-2*radius, 0), (width, 2*radius)], 270, 360, fill=0)
# 左下
draw.rectangle((0, height - radius, radius, height), fill ='white') # 矩形透明度最高
draw.pieslice([(0, height-2*radius), (2*radius, height)], 90, 180, fill=0)
# 右下
draw.rectangle((width - radius, height - radius, width, height), fill ='white') # 矩形透明度最高
draw.pieslice([(width-2*radius, height-2*radius), (width, height)], 0, 90, fill=0)

# Apply the mask to the image
img.putalpha(mask)

# Save the image as PNG format
img.save('image.png')

# Step3: blur the resource to smooth the edge of round corner
# this step can be skip if not necessary

# class MY_FILTER(ImageFilter.BuiltinFilter):
#     name = "my_filter"
#     # fmt: off
#     filterargs = (3, 3), 5, 0, (
#         1, 1, 1,
#         1, 5, 1,
#         1, 1, 1,
#     )
# blurred_image = img.filter(MY_FILTER)

blurred_image = img.filter(ImageFilter.SMOOTH)
blurred_image = blurred_image.filter(ImageFilter.SMOOTH) # if one blur is not enough, 2 blur can be done

# blurred_image.save('blur.png')

# Step4: use opencv to deal with the image
# 使用opencv进行处理边缘
img3 = cv2.imread('pic_whiteBackGround.png')  # pic_whiteBackGround.png should be white background
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

middleNumber = 7  # the middle number of the 3x3 smooth kernel
kernel = np.array([[1, 1, 1], [1, middleNumber, 1], [1, 1, 1]]) / (8 + middleNumber)
img3 = cv2.filter2D(img3, -1, kernel)
img3 = cv2.copyMakeBorder(img3, 0, 0, 0, 0, cv2.BORDER_CONSTANT)
cv2.imwrite('output.png', img3)

print('width =', width, 'height =', height, 'radius =', radius)