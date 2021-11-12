import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt
 
def imshow(X, resize=None):
    image=Image.fromarray(X)
    if resize!= None:
        img=image.resize(resize)
    return plt.imshow(img)
