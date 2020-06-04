from PIL import Image

eve = Image.open('evecon.jpg')
square_eve = eve.resize((686, 1500))
flip_eve = eve.transpose(Image.FLIP_LEFT_RIGHT)
spin_eve = eve.transpose(Image.ROTATE_90)

eve.show()
square_eve.show()
flip_eve.show()
spin_eve.show()
