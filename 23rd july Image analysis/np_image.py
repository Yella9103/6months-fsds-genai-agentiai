import numpy as np # Image processing with NumPy
import pandas as pd #
import matplotlib.pyplot as plt # Plotting library
from PIL import Image
import requests
from io import BytesIO # Load image from URL

def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

virat_url = "https://st1.latestly.com/wp-content/uploads/2025/05/Virat-Kohli-Wallpapers-in-Test-Format-14.jpg"
#virat_url = "https://img1.hscicdn.com/image/upload/f_auto,t_ds_w_1200,q_50/lsci/db/PICTURES/CMS/401600/401666.jpg"
virat = load_image_from_url(virat_url)

#display an original image
plt.figure(figsize=(6,6))
plt.imshow(virat)
plt.title('Virat')
plt.axis('off')
plt.show()

# image to array
virat_np = np.array(virat)
print('Virat Image shape', virat_np.shape)

#display grayscale image
virat_gray = virat.convert('L')


plt.figure(figsize=(6,6))
plt.imshow(virat_gray, cmap='gray')
plt.title('Virat(grayscale)')
plt.axis('off')
plt.show()