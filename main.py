from PIL import Image, ImageDraw
width = 1080
height = 2504
radius = 100
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

print('width =', width, 'height =', height, 'radius =', radius)


