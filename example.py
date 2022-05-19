from PIL import Image

from mapgen import generate


img = Image.new("1", (64, 64))

data = generate((64, 64), smooth=5)
img.putdata(data)

img.save('map.png')
