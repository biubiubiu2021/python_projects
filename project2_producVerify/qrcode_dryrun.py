import qrcode
import PIL.Image as Image

qr = qrcode.QRCode(version=4, error_correction=qrcode.ERROR_CORRECT_L, box_size=8, border =1)
qr.add_data("www.baidu.com")
qr.make(fit=True)
img = qr.make_image(fill_color="grey", back_color="white")#设置二维码颜色
# 加载Logo图像
logo = Image.open(".\\doge.png") #设置二维码背景图片
# 计算Logo的位置
logo_width, logo_height = logo.size
img_width, img_height = img.size
logo_position = ((img_width - logo_width) // 2, (img_height - logo_height) // 2)

# 将Logo嵌入二维码中
img.paste(logo, logo_position,mask=None)

img.show()