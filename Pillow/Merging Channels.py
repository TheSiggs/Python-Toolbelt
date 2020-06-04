from PIL import Image

zan = Image.open('zancolour.jpg')
brid = Image.open('con-bri.jpg')
r1, g1, b1 = zan.split()
r2, g2, b2 = brid.split()

new_img = Image.merge('RGB', (r2, g2, b1))
# zan.show()
# brid.show()
new_img.show()