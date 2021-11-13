import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt
 
def imshow(X, resize=None):
    image=Image.fromarray(X)
    if resize!= None:
        resized_img=image.resize(resize)
    return plt.imshow(resized_img)
