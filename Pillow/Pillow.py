from PIL import Image

# Images
zan = Image.open('zancolour.jpg')
briget = Image.open('con-bri.jpg')
area = (250, 100, 700, 600)
zancropped = zan.crop(area)

# Pasting zancropped to briget
# xstart, ystart, xend, yend
area2 = (300, 600, 750, 1100)
briget.paste(zancropped, area2)

# Display Birdgets new look
briget.show()