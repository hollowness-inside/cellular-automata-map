from PIL import Image

from mapgen import mapgen

data = mapgen((64, 64), smooth=5)

img = Image.new("1", (64, 64))
img.putdata(data)
img.save('map.png')
