# from PIL import Image, ImageDraw
#
# # Create a new image with black background
# img = Image.new('RGB', (1080, 2504), color = 'black')
#
# # Create a mask with rounded corners
# mask = Image.new('L', (1080, 2504), 0)
# draw = ImageDraw.Draw(mask)
# draw.pieslice([(0, 0), (200, 200)], 180, 270, fill=255)
# draw.pieslice([(0, 2504-200), (200, 2504)], 90, 180, fill=255)
# draw.pieslice([(1080-200, 0), (1080, 200)], 270, 360, fill=255)
# draw.pieslice([(1080-200, 2504-200), (1080, 2504)], 0, 90, fill=255)
#
# # Apply the mask to the image
# img.putalpha(mask)
#
# # Save the image as PNG format
# img.save('image.png')

from PIL import Image, ImageDraw

img = Image.new('RGB', (200, 200), color = 'white')

# 创建一个ImageDraw对象
draw = ImageDraw.Draw(img)

# 绘制矩形
draw.rectangle((50, 50, 150, 150), fill ='black')

# 显示图像
img.show()
