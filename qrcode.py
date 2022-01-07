from PIL import Image, ImageDraw
import qrcode
data = ""
img = qrcode.make(data)
img.save("Hello-world!.png")
