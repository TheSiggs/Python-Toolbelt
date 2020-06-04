from PIL import Image
from PIL import ImageFilter

zan = Image.open('zancolour.jpg')

black_white = zan.convert("L")
color = zan.convert("RGB")
printer = zan.convert("CMYK")
blur = zan.filter(ImageFilter.BLUR)
detail = zan.filter(ImageFilter.DETAIL)
edges = zan.filter(ImageFilter.FIND_EDGES)
contour = zan.filter(ImageFilter.CONTOUR)

color.show()
black_white.show()
printer.show()
blur.show()
detail.show()
edges.show()
contour.show()
