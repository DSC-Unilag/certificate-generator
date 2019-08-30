from PIL import Image

def get_dim(path):
    img = Image.open(path)
    return img.width, img.height
